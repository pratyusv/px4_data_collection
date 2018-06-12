#!/usr/bin/env python

import math as mt
import numpy as np
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped
from mavros_msgs.msg import ActuatorControl
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode
from mavros_msgs.srv import SetModeRequest
from mavros_msgs.srv import SetModeResponse
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandBoolRequest
from mavros_msgs.srv import CommandBoolResponse
from sensor_msgs.msg import Imu
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_points",help="data_points",type=int)
args = parser.parse_args()
data_points = args.data_points


current_state = State()
imu_data = Imu()
act_controls = ActuatorControl()

PI = 3.14

k_p_yaw = 0.05
k_d_yaw = 0

k_p_pitch = 0.18
k_d_pitch = 0.045

k_p_roll = 0.18
k_d_roll = 0.045

x_f = []
y_f = []
z_f = []

vx_f = []
vy_f = []
vz_f = []

r_f = []
p_f = []
yaw_f = []


sin_r_f= []
sin_p_f= []
sin_y_f= []

cos_r_f= []
cos_p_f= []
cos_y_f= []

rs_f = []
ps_f = []
ys_f = []

x_des = []
y_des = []
z_des = []

u0 = []
u1 = []
u2 = []
u3 = []
sin_y_des = []
cos_y_des = []

ixx = 0.0347563
iyy = 0.0458929
izz = 0.0977
mass = 1.5

ix = []
iy = []
iz = []
m = []
yaw_des = 0

w_mag = []
w_x = []
w_y = []
w_z = []


a_x = []
a_y = []
a_z = []

aplha_x = []
aplha_y = []
aplha_z = []

ax_f = []
ay_f = []
az_f = []

def quaternion_to_euler_angle(w, x, y, z):
	ysqr = y * y

	t0 = +2.0 * (w * x + y * z)
	t1 = +1.0 - 2.0 * (x * x + ysqr)
	X = mt.degrees(mt.atan2(t0, t1))

	t2 = +2.0 * (w * y - z * x)
	t2 = +1.0 if t2 > +1.0 else t2
	t2 = -1.0 if t2 < -1.0 else t2
	Y = mt.degrees(mt.asin(t2))

	t3 = +2.0 * (w * z + x * y)
	t4 = +1.0 - 2.0 * (ysqr + z * z)
	Z = mt.degrees(mt.atan2(t3, t4))

	return X, Y, Z

local_velocity = TwistStamped()
def lv_cb(data):
	global local_velocity
	local_velocity = data



local_position = PoseStamped()
def lp_cb(data):
	global local_position
	local_position = data


def state_cb(data):
	global current_state
	current_state = data
	# flag = data.armed
	# print(flag)
	# rospy.loginfo(current_state.connected)


def imu_cb(data):
	global imu_data
	imu_data = data

def act_cb(data):
	global act_controls
	act_controls = data


def control():
	# sp = np.load("xy_sin.npy")

	state_sub = rospy.Subscriber("/mavros/state",State,state_cb,queue_size=10)

	rospy.wait_for_service('mavros/cmd/arming')
	arming_client = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)

	rospy.wait_for_service('mavros/set_mode')
	set_mode_client = rospy.ServiceProxy('mavros/set_mode', SetMode)

	acutator_control_pub = rospy.Publisher("/mavros/actuator_control",ActuatorControl,queue_size=10)

	local_pos_pub = rospy.Publisher("/mavros/setpoint_position/local",PoseStamped,queue_size=10)

	mocap_pos_pub = rospy.Publisher("/mavros/mocap/pose",PoseStamped,queue_size=10)

	imu_sub = rospy.Subscriber("/mavros/imu/data",Imu,imu_cb, queue_size=10)
	local_pos_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, lp_cb, queue_size=10)
	local_vel_sub = rospy.Subscriber("/mavros/local_position/velocity", TwistStamped, lv_cb, queue_size=10)
	act_control_sub = rospy.Subscriber("/mavros/act_control/act_control_pub", ActuatorControl,act_cb,queue_size=10)

	rospy.init_node('control',anonymous=True)
	rate =  rospy.Rate(50.0)

	# print("*"*80)
	while not rospy.is_shutdown() and not current_state.connected:
		rate.sleep()
		rospy.loginfo(current_state.connected)
	# print("#"*80)

	pose = PoseStamped()
	pose.pose.position.x = 0
	pose.pose.position.y = 0
	pose.pose.position.z = 3





	offb_set_mode = SetModeRequest()
	offb_set_mode.custom_mode = "OFFBOARD"


	arm_cmd = CommandBoolRequest()
	arm_cmd.value = True

	last_request = rospy.Time.now()

	i = 0
	act = ActuatorControl()
	flag1 = False
	flag2 = False

	prev_imu_data = Imu()
	prev_time = rospy.Time.now()

	prev_omega_x = 0
	prev_omega_y = 0
	prev_omega_z = 0

	prev_vx = 0
	prev_vy = 0
	prev_vz = 0
	delta_t = 0.02

	count = 0
	theta = 0.0
	x_theta = 0.0
	y_theta = 0.0
	step_size = 0.5
	prev_time = 0.0
	curr_time = 0.0		# rospy.loginfo("Outside")
	while not rospy.is_shutdown():
		if current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_request > rospy.Duration(5.0)):
			offb_set_mode_response = set_mode_client(offb_set_mode)
			if offb_set_mode_response.mode_sent:
				rospy.loginfo("Offboard enabled")
				flag1 = True

			last_request = rospy.Time.now()
		else:
			if current_state.armed == False:
				arm_cmd_response = arming_client(arm_cmd)
				if arm_cmd_response.success :
					rospy.loginfo("Vehicle armed")
					flag2 = True

				last_request = rospy.Time.now()


		# rospy.loginfo("Inside")
		curr_time = rospy.Time.now()
		if flag1 and flag2:

			x_f.append(float(local_position.pose.position.x))
			y_f.append(float(local_position.pose.position.y))
			z_f.append(float(local_position.pose.position.z))

			vx_f.append(float(local_velocity.twist.linear.x))
			vy_f.append(float(local_velocity.twist.linear.y))
			vz_f.append(float(local_velocity.twist.linear.z))

			# print(local_velocity.twist.linear.x)

			orientation = [imu_data.orientation.w,imu_data.orientation.x,imu_data.orientation.y ,imu_data.orientation.z]
			(roll,pitch, yaw) = quaternion_to_euler_angle(imu_data.orientation.w,imu_data.orientation.x,imu_data.orientation.y ,imu_data.orientation.z)
			r_f.append(float(mt.radians(roll)))
			p_f.append(float(mt.radians(pitch)))
			yaw_f.append(float(mt.radians(yaw)))

			sin_r_f.append(mt.sin(float(mt.radians(roll))))
			sin_p_f.append(mt.sin(float(mt.radians(pitch))))
			sin_y_f.append(mt.sin(float(mt.radians(yaw))))

			cos_r_f.append(mt.cos(float(mt.radians(roll))))
			cos_p_f.append(mt.cos(float(mt.radians(pitch))))
			cos_y_f.append(mt.cos(float(mt.radians(yaw))))


			rs_f.append(float(imu_data.angular_velocity.x))
			ps_f.append(float(imu_data.angular_velocity.y))
			ys_f.append(float(imu_data.angular_velocity.z))

			ix.append(float(ixx))
			iy.append(float(iyy))
			iz.append(float(izz))

			m.append(float(mass))

			u0.append(act_controls.controls[0])
			u1.append(act_controls.controls[1])
			u2.append(act_controls.controls[2])
			u3.append(act_controls.controls[3])

		
			pose.pose.position.x = x_theta
			pose.pose.position.y = 0
			pose.pose.position.z = 3

			x_des.append(pose.pose.position.x)
			y_des.append(pose.pose.position.y)
			z_des.append(pose.pose.position.z)
			sin_y_des.append(yaw_des)
			cos_y_des.append(yaw_des)

			w_mag.append(0)
			w_x.append(0)
			w_y.append(0)
			w_z.append(0)
			
			n_t = curr_time - prev_time
			#delta_t = float(n_t.nsecs) * 1e-9

			a_x.append((float(local_velocity.twist.linear.x) - prev_vx)/delta_t)
			a_y.append((float(local_velocity.twist.linear.y) - prev_vy)/delta_t)
			a_z.append((float(local_velocity.twist.linear.z) - prev_vz)/delta_t)


			prev_vx = float(local_velocity.twist.linear.x)
			prev_vy = float(local_velocity.twist.linear.y)
			prev_vz = float(local_velocity.twist.linear.z)

			aplha_x.append((float(imu_data.angular_velocity.x) - prev_omega_x)/delta_t)
			aplha_y.append((float(imu_data.angular_velocity.y) - prev_omega_y)/delta_t)
			aplha_z.append((float(imu_data.angular_velocity.z) - prev_omega_z)/delta_t)

			ax_f.append(float(imu_data.linear_acceleration.x))
			ay_f.append(float(imu_data.linear_acceleration.y))
			az_f.append(float(imu_data.linear_acceleration.z))

			prev_omega_x = float(imu_data.angular_velocity.x)
			prev_omega_y = float(imu_data.angular_velocity.y)
			prev_omega_z = float(imu_data.angular_velocity.z)

			print('Local Position :',local_position.pose.position.x , ' Des : ', pose.pose.position.x)

			x_theta = x_theta+0.01


			


			count += 1
			local_pos_pub.publish(pose)

			if(count >= data_points):
				break
		
		prev_time = curr_time
		rate.sleep()


	nn1_x_input_state = np.array([vx_f,vy_f,vz_f, rs_f,ps_f,ys_f, sin_r_f, sin_p_f,sin_y_f, cos_r_f,cos_p_f,cos_y_f, u3],ndmin=2).transpose()
	nn1_x_grd_truth = np.array([a_x,a_y,a_z],ndmin=2).transpose()

	nn2_x_input_state = np.array([vx_f,vy_f,vz_f, rs_f,ps_f,ys_f, sin_r_f, sin_p_f,sin_y_f, cos_r_f,cos_p_f,cos_y_f, u0, u1, u2],ndmin=2).transpose()
	nn2_x_grd_truth  = np.array([aplha_x,aplha_y,aplha_z],ndmin=2).transpose()


	print('nn1_x_input_state   :',nn1_x_input_state.shape)
	print('nn1_x_grd_truth   :',nn1_x_grd_truth.shape)
	print('nn2_x_input_state   :',nn2_x_input_state.shape)
	print('nn2_x_grd_truth :',nn2_x_grd_truth.shape)

	np.save('nn1_x_input_state.npy',nn1_x_input_state)
	np.save('nn1_x_grd_truth.npy',nn1_x_grd_truth)
	np.save('nn2_x_input_state.npy',nn2_x_input_state)
	np.save('nn2_x_grd_truth.npy',nn2_x_grd_truth)

	s_x = np.array([x_f, y_f, z_f,vx_f,vy_f,vz_f,sin_r_f,sin_p_f,sin_y_f,cos_r_f,cos_p_f,cos_y_f,rs_f,ps_f,ys_f,r_f,p_f,yaw_f],ndmin=2).transpose()
	u_x = np.array([u0,u1,u2,u3],ndmin=2).transpose()
	ac_x = np.array([ax_f,ay_f,az_f],ndmin=2).transpose()


	print('s_x :',s_x.shape)
	print('u_x :',u_x.shape)
	print('ac_x :',ac_x.shape)


	np.save('s_x.npy' ,s_x)
	np.save('u_x.npy' ,u_x)
	np.save('a_x.npy' ,ac_x)






if __name__ == '__main__':
	try:
		# current_state = State()
		control()
	except rospy.ROSInterruptException:
		pass
