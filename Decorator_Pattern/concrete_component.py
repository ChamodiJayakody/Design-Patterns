from component import Component

class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. These
    are what decorators can dynamically modify.
    """
    def operation(self) -> str:
        return "ConcreteComponent: Performing core operation."