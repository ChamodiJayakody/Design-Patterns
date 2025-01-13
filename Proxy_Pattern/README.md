# Proxy Design Pattern

## Overview
The **Proxy Pattern** is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. The proxy object acts as an intermediary, forwarding requests to the real object while adding additional behavior such as caching, access control, or lazy initialization.

## Key Concepts
1. **Proxy**: The intermediary object that controls access to the real subject.
2. **Real Subject**: The actual object that performs the operations.
3. **Client**: The entity that interacts with the proxy instead of directly accessing the real subject.

## Components
1. **Subject Interface**
    - Declares common operations that the real subject and proxy implement.

2. **Real Subject**
    - Implements the operations defined in the subject interface.

3. **Proxy**
    - Implements the subject interface.
    - Controls access to the real subject and may add additional functionality.

## Applications
- Access control for sensitive operations or resources.
- Lazy initialization to defer object creation until necessary.
- Adding logging or monitoring behavior without modifying the real subject.
- Remote method invocation in distributed systems.

## Advantages
- Adds a level of control over the real subject.
- Promotes separation of concerns by decoupling the client and real subject.
- Useful for optimizing resource usage and adding additional behavior transparently.

## Disadvantages
- Adds complexity to the system.
- May introduce a slight performance overhead.