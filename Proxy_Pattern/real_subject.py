from subject import Subject

class RealSubject(Subject):
    """
    The RealSubject contains the core business logic.
    """
    def request(self) -> str:
        return "RealSubject: Handling the request."