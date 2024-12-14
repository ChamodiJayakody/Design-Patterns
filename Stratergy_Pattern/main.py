from duck import Duck
from fly_with_wings import FlyWithWings
from fly_no_way import FlyNoWay

if __name__ == "__main__":
    # Duck that can fly with wings
    mallard = Duck(FlyWithWings())
    print(mallard.perform_fly())

    # Change the behavior dynamically
    mallard.set_fly_behavior(FlyNoWay())
    print(mallard.perform_fly())