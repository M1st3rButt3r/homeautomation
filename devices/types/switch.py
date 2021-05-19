from devices.device import Device


class Switch(Device):
    def __init__(self):
        self.actions = {
            "on": self.on
        }

    def on(self):
        print("on")
