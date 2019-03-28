from kukavarproxy import KUKA


class BigOrange():
	def __init__(self, robot_ip):
		self.robot = KUKA(robot_ip)

	def get_pose(self):
		""" get current robot pose"""
		return self.robot.read("$POS_ACT")

	def set_pose(self, var):
		""" set robot pose """
		return self.robot.write("$POS_ACT", var)

	def ex_path(self, i, val, var='REMOTEPOS'):
		""" execute a single path. blocking.
		assumes var is REMOTEPOS
		assumes i is int
		assumes val is robot position coords"""
		#remotepos[512] - can write an arrray length to each remotepos[0].. 1.. 2.. 3 etc etc
		return self.robot.write(var+"["+ str(i+1)+"]", val)

	def get_j(self):
		""" get current KUKA J user global"""
		return int(self.robot.read('J'))

	def set_out(self, out, state):
		""" set a digital out
		assumes out is int
		assumes state is bool"""
		return self.robot.write("$OUT["+str(out)+"]", state)

	def get_out(self, out):
		""" get digital out """
		return self.robot.read("$OUT[" + str(out) + "]")

	def get_axis(self):
		""" get current axis-specific setpoint position of the robot"""
		return self.robot.read("$AXIS_ACT")

	def gen_remotepos(self, j):
		return self.robot.write("REMOTEPOS[" + str(j + 1) + "]", test_array[j + adv])

	def extrude(self, pts):
		count = len(pts)
		advance = self.get_advance_run()
		hold_j = 1
		j = self.get_j()
		while j < count - 4:
			j = self.get_j()
			if j <= 1:
				print("Initializing . . .")
				self.robot.write("COUNT", count)
				self.gen_remotepos(0)
				self.gen_remotepos(1)
				self.gen_remotepos(2)
				self.gen_remotepos(3)
				self.gen_remotepos(4)
			elif hold_j != j:
				hold_j = j
				self.gen_remotepos(j, advance)
				print('writing to pos: ', j)



if __name__ == '__main__':
	print("Kir")
	test = BigOrange()
	test.extrude()
