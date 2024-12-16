from subject import Subject
from observer import Observer
from typing import List


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state changes.
    """
    def __init__(self):
        self._state: str = ""
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Subject: Detached an observer.")
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self._state)

    def some_business_logic(self, new_state: str) -> None:
        print(f"Subject: Changing state to {new_state}")
        self._state = new_state
        self.notify()