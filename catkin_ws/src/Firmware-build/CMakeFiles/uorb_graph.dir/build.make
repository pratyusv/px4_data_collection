# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build

# Utility rule file for uorb_graph.

# Include the progress variables for this target.
include CMakeFiles/uorb_graph.dir/progress.make

CMakeFiles/uorb_graph: sitl


sitl:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating uORB graph"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware && /usr/bin/python /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/Tools/uorb_graph/create.py --exclude-path src/examples --file /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/Tools/uorb_graph/graph_sitl

uorb_graph: CMakeFiles/uorb_graph
uorb_graph: sitl
uorb_graph: CMakeFiles/uorb_graph.dir/build.make

.PHONY : uorb_graph

# Rule to build all files generated by this target.
CMakeFiles/uorb_graph.dir/build: uorb_graph

.PHONY : CMakeFiles/uorb_graph.dir/build

CMakeFiles/uorb_graph.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/uorb_graph.dir/cmake_clean.cmake
.PHONY : CMakeFiles/uorb_graph.dir/clean

CMakeFiles/uorb_graph.dir/depend:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles/uorb_graph.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/uorb_graph.dir/depend

