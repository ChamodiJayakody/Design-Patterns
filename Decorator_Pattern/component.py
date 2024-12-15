from abc import ABC, abstractmethod

class Component(ABC):
    """
    The Component interface defines operations that can be altered by decorators.
    """
    @abstractmethod
    def operation(self) -> str:
        pass