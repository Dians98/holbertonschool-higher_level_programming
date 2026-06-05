class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":

    exocet = FlyingFish()

    print("--- Method Execution ---")
    exocet.fly()
    exocet.swim()
    exocet.habitat()

    print("\n--- Method Resolution Order Exploration ---")
    print(FlyingFish.mro())
