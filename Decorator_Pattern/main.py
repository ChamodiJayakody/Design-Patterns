from concrete_component import ConcreteComponent
from decorator_a import ConcreteDecoratorA
from decorator_b import ConcreteDecoratorB

if __name__ == "__main__":
    # Base component
    component = ConcreteComponent()
    print(component.operation())

    # Component with Decorator A
    decorator_a = ConcreteDecoratorA(component)
    print(decorator_a.operation())

    # Component with Decorator A and Decorator B
    decorator_b = ConcreteDecoratorB(decorator_a)
    print(decorator_b.operation())
