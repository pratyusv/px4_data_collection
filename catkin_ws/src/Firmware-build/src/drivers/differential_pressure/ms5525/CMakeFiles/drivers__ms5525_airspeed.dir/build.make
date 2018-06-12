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
include src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/depend.make

# Include the progress variables for this target.
include src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/progress.make

# Include the compile flags for this target's objects.
include src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/flags.make

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/flags.make
src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o: /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o -c /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525.cpp

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.i"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525.cpp > CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.i

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.s"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525.cpp -o CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.s

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.requires:

.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.requires

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.provides: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.requires
	$(MAKE) -f src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/build.make src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.provides.build
.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.provides

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.provides.build: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o


src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/flags.make
src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o: /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525_main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o -c /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525_main.cpp

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.i"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525_main.cpp > CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.i

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.s"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525/MS5525_main.cpp -o CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.s

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.requires:

.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.requires

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.provides: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.requires
	$(MAKE) -f src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/build.make src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.provides.build
.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.provides

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.provides.build: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o


# Object files for target drivers__ms5525_airspeed
drivers__ms5525_airspeed_OBJECTS = \
"CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o" \
"CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o"

# External object files for target drivers__ms5525_airspeed
drivers__ms5525_airspeed_EXTERNAL_OBJECTS =

src/drivers/differential_pressure/ms5525/libdrivers__ms5525_airspeed.a: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o
src/drivers/differential_pressure/ms5525/libdrivers__ms5525_airspeed.a: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o
src/drivers/differential_pressure/ms5525/libdrivers__ms5525_airspeed.a: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/build.make
src/drivers/differential_pressure/ms5525/libdrivers__ms5525_airspeed.a: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libdrivers__ms5525_airspeed.a"
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && $(CMAKE_COMMAND) -P CMakeFiles/drivers__ms5525_airspeed.dir/cmake_clean_target.cmake
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/drivers__ms5525_airspeed.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/build: src/drivers/differential_pressure/ms5525/libdrivers__ms5525_airspeed.a

.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/build

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/requires: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525.cpp.o.requires
src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/requires: src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/MS5525_main.cpp.o.requires

.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/requires

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/clean:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 && $(CMAKE_COMMAND) -P CMakeFiles/drivers__ms5525_airspeed.dir/cmake_clean.cmake
.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/clean

src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/depend:
	cd /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware/src/drivers/differential_pressure/ms5525 /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525 /home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/Firmware-build/src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/drivers/differential_pressure/ms5525/CMakeFiles/drivers__ms5525_airspeed.dir/depend

