from abc import ABC, abstractmethod
from typing import List
from observer import Observer

class Subject(ABC):
    """
    The Subject interface declares methods for attaching, detaching, and notifying observers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass