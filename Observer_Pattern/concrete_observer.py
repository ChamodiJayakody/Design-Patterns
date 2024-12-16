from observer import Observer

class ConcreteObserverA(Observer):
    def update(self, message: str) -> None:
        print(f"ConcreteObserverA: Reacted to the event with message: {message}")

class ConcreteObserverB(Observer):
    def update(self, message: str) -> None:
        print(f"ConcreteObserverB: Reacted to the event with message: {message}")