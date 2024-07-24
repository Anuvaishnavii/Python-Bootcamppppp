'''class Myclass:
    def add(a,b):
        return a+b
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.add(12,5))'''

class myclass:
    def add(a,b):
        return a+b 
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    def div(a,b):
        return a/b
obj1=myclass
obj2=myclass
print(obj1.add(15,8))
print(obj1.sub(15,8))
print(obj1.mul(15,8))
print(obj1.mod(15,8))
print(obj1.div(15,8))
print(obj2.add(15,8))
print(obj2.sub(15,8))
print(obj2.mul(15,8))
print(obj2.mod(15,8))
print(obj2.div(15,8))