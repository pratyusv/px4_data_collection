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

# Include any dependencies generated for this target.
include src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/depend.make

# Include the progress variables for this target.
include src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/progress.make

# Include the compile flags for this target's objects.
include src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/flags.make

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/flags.make
src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o: /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/platforms/posix/drivers/accelsim/accelsim.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o -c /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/platforms/posix/drivers/accelsim/accelsim.cpp

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.i"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/platforms/posix/drivers/accelsim/accelsim.cpp > CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.i

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.s"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/platforms/posix/drivers/accelsim/accelsim.cpp -o CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.s

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.requires:

.PHONY : src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.requires

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.provides: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.requires
	$(MAKE) -f src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/build.make src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.provides.build
.PHONY : src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.provides

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.provides.build: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o


# Object files for target platforms__posix__drivers__accelsim
platforms__posix__drivers__accelsim_OBJECTS = \
"CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o"

# External object files for target platforms__posix__drivers__accelsim
platforms__posix__drivers__accelsim_EXTERNAL_OBJECTS =

src/platforms/posix/drivers/accelsim/libplatforms__posix__drivers__accelsim.a: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o
src/platforms/posix/drivers/accelsim/libplatforms__posix__drivers__accelsim.a: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/build.make
src/platforms/posix/drivers/accelsim/libplatforms__posix__drivers__accelsim.a: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libplatforms__posix__drivers__accelsim.a"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim && $(CMAKE_COMMAND) -P CMakeFiles/platforms__posix__drivers__accelsim.dir/cmake_clean_target.cmake
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/platforms__posix__drivers__accelsim.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/build: src/platforms/posix/drivers/accelsim/libplatforms__posix__drivers__accelsim.a

.PHONY : src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/build

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/requires: src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/accelsim.cpp.o.requires

.PHONY : src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/requires

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/clean:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim && $(CMAKE_COMMAND) -P CMakeFiles/platforms__posix__drivers__accelsim.dir/cmake_clean.cmake
.PHONY : src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/clean

src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/depend:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/platforms/posix/drivers/accelsim /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/platforms/posix/drivers/accelsim/CMakeFiles/platforms__posix__drivers__accelsim.dir/depend

