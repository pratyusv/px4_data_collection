# Data Set for Training

This repository contains code to collect the data set for training.

### Workspace

The workspace is created by using `catkin_tools`.

The workspace has following packages :
1. **px4 autpilot** : `v1.7.3` works with catkin_tools. After `v1.7.3` there are errors in building with `catkin_tools`

2. **mavros** : The mavros package is the link between ros msgs and the `mavlink`.

3. **mavlink** : The mavlink package

### Installation

#### mavros
```
$ sudo apt-get install ros-indigo-mavros ros-indigo-mavros-extras
```

#### mavlink
Mavlink is already present inside `/opt/ros/kinetic/share`. As we need to customize the mavlink, it is better to install inside our workspace.

```
$ sudo apt-get install python-wstool python-rosinstall-generator python-catkin-tools
$ wstool init ~/catkin_ws/src
$ rosinstall_generator --upstream mavros | tee /tmp/mavros.rosinstall
$ rosinstall_generator --upstream-development mavros | tee /tmp/mavros.rosinstall
$ rosinstall_generator mavlink | tee -a /tmp/mavros.rosinstall
$ wstool merge -t src /tmp/mavros.rosinstall
$ wstool update -t src
$ rosdep install --from-paths src --ignore-src --rosdistro `echo $ROS_DISTRO` -y
$ catkin build
```


-------------
## Create custom mavros receiver and sender

The aim is to record the control signals send by px4 to the ESC, using ROS node.

1. Create `act_control.cpp` in the path `px4_data_collection/catkin_ws/mavros/mavros_extras/src/plugins`.
This is the reciever node that records the control parameters.

2. Edit `mavros_plugins.xml` inside [catkin_ws/src/mavros/mavros_extras/mavros_plugins.xml](catkin_ws/src/mavros/mavros_extras/mavros_plugins.xml)

add:

```
<class name="act_control" type="mavros::extra_plugins::ActControlPlugin" base_class_type="mavros::plugin::PluginBase">
  <description>Send actuator controls to FCU.</description>
</class>
```

3. Edit `CMakeList.txt` inside [catkin_ws/src/mavros/mavros_extras/CMakeLists.txt](catkin_ws/src/mavros/mavros_extras/CMakeLists.txt)

add :

```
add_library(
...
src/plugins/act_control.cpp
...
)
```

4. Edit `common.xml` inside [catkin_ws/src/mavlink/message_definitions/v1.0/common.xml](catkin_ws/src/mavlink/message_definitions/v1.0/common.xml)

add :

```
<message id="229" name="LQR_CONTROLS">
  <description> Send controls generated from off board cobntroller to on board PD controller</description>
  <field type="float" name="roll_moment">actuator controls</field>
  <field type="float" name="pitch_moment">actuator controls</field>
  <field type="float" name="yaw_moment">actuator controls</field>
  <field type="float" name="thrust_moment">actuator controls</field>
  <field type="float" name="roll_angle">actuator controls</field>
  <field type="float" name="pitch_angle">actuator controls</field>
  <field type="float" name="yaw_angle">actuator controls</field>
</message>
```
---------
#### Inside px4

1. Edit `common.xml` inside [catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/message_definitions/common.xml](catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/message_definitions/common.xml)

add:

```
<message id="229" name="LQR_CONTROLS">
  <description> Send controls generated from off board cobntroller to on board PD controller</description>
  <field type="float" name="roll_moment">actuator controls</field>
  <field type="float" name="pitch_moment">actuator controls</field>
  <field type="float" name="yaw_moment">actuator controls</field>
  <field type="float" name="thrust_moment">actuator controls</field>
  <field type="float" name="roll_angle">actuator controls</field>
  <field type="float" name="pitch_angle">actuator controls</field>
  <field type="float" name="yaw_angle">actuator controls</field>
</message>
```

2. Remove `common` and `standard` directories from [catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/common](catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/common) and [catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/standard](catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/standard)

3. Generate `standard` and `common` directories using `mavlink-generator` located in [catkin_ws/src/mavlink/pymavlink](catkin_ws/src/mavlink/pymavlink)

> $ python mavgenerate.py
>

```
At XML, "Browse" to [catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0/message_definitions/common.xml].
At Out, "Browse" to [catkin_ws/src/Firmware/mavlink/include/mavlink/v2.0].
Select Language "C"
Select Protocol "2.0"
Check Validate
```

4. Make uOrb message [catkin_ws/src/Firmware/msg/lqr_controls.msg](catkin_ws/src/Firmware/msg/lqr_controls.msg)

```
float32 roll_moment
float32 pitch_moment
float32 yaw_moment
float32 thrust_moment
float32 roll_angle
float32 pitch_angle
float32 yaw_angle
```

5. Edit `CMakeList.txt` inside [catkin_ws/src/Firmware/msg/CMakeLists.txt](catkin_ws/src/Firmware/msg/CMakeLists.txt)
```
set(
...
     lqr_controls.msg
     )
```

6. Edit `mavlink_receiver.h` located at [catkin_ws/src/Firmware/src/modules/mavlink/mavlink_receiver.h](catkin_ws/src/Firmware/src/modules/mavlink/mavlink_receiver.h)

```
#include <uORB/topics/lqr_controls.h>
.....
class MavlinkReceiver
{
void handle_message_att_pos_mocap(mavlink_message_t *msg);
void handle_message_lqr_controls(mavlink_message_t *msg);
......
orb_advert_t _att_pos_mocap_pub;
orb_advert_t _lqr_controls_pub;
}
```

7. Edit `mavlink_receiver.cpp` located at
[catkin_ws/src/Firmware/src/modules/mavlink/mavlink_receiver.cpp](catkin_ws/src/Firmware/src/modules/mavlink/mavlink_receiver.cpp)

```
MavlinkReceiver::MavlinkReceiver(Mavlink *parent) :
....
_att_pos_mocap_pub(nullptr),
_lqr_controls_pub(nullptr),
....


MavlinkReceiver::handle_message(mavlink_message_t *msg)
{
  switch (msg->msgid) {

		case MAVLINK_MSG_ID_LQR_CONTROLS:
        handle_message_lqr_controls(msg);
        break;
        ....
}
```

add function

```
void
MavlinkReceiver::handle_message_lqr_controls(mavlink_message_t *msg)
{
    mavlink_lqr_controls_t man;
    mavlink_msg_lqr_controls_decode(msg, &man);


    struct lqr_controls_s key = {};

    key.timestamp = hrt_absolute_time();
    key.roll_moment = man.roll_moment;
		key.pitch_moment = man.pitch_moment;
		key.yaw_moment = man.yaw_moment;
		key.thrust_moment = man.thrust_moment;

		key.roll_angle = man.roll_angle;
		key.pitch_angle = man.pitch_angle;
		key.yaw_angle = man.yaw_angle;

    if (_lqr_controls_pub == nullptr) {
        _lqr_controls_pub = orb_advertise(ORB_ID(lqr_controls), &key);

    } else {
        orb_publish(ORB_ID(lqr_controls), _lqr_controls_pub, &key);
    }
  ```

8. To change the rates at which the mavros should publish data, edit `mavlink_main.cpp` at
[catkin_ws/src/Firmware/src/modules/mavlink/mavlink_main.h](catkin_ws/src/Firmware/src/modules/mavlink/mavlink_main.h)

```
case MAVLINK_MODE_ONBOARD:
  configure_stream("SYS_STATUS", 5.0f);
  configure_stream("EXTENDED_SYS_STATE", 5.0f);
  configure_stream("HIGHRES_IMU", 50.0f);
  configure_stream("ATTITUDE", 50.0f); /* 100 to 50 */
  configure_stream("ATTITUDE_QUATERNION", 50.0f);
  configure_stream("RC_CHANNELS", 20.0f);
  configure_stream("SERVO_OUTPUT_RAW_0", 10.0f);
  configure_stream("ALTITUDE", 10.0f);
  configure_stream("GPS_RAW_INT");
  configure_stream("ADSB_VEHICLE");
  configure_stream("COLLISION");
  configure_stream("DISTANCE_SENSOR", 10.0f);
  configure_stream("OPTICAL_FLOW_RAD", 10.0f);
  configure_stream("VISION_POSITION_ESTIMATE", 10.0f);
  configure_stream("ESTIMATOR_STATUS", 1.0f);
  configure_stream("NAV_CONTROLLER_OUTPUT", 10.0f);
  configure_stream("GLOBAL_POSITION_INT", 50.0f);
  configure_stream("LOCAL_POSITION_NED", 50.0f); /* 30 to 50 */
  configure_stream("POSITION_TARGET_GLOBAL_INT", 10.0f);
  configure_stream("ATTITUDE_TARGET", 10.0f);
  configure_stream("HOME_POSITION", 0.5f);
  configure_stream("NAMED_VALUE_FLOAT", 10.0f);
  configure_stream("DEBUG", 10.0f);
  configure_stream("DEBUG_VECT", 10.0f);
  configure_stream("VFR_HUD", 10.0f);
  configure_stream("WIND_COV", 10.0f);
  configure_stream("POSITION_TARGET_LOCAL_NED", 10.0f);
  configure_stream("SYSTEM_TIME", 1.0f);
  configure_stream("TIMESYNC", 10.0f);
  configure_stream("CAMERA_CAPTURE", 2.0f);
  configure_stream("CAMERA_TRIGGER");
  configure_stream("CAMERA_IMAGE_CAPTURED");
  configure_stream("ACTUATOR_CONTROL_TARGET0", 50.0f); /* 10 to 50 */
  break;
  ```
