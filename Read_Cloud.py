import sensor_msgs.point_cloud2 as pc2
import rospy
from srv import trimmed_scan


def on_scan(self, scan):
    rospy.loginfo("Got scan, projecting")
    points = pc2.read_points(scan, field_names = ("X", "Y", "Z"), skip_nans=True)
    print(type(points))
    return points
    # for p in points:
    #      print (" x : %f  y: %f  z: %f" %(p[0],p[1],p[2]))

def cloud_request():
    rospy.wait_for_service('trim_scan')
    try:
        req_trimmed = rospy.ServiceProxy('trim_scan', trimmed_scan)
        resp1 = req_trimmed()
        return resp1.trimmed
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", pc2, on_scan)

    cloud_request()
