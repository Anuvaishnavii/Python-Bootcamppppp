#Constructor
class myclass:
    cls_var="I'm class variable"
    def add(a,b):
        ins_var_add="I'm instance variable"
        print(ins_var_add)
        print(cls_var)
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