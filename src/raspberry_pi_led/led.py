import rospy
from std_msgs.msg import String

class Led:
    def __init__(self):
        '''
            Lighthouse signer initialisation.
        '''
        rospy.init_node('raspberry_pi_led')
        rospy.loginfo("I'm alive");
        

        def callback(data):
            rospy.loginfo("I got the task");

        rospy.Subscriber('/task', String, callback)

    def spin(self):
        '''
            Waiting for the new messages.
        '''
        rospy.spin()
