from concrete_subject import ConcreteSubject
from concrete_observer import ConcreteObserverA, ConcreteObserverB

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    print("\nState Change 1:")
    subject.some_business_logic("State 1")

    print("\nState Change 2:")
    subject.some_business_logic("State 2")

    print("\nDetaching Observer A")
    subject.detach(observer_a)

    print("\nState Change 3:")
    subject.some_business_logic("State 3")