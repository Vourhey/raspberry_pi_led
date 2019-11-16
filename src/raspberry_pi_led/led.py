import rospy
import socket
from std_msgs.msg import String

class Led:
    def __init__(self):
        '''
            Lighthouse signer initialisation.
        '''
        rospy.init_node('raspberry_pi_led')
        rospy.loginfo("I'm alive");
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('raspberrypi', 8089))
        

        def callback(data):
            rospy.loginfo("I got the task");
            clientsocket.send(bytes('r', 'UTF-8'))

        rospy.Subscriber('/task', String, callback)

    def spin(self):
        '''
            Waiting for the new messages.
        '''
        rospy.spin()
