from decorator import Decorator

class ConcreteDecoratorB(Decorator):
    """
    Adds another layer of behavior to the component.
    """
    def operation(self) -> str:
        return f"DecoratorB: Adding behavior B.\n{self._component.operation()}"