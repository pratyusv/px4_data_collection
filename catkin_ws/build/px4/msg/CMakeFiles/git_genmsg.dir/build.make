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
CMAKE_SOURCE_DIR = /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pratyush/git/px4_data_collection/catkin_ws/build/px4

# Utility rule file for git_genmsg.

# Include the progress variables for this target.
include msg/CMakeFiles/git_genmsg.dir/progress.make

msg/CMakeFiles/git_genmsg: msg/git_init_tools_genmsg.stamp


msg/git_init_tools_genmsg.stamp: /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/.gitmodules
msg/git_init_tools_genmsg.stamp: /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/msg/tools/genmsg/.git
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/pratyush/git/px4_data_collection/catkin_ws/build/px4/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "git submodule tools/genmsg"
	cd /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/msg && bash /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/Tools/check_submodules.sh tools/genmsg
	cd /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/msg && cmake -E touch /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/msg/git_init_tools_genmsg.stamp

git_genmsg: msg/CMakeFiles/git_genmsg
git_genmsg: msg/git_init_tools_genmsg.stamp
git_genmsg: msg/CMakeFiles/git_genmsg.dir/build.make

.PHONY : git_genmsg

# Rule to build all files generated by this target.
msg/CMakeFiles/git_genmsg.dir/build: git_genmsg

.PHONY : msg/CMakeFiles/git_genmsg.dir/build

msg/CMakeFiles/git_genmsg.dir/clean:
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/msg && $(CMAKE_COMMAND) -P CMakeFiles/git_genmsg.dir/cmake_clean.cmake
.PHONY : msg/CMakeFiles/git_genmsg.dir/clean

msg/CMakeFiles/git_genmsg.dir/depend:
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/msg /home/pratyush/git/px4_data_collection/catkin_ws/build/px4 /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/msg /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/msg/CMakeFiles/git_genmsg.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : msg/CMakeFiles/git_genmsg.dir/depend

