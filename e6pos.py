import numpy as np
import pandas as pd





class Path_Planner:
	template = "{{E6POS: X {}, Y {}, Z {}, A {}, B {}, C {}}}"

	def __init__(self):
		self.cloud = None
		self.step_size = 5

	def closest(self, pt):
		new = self.cloud.assign(dist=lambda x: (((x['X'] - pt[0]) ** 2) + ((x['Y'] - pt[1]) ** 2)))
		return new.loc[new["dist"].idxmin()][['Z', 'dist']]

	def set_cloud(self, cloud):
		self.cloud = pd.DataFrame(
			[[i, j, 5] for i in range(0, 200) for j in range(100, 400)],
			columns=(list("XYZ"))
		)

	def project(self, df):
		df[['Z', 'Dist']] = df.apply(self.closest, axis=1)
		print(df)
		return df

	def lin(self, lst):
		pts = [np.array(i) for i in lst]
		df = pd.DataFrame(pts, columns=list('XYZ'))
		df = self.project(df)
		return df

	def ptp(self, start, end):
		u = np.array(end - start)
		vec = u / np.sqrt(np.sum(u ** 2))
		length = np.sqrt(np.sum(u ** 2))
		pts = [vec * i + start for i in range(0, int(length), self.step_size)]
		pts.append(end)
		df = pd.DataFrame(pts, columns=list('XYZ'))
		df = self.project(df)
		return [tuple(x) for x in df.values]

	def plan_ptp(self, start, end, ang):
		end = np.array(end)
		start = np.array(start)

		return [self.template.format(*item[0:3], ang, 90, 0) for item in self.ptp(start, end)]


if __name__ == '__main__':
	planner = Path_Planner()
	planner.set_cloud(5)
	pt1 = np.array([0, 100, 0])
	pt2 = np.array([0, 300, 0])
	print(planner.ptp(pt1, pt2))