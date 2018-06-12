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

# Include any dependencies generated for this target.
include src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/depend.make

# Include the progress variables for this target.
include src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/progress.make

# Include the compile flags for this target's objects.
include src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/flags.make

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/flags.make
src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o: /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/src/modules/mc_att_control/tailsitter_recovery/tailsitter_recovery.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pratyush/git/px4_data_collection/catkin_ws/build/px4/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o"
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o -c /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/src/modules/mc_att_control/tailsitter_recovery/tailsitter_recovery.cpp

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.i"
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/src/modules/mc_att_control/tailsitter_recovery/tailsitter_recovery.cpp > CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.i

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.s"
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/src/modules/mc_att_control/tailsitter_recovery/tailsitter_recovery.cpp -o CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.s

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.requires:

.PHONY : src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.requires

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.provides: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.requires
	$(MAKE) -f src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/build.make src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.provides.build
.PHONY : src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.provides

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.provides.build: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o


# Object files for target tailsitter_recovery
tailsitter_recovery_OBJECTS = \
"CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o"

# External object files for target tailsitter_recovery
tailsitter_recovery_EXTERNAL_OBJECTS =

/home/pratyush/git/px4_data_collection/catkin_ws/devel/.private/px4/lib/libtailsitter_recovery.a: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o
/home/pratyush/git/px4_data_collection/catkin_ws/devel/.private/px4/lib/libtailsitter_recovery.a: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/build.make
/home/pratyush/git/px4_data_collection/catkin_ws/devel/.private/px4/lib/libtailsitter_recovery.a: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pratyush/git/px4_data_collection/catkin_ws/build/px4/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library /home/pratyush/git/px4_data_collection/catkin_ws/devel/.private/px4/lib/libtailsitter_recovery.a"
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery && $(CMAKE_COMMAND) -P CMakeFiles/tailsitter_recovery.dir/cmake_clean_target.cmake
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tailsitter_recovery.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/build: /home/pratyush/git/px4_data_collection/catkin_ws/devel/.private/px4/lib/libtailsitter_recovery.a

.PHONY : src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/build

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/requires: src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/tailsitter_recovery.cpp.o.requires

.PHONY : src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/requires

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/clean:
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery && $(CMAKE_COMMAND) -P CMakeFiles/tailsitter_recovery.dir/cmake_clean.cmake
.PHONY : src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/clean

src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/depend:
	cd /home/pratyush/git/px4_data_collection/catkin_ws/build/px4 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware /home/pratyush/git/px4_data_collection/catkin_ws/src/Firmware/src/modules/mc_att_control/tailsitter_recovery /home/pratyush/git/px4_data_collection/catkin_ws/build/px4 /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery /home/pratyush/git/px4_data_collection/catkin_ws/build/px4/src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/modules/mc_att_control/tailsitter_recovery/CMakeFiles/tailsitter_recovery.dir/depend

