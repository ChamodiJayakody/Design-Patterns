class SingletonMeta(type):
    """
    A metaclass for creating Singleton classes.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # If an instance does not exist, create one and store it.
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]