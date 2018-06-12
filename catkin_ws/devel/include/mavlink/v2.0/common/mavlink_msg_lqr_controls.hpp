// MESSAGE LQR_CONTROLS support class

#pragma once

namespace mavlink {
namespace common {
namespace msg {

/**
 * @brief LQR_CONTROLS message
 *
 *  Send controls generated from off board cobntroller to on board PD controller
 */
struct LQR_CONTROLS : mavlink::Message {
    static constexpr msgid_t MSG_ID = 229;
    static constexpr size_t LENGTH = 28;
    static constexpr size_t MIN_LENGTH = 28;
    static constexpr uint8_t CRC_EXTRA = 13;
    static constexpr auto NAME = "LQR_CONTROLS";


    float roll_moment; /*< actuator controls */
    float pitch_moment; /*< actuator controls */
    float yaw_moment; /*< actuator controls */
    float thrust_moment; /*< actuator controls */
    float roll_angle; /*< actuator controls */
    float pitch_angle; /*< actuator controls */
    float yaw_angle; /*< actuator controls */


    inline std::string get_name(void) const override
    {
            return NAME;
    }

    inline Info get_message_info(void) const override
    {
            return { MSG_ID, LENGTH, MIN_LENGTH, CRC_EXTRA };
    }

    inline std::string to_yaml(void) const override
    {
        std::stringstream ss;

        ss << NAME << ":" << std::endl;
        ss << "  roll_moment: " << roll_moment << std::endl;
        ss << "  pitch_moment: " << pitch_moment << std::endl;
        ss << "  yaw_moment: " << yaw_moment << std::endl;
        ss << "  thrust_moment: " << thrust_moment << std::endl;
        ss << "  roll_angle: " << roll_angle << std::endl;
        ss << "  pitch_angle: " << pitch_angle << std::endl;
        ss << "  yaw_angle: " << yaw_angle << std::endl;

        return ss.str();
    }

    inline void serialize(mavlink::MsgMap &map) const override
    {
        map.reset(MSG_ID, LENGTH);

        map << roll_moment;                   // offset: 0
        map << pitch_moment;                  // offset: 4
        map << yaw_moment;                    // offset: 8
        map << thrust_moment;                 // offset: 12
        map << roll_angle;                    // offset: 16
        map << pitch_angle;                   // offset: 20
        map << yaw_angle;                     // offset: 24
    }

    inline void deserialize(mavlink::MsgMap &map) override
    {
        map >> roll_moment;                   // offset: 0
        map >> pitch_moment;                  // offset: 4
        map >> yaw_moment;                    // offset: 8
        map >> thrust_moment;                 // offset: 12
        map >> roll_angle;                    // offset: 16
        map >> pitch_angle;                   // offset: 20
        map >> yaw_angle;                     // offset: 24
    }
};

} // namespace msg
} // namespace common
} // namespace mavlink
