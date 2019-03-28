import math
import time
import numpy as np
import matplotlib.pyplot as plt
import serial
import pandas as pd


def tr_to_tcp(cord):
	array = np.array([cord[1] * np.cos(cord[0]), cord[1] * np.sin(cord[0]), 0])
	matrix = np.array([[-1, 0, 0, 13.5], [0, 1, 0, 0], [0, 0, -1, 9.35], [0, 0, 0, 1]])

	arr1 = np.dot(matrix, np.append(array, 1))
	homo_array = np.delete(np.true_divide(arr1, arr1[3]), 3)
	return pd.Series({'X':homo_array[0], 'Y':homo_array[1], 'Z':homo_array[2]})


def main():
	dists = {}
	toPandas = {}
	with serial.Serial('/dev/ttyUSB0', 230400, timeout=5) as ser:
		ser.write(b'e')
		time.sleep(1)
		ser.write(b'b')

		start_count = 0
		fig = plt.figure()
		plt.ion()
		while True:
			got_scan = False
			while not got_scan:
				s = ser.read(1)
				if not s:
					continue
				if start_count == 0:
					if ord(s) == 0xFA:
						start_count = 1
						print("KIR")
				elif start_count == 1:
					if ord(s) == 0xA0:
						start_count = 0
						got_scan = True
						print("Kos")

						s += ser.read(2518)
						s = bytes([0xFA]) + s
						# print(len(s))

						for i in range(0, len(s), 42):
							# print(0xA0+i/42, ord(s[i]), ord(s[i+1]))
							if s[i] == 0xFA and s[i + 1] == 0xA0 + i / 42:
								# good_sets += 1
								# motor_speed += (ord(s[i+3]) << 8) + ord(s[i+2])
								# rpms = (ord(s[i+3]) << 8 | ord(s[i+2])) / 10

								for j in range(i + 4, i + 40, 6):
									index = 6 * (i / 42) + (j - 4 - i) / 6

									byte0 = s[j]
									byte1 = s[j + 1]
									byte2 = s[j + 2]
									byte3 = s[j + 3]

									dist = (byte3 << 8) + byte2
									dists[math.radians(359 - index)] = dist
									toPandas[359 - index] = [math.radians(359 - index), dist]

						# print('>>> ', dist, 359 - index)
					else:
						start_count = 0

			df = pd.DataFrame.from_dict(toPandas, orient='index')
			df = df[(df[1] < 400) & (df[1] > 0)].dropna()
			# df.apply()
			df[['X', 'Y', 'Z']] = df.apply(tr_to_tcp, axis=1)
			print(df)

			ax = fig.add_subplot(111, projection='polar')
			ax.set_ylim(00, 200)
			ax.scatter(dists.keys(), dists.values())
			plt.draw()
			plt.pause(0.0001)
			plt.clf()


if __name__ == '__main__':
	main()
