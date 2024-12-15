from component import Component

class Decorator(Component):
    """
    Base Decorator class that delegates operations to a wrapped component.
    """
    def __init__(self, component: Component):
        self._component = component

    def operation(self) -> str:
        return self._component.operation()