class Target:
    """
    Defines the domain-specific interface used by the client.
    """
    def request(self) -> str:
        return "Target: The default target's behavior."