class Animal:
    def speak():
        return "Speaking.........."
class Dog(Animal):
    def speak():
        return "Dog is speaking..."
class puppy(Dog):
    def speak():
        return "Puppy is speaking...."
obj3=puppy
print(obj3.speak())


def run():
    return "Running"
def run():
    return "The previous data is lost"
print(run())