from kuka import BigOrange
from e6pos import Path_Planner

# import sensor_msgs.point_cloud2 as pc2
# import rospy
# from srv import trimmed_scan


# def on_scan(self, scan):
#     rospy.loginfo("Got scan, projecting")
#     points = pc2.read_points(scan, field_names = ("X", "Y", "Z"), skip_nans=True)
#     print(type(points))
#     return points
#
# def cloud_request():
#     rospy.wait_for_service('trim_scan')
#     try:
#         req_trimmed = rospy.ServiceProxy('trim_scan', trimmed_scan)
#         resp1 = req_trimmed()
#         return on_scan(resp1.trimmed)
#     except rospy.ServiceException as e:
#         print("Service call failed: %s"%e)


def main():
    # rospy.init_node('listener', anonymous=True)
    #
    # robot = BigOrange('192.168.1.100')
    # robot = BigOrange('127.0.0.1')
    planner = Path_Planner()
    # cloud = cloud_request()
    planner.set_cloud(5)
    plan = planner.plan_ptp((-100, -100, -100), (200, 200, 200), 45)
    print(plan)
    # robot.extrude(plan)


if __name__ == '__main__':
    main()
