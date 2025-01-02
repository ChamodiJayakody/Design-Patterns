from singleton_class import Singleton

if __name__ == "__main__":
    # The client code.
    singleton1 = Singleton("First Instance")
    print(singleton1.some_business_logic())

    singleton2 = Singleton("Second Instance")
    print(singleton2.some_business_logic())

    # Verify that singleton1 and singleton2 are the same instance.
    if id(singleton1) == id(singleton2):
        print("singleton1 and singleton2 are the same instance.")
    else:
        print("singleton1 and singleton2 are different instances.")