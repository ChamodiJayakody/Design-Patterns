from singleton import SingletonMeta

class Singleton(metaclass=SingletonMeta):
    """
    Singleton class that uses the SingletonMeta metaclass.
    """
    def __init__(self, value: str):
        self.value = value

    def some_business_logic(self) -> str:
        return f"Singleton instance with value: {self.value}"