#/bin/bash

PX4_DIR="./Firmware/"
ROS_NODE_DIR="./offb_pkg/src/next_state/scripts/"

cd ${ROS_NODE_DIR}
list=$(ls *.py)
cd - > /dev/null

c=0
for i in ${list}; do
	cd ${PX4_DIR}
	xterm -e "make posix_sitl_default gazebo" &
	cd - > /dev/null

	sleep 15s

	echo "********** ${i}"
	cd ${ROS_NODE_DIR}
	./${i} 30000 &> /dev/null
	# ./${i} 50000
	echo "********** ${i} completed"
	kill -9 $(pgrep xterm)
	kill -9 $(pgrep make)
	sleep 5s
	cd - > /dev/null

	# c=$((c+1))
	# if ((c==2)); then
	# 	break;
	# fi
done
