from real_subject import RealSubject
from proxy import Proxy

if __name__ == "__main__":
    print("Client: Executing with a RealSubject:")
    real_subject = RealSubject()
    print(real_subject.request())

    print("\nClient: Executing with a Proxy:")
    proxy = Proxy(real_subject)
    print(proxy.request())
