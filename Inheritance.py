class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
        def bark():
            return "Bowwwwuuuuuu"
class puppy(Dog):
        def puppy_speak():
            return "I'm Puppy"
obj1=Animal
obj2=Dog 
obj3=puppy
print(obj1.speak())
print(obj2.bark())
print(obj3.puppy_speak())