Adapter Pattern

Overview

The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by wrapping an existing class with a new interface.

This implementation follows the SOLID principles to ensure modular and scalable code.

Participants

Target Interface (target.py):   Defines the domain-specific interface used by the client.
Adaptee (adaptee.py)        :   Contains some useful behavior but has an incompatible interface.
Adapter (adapter.py)        :   Makes the Adaptee's interface compatible with the Target interface.
Client (main.py)            :   Interacts with the Target interface and uses the Adapter to communicate with the Adaptee.

How It Works

Client uses the Target interface to make requests.
The Adapter translates those requests into a form that the Adaptee understands.
The Adaptee executes the requested operation and returns the result to the Adapter, which passes it back to the Client.

Benefits of Adapter Pattern

Reusability: Allows the reuse of existing functionality with incompatible interfaces.
Single Responsibility Principle: Separates the concerns of adapting an interface from the business logic.
Open/Closed Principle: The Adapter can be extended to support additional Adaptee implementations without modifying the client code.

Example Use Cases

Integrating third-party libraries with your application.
Migrating legacy code to a new system.
Connecting new systems to old ones with incompatible interfaces.