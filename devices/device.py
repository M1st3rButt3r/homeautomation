class Device:
    def __init__(self):
        self.actions = {

        }

    def execute(self, action):
        if action in self.actions:
            self.actions[action]()

