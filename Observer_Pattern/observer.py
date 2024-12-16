from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, message: str) -> None:
        pass