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

# Utility rule file for none_tailsitter_valgrind.

# Include the progress variables for this target.
include platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/progress.make

platforms/posix/CMakeFiles/none_tailsitter_valgrind:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/tmp && /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/Tools/sitl_run.sh /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/px4 posix-configs/SITL/init/ekf2 valgrind none tailsitter /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build

none_tailsitter_valgrind: platforms/posix/CMakeFiles/none_tailsitter_valgrind
none_tailsitter_valgrind: platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/build.make

.PHONY : none_tailsitter_valgrind

# Rule to build all files generated by this target.
platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/build: none_tailsitter_valgrind

.PHONY : platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/build

platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/clean:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/platforms/posix && $(CMAKE_COMMAND) -P CMakeFiles/none_tailsitter_valgrind.dir/cmake_clean.cmake
.PHONY : platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/clean

platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/depend:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/platforms/posix /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/platforms/posix /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : platforms/posix/CMakeFiles/none_tailsitter_valgrind.dir/depend

