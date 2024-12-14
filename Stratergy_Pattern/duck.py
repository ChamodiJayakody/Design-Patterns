from fly_behavior import FlyBehavior

class Duck:
    def __init__(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def perform_fly(self):
        return self.fly_behavior.fly()

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior