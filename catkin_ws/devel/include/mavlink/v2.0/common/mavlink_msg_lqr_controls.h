#pragma once
// MESSAGE LQR_CONTROLS PACKING

#define MAVLINK_MSG_ID_LQR_CONTROLS 229

MAVPACKED(
typedef struct __mavlink_lqr_controls_t {
 float roll_moment; /*< actuator controls*/
 float pitch_moment; /*< actuator controls*/
 float yaw_moment; /*< actuator controls*/
 float thrust_moment; /*< actuator controls*/
 float roll_angle; /*< actuator controls*/
 float pitch_angle; /*< actuator controls*/
 float yaw_angle; /*< actuator controls*/
}) mavlink_lqr_controls_t;

#define MAVLINK_MSG_ID_LQR_CONTROLS_LEN 28
#define MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN 28
#define MAVLINK_MSG_ID_229_LEN 28
#define MAVLINK_MSG_ID_229_MIN_LEN 28

#define MAVLINK_MSG_ID_LQR_CONTROLS_CRC 13
#define MAVLINK_MSG_ID_229_CRC 13



#if MAVLINK_COMMAND_24BIT
#define MAVLINK_MESSAGE_INFO_LQR_CONTROLS { \
    229, \
    "LQR_CONTROLS", \
    7, \
    {  { "roll_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 0, offsetof(mavlink_lqr_controls_t, roll_moment) }, \
         { "pitch_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 4, offsetof(mavlink_lqr_controls_t, pitch_moment) }, \
         { "yaw_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 8, offsetof(mavlink_lqr_controls_t, yaw_moment) }, \
         { "thrust_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 12, offsetof(mavlink_lqr_controls_t, thrust_moment) }, \
         { "roll_angle", NULL, MAVLINK_TYPE_FLOAT, 0, 16, offsetof(mavlink_lqr_controls_t, roll_angle) }, \
         { "pitch_angle", NULL, MAVLINK_TYPE_FLOAT, 0, 20, offsetof(mavlink_lqr_controls_t, pitch_angle) }, \
         { "yaw_angle", NULL, MAVLINK_TYPE_FLOAT, 0, 24, offsetof(mavlink_lqr_controls_t, yaw_angle) }, \
         } \
}
#else
#define MAVLINK_MESSAGE_INFO_LQR_CONTROLS { \
    "LQR_CONTROLS", \
    7, \
    {  { "roll_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 0, offsetof(mavlink_lqr_controls_t, roll_moment) }, \
         { "pitch_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 4, offsetof(mavlink_lqr_controls_t, pitch_moment) }, \
         { "yaw_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 8, offsetof(mavlink_lqr_controls_t, yaw_moment) }, \
         { "thrust_moment", NULL, MAVLINK_TYPE_FLOAT, 0, 12, offsetof(mavlink_lqr_controls_t, thrust_moment) }, \
         { "roll_angle", NULL, MAVLINK_TYPE_FLOAT, 0, 16, offsetof(mavlink_lqr_controls_t, roll_angle) }, \
         { "pitch_angle", NULL, MAVLINK_TYPE_FLOAT, 0, 20, offsetof(mavlink_lqr_controls_t, pitch_angle) }, \
         { "yaw_angle", NULL, MAVLINK_TYPE_FLOAT, 0, 24, offsetof(mavlink_lqr_controls_t, yaw_angle) }, \
         } \
}
#endif

/**
 * @brief Pack a lqr_controls message
 * @param system_id ID of this system
 * @param component_id ID of this component (e.g. 200 for IMU)
 * @param msg The MAVLink message to compress the data into
 *
 * @param roll_moment actuator controls
 * @param pitch_moment actuator controls
 * @param yaw_moment actuator controls
 * @param thrust_moment actuator controls
 * @param roll_angle actuator controls
 * @param pitch_angle actuator controls
 * @param yaw_angle actuator controls
 * @return length of the message in bytes (excluding serial stream start sign)
 */
static inline uint16_t mavlink_msg_lqr_controls_pack(uint8_t system_id, uint8_t component_id, mavlink_message_t* msg,
                               float roll_moment, float pitch_moment, float yaw_moment, float thrust_moment, float roll_angle, float pitch_angle, float yaw_angle)
{
#if MAVLINK_NEED_BYTE_SWAP || !MAVLINK_ALIGNED_FIELDS
    char buf[MAVLINK_MSG_ID_LQR_CONTROLS_LEN];
    _mav_put_float(buf, 0, roll_moment);
    _mav_put_float(buf, 4, pitch_moment);
    _mav_put_float(buf, 8, yaw_moment);
    _mav_put_float(buf, 12, thrust_moment);
    _mav_put_float(buf, 16, roll_angle);
    _mav_put_float(buf, 20, pitch_angle);
    _mav_put_float(buf, 24, yaw_angle);

        memcpy(_MAV_PAYLOAD_NON_CONST(msg), buf, MAVLINK_MSG_ID_LQR_CONTROLS_LEN);
#else
    mavlink_lqr_controls_t packet;
    packet.roll_moment = roll_moment;
    packet.pitch_moment = pitch_moment;
    packet.yaw_moment = yaw_moment;
    packet.thrust_moment = thrust_moment;
    packet.roll_angle = roll_angle;
    packet.pitch_angle = pitch_angle;
    packet.yaw_angle = yaw_angle;

        memcpy(_MAV_PAYLOAD_NON_CONST(msg), &packet, MAVLINK_MSG_ID_LQR_CONTROLS_LEN);
#endif

    msg->msgid = MAVLINK_MSG_ID_LQR_CONTROLS;
    return mavlink_finalize_message(msg, system_id, component_id, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
}

/**
 * @brief Pack a lqr_controls message on a channel
 * @param system_id ID of this system
 * @param component_id ID of this component (e.g. 200 for IMU)
 * @param chan The MAVLink channel this message will be sent over
 * @param msg The MAVLink message to compress the data into
 * @param roll_moment actuator controls
 * @param pitch_moment actuator controls
 * @param yaw_moment actuator controls
 * @param thrust_moment actuator controls
 * @param roll_angle actuator controls
 * @param pitch_angle actuator controls
 * @param yaw_angle actuator controls
 * @return length of the message in bytes (excluding serial stream start sign)
 */
static inline uint16_t mavlink_msg_lqr_controls_pack_chan(uint8_t system_id, uint8_t component_id, uint8_t chan,
                               mavlink_message_t* msg,
                                   float roll_moment,float pitch_moment,float yaw_moment,float thrust_moment,float roll_angle,float pitch_angle,float yaw_angle)
{
#if MAVLINK_NEED_BYTE_SWAP || !MAVLINK_ALIGNED_FIELDS
    char buf[MAVLINK_MSG_ID_LQR_CONTROLS_LEN];
    _mav_put_float(buf, 0, roll_moment);
    _mav_put_float(buf, 4, pitch_moment);
    _mav_put_float(buf, 8, yaw_moment);
    _mav_put_float(buf, 12, thrust_moment);
    _mav_put_float(buf, 16, roll_angle);
    _mav_put_float(buf, 20, pitch_angle);
    _mav_put_float(buf, 24, yaw_angle);

        memcpy(_MAV_PAYLOAD_NON_CONST(msg), buf, MAVLINK_MSG_ID_LQR_CONTROLS_LEN);
#else
    mavlink_lqr_controls_t packet;
    packet.roll_moment = roll_moment;
    packet.pitch_moment = pitch_moment;
    packet.yaw_moment = yaw_moment;
    packet.thrust_moment = thrust_moment;
    packet.roll_angle = roll_angle;
    packet.pitch_angle = pitch_angle;
    packet.yaw_angle = yaw_angle;

        memcpy(_MAV_PAYLOAD_NON_CONST(msg), &packet, MAVLINK_MSG_ID_LQR_CONTROLS_LEN);
#endif

    msg->msgid = MAVLINK_MSG_ID_LQR_CONTROLS;
    return mavlink_finalize_message_chan(msg, system_id, component_id, chan, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
}

/**
 * @brief Encode a lqr_controls struct
 *
 * @param system_id ID of this system
 * @param component_id ID of this component (e.g. 200 for IMU)
 * @param msg The MAVLink message to compress the data into
 * @param lqr_controls C-struct to read the message contents from
 */
static inline uint16_t mavlink_msg_lqr_controls_encode(uint8_t system_id, uint8_t component_id, mavlink_message_t* msg, const mavlink_lqr_controls_t* lqr_controls)
{
    return mavlink_msg_lqr_controls_pack(system_id, component_id, msg, lqr_controls->roll_moment, lqr_controls->pitch_moment, lqr_controls->yaw_moment, lqr_controls->thrust_moment, lqr_controls->roll_angle, lqr_controls->pitch_angle, lqr_controls->yaw_angle);
}

/**
 * @brief Encode a lqr_controls struct on a channel
 *
 * @param system_id ID of this system
 * @param component_id ID of this component (e.g. 200 for IMU)
 * @param chan The MAVLink channel this message will be sent over
 * @param msg The MAVLink message to compress the data into
 * @param lqr_controls C-struct to read the message contents from
 */
static inline uint16_t mavlink_msg_lqr_controls_encode_chan(uint8_t system_id, uint8_t component_id, uint8_t chan, mavlink_message_t* msg, const mavlink_lqr_controls_t* lqr_controls)
{
    return mavlink_msg_lqr_controls_pack_chan(system_id, component_id, chan, msg, lqr_controls->roll_moment, lqr_controls->pitch_moment, lqr_controls->yaw_moment, lqr_controls->thrust_moment, lqr_controls->roll_angle, lqr_controls->pitch_angle, lqr_controls->yaw_angle);
}

/**
 * @brief Send a lqr_controls message
 * @param chan MAVLink channel to send the message
 *
 * @param roll_moment actuator controls
 * @param pitch_moment actuator controls
 * @param yaw_moment actuator controls
 * @param thrust_moment actuator controls
 * @param roll_angle actuator controls
 * @param pitch_angle actuator controls
 * @param yaw_angle actuator controls
 */
#ifdef MAVLINK_USE_CONVENIENCE_FUNCTIONS

static inline void mavlink_msg_lqr_controls_send(mavlink_channel_t chan, float roll_moment, float pitch_moment, float yaw_moment, float thrust_moment, float roll_angle, float pitch_angle, float yaw_angle)
{
#if MAVLINK_NEED_BYTE_SWAP || !MAVLINK_ALIGNED_FIELDS
    char buf[MAVLINK_MSG_ID_LQR_CONTROLS_LEN];
    _mav_put_float(buf, 0, roll_moment);
    _mav_put_float(buf, 4, pitch_moment);
    _mav_put_float(buf, 8, yaw_moment);
    _mav_put_float(buf, 12, thrust_moment);
    _mav_put_float(buf, 16, roll_angle);
    _mav_put_float(buf, 20, pitch_angle);
    _mav_put_float(buf, 24, yaw_angle);

    _mav_finalize_message_chan_send(chan, MAVLINK_MSG_ID_LQR_CONTROLS, buf, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
#else
    mavlink_lqr_controls_t packet;
    packet.roll_moment = roll_moment;
    packet.pitch_moment = pitch_moment;
    packet.yaw_moment = yaw_moment;
    packet.thrust_moment = thrust_moment;
    packet.roll_angle = roll_angle;
    packet.pitch_angle = pitch_angle;
    packet.yaw_angle = yaw_angle;

    _mav_finalize_message_chan_send(chan, MAVLINK_MSG_ID_LQR_CONTROLS, (const char *)&packet, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
#endif
}

/**
 * @brief Send a lqr_controls message
 * @param chan MAVLink channel to send the message
 * @param struct The MAVLink struct to serialize
 */
static inline void mavlink_msg_lqr_controls_send_struct(mavlink_channel_t chan, const mavlink_lqr_controls_t* lqr_controls)
{
#if MAVLINK_NEED_BYTE_SWAP || !MAVLINK_ALIGNED_FIELDS
    mavlink_msg_lqr_controls_send(chan, lqr_controls->roll_moment, lqr_controls->pitch_moment, lqr_controls->yaw_moment, lqr_controls->thrust_moment, lqr_controls->roll_angle, lqr_controls->pitch_angle, lqr_controls->yaw_angle);
#else
    _mav_finalize_message_chan_send(chan, MAVLINK_MSG_ID_LQR_CONTROLS, (const char *)lqr_controls, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
#endif
}

#if MAVLINK_MSG_ID_LQR_CONTROLS_LEN <= MAVLINK_MAX_PAYLOAD_LEN
/*
  This varient of _send() can be used to save stack space by re-using
  memory from the receive buffer.  The caller provides a
  mavlink_message_t which is the size of a full mavlink message. This
  is usually the receive buffer for the channel, and allows a reply to an
  incoming message with minimum stack space usage.
 */
static inline void mavlink_msg_lqr_controls_send_buf(mavlink_message_t *msgbuf, mavlink_channel_t chan,  float roll_moment, float pitch_moment, float yaw_moment, float thrust_moment, float roll_angle, float pitch_angle, float yaw_angle)
{
#if MAVLINK_NEED_BYTE_SWAP || !MAVLINK_ALIGNED_FIELDS
    char *buf = (char *)msgbuf;
    _mav_put_float(buf, 0, roll_moment);
    _mav_put_float(buf, 4, pitch_moment);
    _mav_put_float(buf, 8, yaw_moment);
    _mav_put_float(buf, 12, thrust_moment);
    _mav_put_float(buf, 16, roll_angle);
    _mav_put_float(buf, 20, pitch_angle);
    _mav_put_float(buf, 24, yaw_angle);

    _mav_finalize_message_chan_send(chan, MAVLINK_MSG_ID_LQR_CONTROLS, buf, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
#else
    mavlink_lqr_controls_t *packet = (mavlink_lqr_controls_t *)msgbuf;
    packet->roll_moment = roll_moment;
    packet->pitch_moment = pitch_moment;
    packet->yaw_moment = yaw_moment;
    packet->thrust_moment = thrust_moment;
    packet->roll_angle = roll_angle;
    packet->pitch_angle = pitch_angle;
    packet->yaw_angle = yaw_angle;

    _mav_finalize_message_chan_send(chan, MAVLINK_MSG_ID_LQR_CONTROLS, (const char *)packet, MAVLINK_MSG_ID_LQR_CONTROLS_MIN_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_LEN, MAVLINK_MSG_ID_LQR_CONTROLS_CRC);
#endif
}
#endif

#endif

// MESSAGE LQR_CONTROLS UNPACKING


/**
 * @brief Get field roll_moment from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_roll_moment(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  0);
}

/**
 * @brief Get field pitch_moment from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_pitch_moment(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  4);
}

/**
 * @brief Get field yaw_moment from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_yaw_moment(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  8);
}

/**
 * @brief Get field thrust_moment from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_thrust_moment(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  12);
}

/**
 * @brief Get field roll_angle from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_roll_angle(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  16);
}

/**
 * @brief Get field pitch_angle from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_pitch_angle(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  20);
}

/**
 * @brief Get field yaw_angle from lqr_controls message
 *
 * @return actuator controls
 */
static inline float mavlink_msg_lqr_controls_get_yaw_angle(const mavlink_message_t* msg)
{
    return _MAV_RETURN_float(msg,  24);
}

/**
 * @brief Decode a lqr_controls message into a struct
 *
 * @param msg The message to decode
 * @param lqr_controls C-struct to decode the message contents into
 */
static inline void mavlink_msg_lqr_controls_decode(const mavlink_message_t* msg, mavlink_lqr_controls_t* lqr_controls)
{
#if MAVLINK_NEED_BYTE_SWAP || !MAVLINK_ALIGNED_FIELDS
    lqr_controls->roll_moment = mavlink_msg_lqr_controls_get_roll_moment(msg);
    lqr_controls->pitch_moment = mavlink_msg_lqr_controls_get_pitch_moment(msg);
    lqr_controls->yaw_moment = mavlink_msg_lqr_controls_get_yaw_moment(msg);
    lqr_controls->thrust_moment = mavlink_msg_lqr_controls_get_thrust_moment(msg);
    lqr_controls->roll_angle = mavlink_msg_lqr_controls_get_roll_angle(msg);
    lqr_controls->pitch_angle = mavlink_msg_lqr_controls_get_pitch_angle(msg);
    lqr_controls->yaw_angle = mavlink_msg_lqr_controls_get_yaw_angle(msg);
#else
        uint8_t len = msg->len < MAVLINK_MSG_ID_LQR_CONTROLS_LEN? msg->len : MAVLINK_MSG_ID_LQR_CONTROLS_LEN;
        memset(lqr_controls, 0, MAVLINK_MSG_ID_LQR_CONTROLS_LEN);
    memcpy(lqr_controls, _MAV_PAYLOAD(msg), len);
#endif
}
