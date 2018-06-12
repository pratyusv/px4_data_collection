execute_process(COMMAND "/home/pratyush/git/px4_data_collection/catkin_ws/build/mavros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/pratyush/git/px4_data_collection/catkin_ws/build/mavros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
