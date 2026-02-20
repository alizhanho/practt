class Animal:
    def speak(self):
        print("Animal makes a sounds")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()