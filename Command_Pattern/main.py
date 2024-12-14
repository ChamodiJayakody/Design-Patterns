from receiver import Receiver
from concrete_commands import ConcreteCommandA, ConcreteCommandB
from invoker import Invoker

if __name__ == "__main__":
    receiver = Receiver()
    
    # Create Commands
    command_a = ConcreteCommandA(receiver)
    command_b = ConcreteCommandB(receiver)

    # Configure the Invoker
    invoker = Invoker()
    invoker.set_on_start(command_a)
    invoker.set_on_finish(command_b)

    # Execute through Invoker
    print(invoker.do_something_important())