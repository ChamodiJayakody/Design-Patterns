from command import Command
from receiver import Receiver

class ConcreteCommandA(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.action_a()

class ConcreteCommandB(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.action_b()
