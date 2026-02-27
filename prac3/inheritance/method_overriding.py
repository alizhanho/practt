class Animal:
    def speak(self):
        print("Animal sounds")


class Cat(Animal):
    def speak(self):
        print("Meow")


cat = Cat()
cat.speak()