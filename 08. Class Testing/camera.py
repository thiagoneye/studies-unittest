class Camera:
    def __init__(self, location):
        self.location = location
        self.recording = False

    def detect_breach(self):
        if self.recording:
            print(f"{self.location} camera detected a security breach.")
            return True
        else:
            return False

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False
