from subject import Subject
from real_subject import RealSubject

class Proxy(Subject):
    """
    The Proxy contains a reference to the RealSubject. It can control access to it.
    """
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self) -> str:
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        return "Proxy: Access denied."

    def check_access(self) -> bool:
        """
        Simulate access control logic.
        """
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        """
        Simulate logging the access.
        """
        print("Proxy: Logging the time of request.")