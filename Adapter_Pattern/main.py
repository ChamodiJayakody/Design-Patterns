from target import Target
from adaptee import Adaptee
from adapter import Adapter
from client import client_code

if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)

    print("\nClient: The Adaptee class has a weird interface. See, I don't understand it:")
    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.specific_request()}")

    print("\nClient: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)