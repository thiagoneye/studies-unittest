class SecuritySystem:
    def __init__(self, cameras, sensors, alarms):
        self.cameras = cameras
        self.sensors = sensors
        self.alarms = alarms
        self.armed = False

    def arm(self):
        self.armed = True

    def disarm(self):
        self.armed = False

    def notify_authorities(self):
        if self.armed:
            return "Notifying authorities of a security breach..."
        else:
            return "System is not armed."

    def detect_breach(self):
        if self.armed:
            for sensor in self.sensors:
                if sensor.detect_breach():
                    return True
            for camera in self.cameras:
                if camera.detect_breach():
                    return True
        return False

    def sound_alarms(self):
        if self.armed:
            for alarm in self.alarms:
                alarm.sound()
