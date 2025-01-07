Observer Pattern

Overview

The Observer Pattern is a behavioral design pattern that establishes a one-to-many relationship between objects, so that when one object (the Subject) changes state, all its dependents (the Observers) are notified and updated automatically.

This implementation adheres to SOLID principles for better maintainability and extensibility.

Participants

Subject Interface (subject.py): Declares methods for attaching, detaching, and notifying observers.
Concrete Subject (concrete_subject.py): Implements the Subject interface and stores the state of interest.
Notifies observers of any changes in its state.
Observer Interface (observer.py): Declares the update method, used by subjects to notify observers.
Concrete Observers (concrete_observer.py): Implement the Observer interface and react to updates from the Subject.
Client (main.py): Creates subjects and observers, attaches observers to subjects, and triggers
state changes.

How It Works

The Subject maintains a list of observers and notifies them whenever its state changes.
Observers implement the update method, which is called by the subject to propagate changes.
The Client sets up the system by attaching observers to the subject and triggering state changes.

Benefits of Observer Pattern

Decoupling: Subject and observers are loosely coupled.
Open/Closed Principle: Observers can be added or removed without modifying the subject.
Scalability: Multiple observers can listen to a single subject.

Example Use Cases

Event-driven systems (e.g., GUI frameworks, notification systems).
Messaging systems (e.g., pub/sub models).
Data-binding in MVC or MVVM architectures.
