from target import Target
from adaptee import Adaptee

class Adapter(Target):
    """
    Makes the Adaptee's interface compatible with the Target's interface.
    """
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        # Translate the Adaptee's behavior into the Target's interface.
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"