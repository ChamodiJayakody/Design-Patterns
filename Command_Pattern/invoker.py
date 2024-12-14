from command import Command

class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """
    def __init__(self):
        self._on_start = None
        self._on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        results = []
        if self._on_start:
            results.append(self._on_start.execute())
        results.append("Invoker: Doing something really important...")
        if self._on_finish:
            results.append(self._on_finish.execute())
        return "\n".join(results)
