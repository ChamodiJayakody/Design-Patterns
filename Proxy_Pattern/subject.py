from abc import ABC, abstractmethod

class Subject(ABC):
    """
    The Subject interface declares common operations that both RealSubject and the Proxy implement.
    """
    @abstractmethod
    def request(self) -> str:
        pass
