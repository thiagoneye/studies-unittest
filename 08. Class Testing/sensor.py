class Sensor:
    def __init__(self, type):
        self.type = type
        self.breach_detected = False

    def detect_breach(self):
        if self.breach_detected:
            print(f"{self.type} sensor detected a security breach.")
            return True
        else:
            return False
