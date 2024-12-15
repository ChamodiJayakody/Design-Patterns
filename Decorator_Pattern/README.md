Decorator Pattern

Overview

The Decorator Pattern is a structural design pattern that lets you dynamically add behavior or responsibilities to objects without modifying their code. It uses composition to "wrap" objects, creating a flexible alternative to subclassing.

This implementation adheres to SOLID principles for better maintainability and extensibility.

Participants

Component Interface (component.py):                     Defines the interface that concrete components and decorators implement.
Concrete Component (concrete_component.py):             Implements the base functionality that can be decorated.
Decorator Interface (decorator.py):                     Maintains a reference to a component object and defines an interface that conforms to the component's interface.
Concrete Decorators (decorator_a.py, decorator_b.py):   Add specific behaviors to the component dynamically.
Client (main.py):                                       Configures and uses the decorated objects.

How It Works

Component defines the base interface for objects.
Concrete Component provides the core functionality.
Decorator wraps a component and adds new behavior dynamically.
The Client uses decorators to extend the behavior of components without modifying their code.

Benefits of Decorator Pattern

Open/Closed Principle: New decorators can be added without altering existing code.
Single Responsibility Principle: Responsibilities are divided among classes instead of being managed by a single class.
Flexibility: Allows dynamic composition of behaviors at runtime.

Example Use Cases

Adding UI elements (e.g., scrollbars, borders, shadows).
Adding features to existing objects in a flexible way (e.g., logging, security).
Extending functionality in frameworks and libraries.