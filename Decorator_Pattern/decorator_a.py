from decorator import Decorator

class ConcreteDecoratorA(Decorator):
    """
    Adds additional behavior before or after the base component's operation.
    """
    def operation(self) -> str:
        return f"DecoratorA: Adding behavior A.\n{self._component.operation()}"