class Alarm:
    def __init__(self, name):
        self.name = name
        self.sounding = False

    def sound(self):
        self.sounding = True
        print(f"{self.name} alarm is sounding.")

    def silence(self):
        self.sounding = False
        print(f"{self.name} alarm has been silenced.")
