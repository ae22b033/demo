#!/usr/bin/env python3 
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math 

def move(distance):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = distance
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    # Loop to move the turtle in an specified distance
    while current_distance < distance:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = vel_msg.linear.x * (t1 - t0)

    # Stopping the turtle after the movement is done
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

def rotate(angle):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angle

    # Setting the current time for angle calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    # Loop to rotate the turtle by the specified angle
    while current_angle < angle:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = vel_msg.angular.z * (t1 - t0)

    # Stopping the turtle after the rotation is done
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def square():
    rospy.init_node('turtle_square', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    move(2.0)  # Move forward
    rotate( (math.pi)/2)  # Rotate 90 degrees (1.57 radians)
    move(2.0)  # Move forward
    rotate( (math.pi)/2)  # Rotate 90 degrees
    move(2.0)  # Move forward
    rotate( (math.pi)/2)  # Rotate 90 degrees
    move(2.0)  # Move forward

def pose_callback(pose):
    print(f"Turtle Pose - X: {pose.x}, Y: {pose.y}, Theta: {pose.theta}")

if __name__ == '__main__':
    try:
        square()
    except rospy.ROSInterruptException:
        pass



