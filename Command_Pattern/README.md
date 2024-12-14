Command Pattern

Overview

The Command Pattern is a behavioral design pattern that encapsulates a request as an object, allowing you to parameterize objects with different requests, delay or queue a request's execution, and support undoable operations.

This implementation follows the SOLID principles for better maintainability and scalability.

Participants

Command Interface (command.py)          :  Declares the execute method that all concrete commands implement.
Concrete Commands (concrete_commands.py):  ConcreteCommandA: Executes action_a on the Receiver.
                                           ConcreteCommandB: Executes action_b on the Receiver.
Receiver (receiver.py)                  :  Contains the business logic, e.g., action_a and action_b.
Invoker (invoker.py)                    :  Holds references to commands and triggers them.
Client (main.py)                        :  Creates commands and configures the invoker with them.

How It Works

Client creates commands (ConcreteCommandA and ConcreteCommandB) and assigns them to the Invoker.
Invoker calls execute on the assigned commands at the appropriate time.
Receiver performs the actual business logic.

Benefits of Command Pattern

Encapsulation of Requests: Encapsulates requests as objects, allowing flexibility in the request's execution.
Open/Closed Principle: New commands can be added without modifying existing code.
Undo/Redo: Provides a way to easily implement undoable actions by storing history of commands.

Example Use Cases

GUI buttons and menu actions.
Transactional systems (e.g., database commits/rollbacks).
Task scheduling and queueing systems.
