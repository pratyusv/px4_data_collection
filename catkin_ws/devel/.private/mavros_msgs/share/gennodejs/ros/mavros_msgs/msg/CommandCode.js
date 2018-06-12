// Auto-generated. Do not edit!

// (in-package mavros_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class CommandCode {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CommandCode
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CommandCode
    let len;
    let data = new CommandCode(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mavros_msgs/CommandCode';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5f2b024f460e58b487bc6e944e943789';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Some MAV_CMD command codes.
    # Actual meaning and params you may find in MAVLink documentation
    # http://mavlink.org/messages/common#ENUM_MAV_CMD
    
    # some common MAV_CMD
    uint16 CMD_DO_SET_MODE = 176
    uint16 CMD_DO_JUMP = 177
    uint16 CMD_DO_CHANGE_SPEED = 178
    uint16 CMD_DO_SET_HOME = 179
    uint16 CMD_DO_SET_RELAY = 181
    uint16 CMD_DO_REPEAT_RELAY = 182
    uint16 CMD_DO_SET_SERVO = 183
    uint16 CMD_DO_REPEAT_SERVO = 184
    uint16 CMD_DO_CONTROL_VIDEO = 200
    uint16 CMD_DO_SET_ROI = 201
    uint16 CMD_DO_MOUNT_CONTROL = 205
    uint16 CMD_DO_SET_CAM_TRIGG_DIST = 206
    uint16 CMD_DO_FENCE_ENABLE = 207
    uint16 CMD_DO_PARACHUTE = 208
    uint16 CMD_DO_INVERTED_FLIGHT = 210
    uint16 CMD_DO_MOUNT_CONTROL_QUAT = 220
    uint16 CMD_PREFLIGHT_CALIBRATION = 241
    uint16 CMD_MISSION_START = 300
    uint16 CMD_COMPONENT_ARM_DISARM = 400
    uint16 CMD_GET_HOME_POSITION = 410
    uint16 CMD_START_RX_PAIR = 500
    uint16 CMD_REQUEST_AUTOPILOT_CAPABILITIES = 520
    uint16 CMD_DO_TRIGGER_CONTROL = 2003
    
    # Waypoint related commands
    uint16 NAV_WAYPOINT = 16
    uint16 NAV_LOITER_UNLIM = 17
    uint16 NAV_LOITER_TURNS = 18
    uint16 NAV_LOITER_TIME = 19
    uint16 NAV_RETURN_TO_LAUNCH = 20
    uint16 NAV_LAND = 21
    uint16 NAV_TAKEOFF = 22
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CommandCode(null);
    return resolved;
    }
};

// Constants for message
CommandCode.Constants = {
  CMD_DO_SET_MODE: 176,
  CMD_DO_JUMP: 177,
  CMD_DO_CHANGE_SPEED: 178,
  CMD_DO_SET_HOME: 179,
  CMD_DO_SET_RELAY: 181,
  CMD_DO_REPEAT_RELAY: 182,
  CMD_DO_SET_SERVO: 183,
  CMD_DO_REPEAT_SERVO: 184,
  CMD_DO_CONTROL_VIDEO: 200,
  CMD_DO_SET_ROI: 201,
  CMD_DO_MOUNT_CONTROL: 205,
  CMD_DO_SET_CAM_TRIGG_DIST: 206,
  CMD_DO_FENCE_ENABLE: 207,
  CMD_DO_PARACHUTE: 208,
  CMD_DO_INVERTED_FLIGHT: 210,
  CMD_DO_MOUNT_CONTROL_QUAT: 220,
  CMD_PREFLIGHT_CALIBRATION: 241,
  CMD_MISSION_START: 300,
  CMD_COMPONENT_ARM_DISARM: 400,
  CMD_GET_HOME_POSITION: 410,
  CMD_START_RX_PAIR: 500,
  CMD_REQUEST_AUTOPILOT_CAPABILITIES: 520,
  CMD_DO_TRIGGER_CONTROL: 2003,
  NAV_WAYPOINT: 16,
  NAV_LOITER_UNLIM: 17,
  NAV_LOITER_TURNS: 18,
  NAV_LOITER_TIME: 19,
  NAV_RETURN_TO_LAUNCH: 20,
  NAV_LAND: 21,
  NAV_TAKEOFF: 22,
}

module.exports = CommandCode;
