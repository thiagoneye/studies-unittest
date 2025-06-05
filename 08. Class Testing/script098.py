import unittest
from security_system import SecuritySystem
from camera import Camera
from sensor import Sensor
from alarm import Alarm


class TestSecuritySystem(unittest.TestCase):
    def setUp(self):
        cameras = [Camera("Front Door"), Camera("Back Door"), Camera("Garage")]
        sensors = [Sensor("Window Sensor"), Sensor("Motion Sensor")]
        alarms = [Alarm("Main Alarm"), Alarm("Backup Alarm")]
        self.security_system = SecuritySystem(cameras, sensors, alarms)

    def test_arm(self):
        self.security_system.arm()
        self.assertTrue(
            self.security_system.armed, msg="The security system is disarmed."
        )

    def test_disarm(self):
        self.security_system.armed = True
        self.security_system.disarm()
        self.assertFalse(
            self.security_system.armed, msg="The security system is armed."
        )

    def test_notify_authorities(self):
        self.security_system.armed = True
        actual = self.security_system.notify_authorities()
        expected = "Notifying authorities of a security breach..."
        self.assertEqual(actual, expected)

        self.security_system.armed = False
        actual = self.security_system.notify_authorities()
        expected = "System is not armed."
        self.assertEqual(actual, expected)

    def test_detect_breach(self):
        self.assertFalse(
            self.security_system.detect_breach(), msg="The security system is armed."
        )

        self.security_system.armed = True
        self.security_system.sensors[0].breach_detected = True
        self.assertTrue(
            self.security_system.detect_breach(), msg="The security system is disarmed."
        )


if __name__ == "__main__":
    unittest.main()
