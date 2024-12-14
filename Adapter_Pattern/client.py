from target import Target

def client_code(target: Target) -> None:
    """
    The client code works with all objects using the Target interface.
    """
    print(target.request())