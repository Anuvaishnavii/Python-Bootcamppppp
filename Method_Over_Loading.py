'''class cal:
    def add(self,args):
        return sum(args)
obj1=cal
print(obj1.add())'''
class cal:
   ''' def add(a,b,c):
        return a+b+c
    def add(a,b,c,d):
        return a+b+c+d
    def add(a,b,c,d,e):
        return a+b+c+d+e'''
   def add(self,*args):
      return sum(args)
obj1=cal
print(obj1.add(1,5,3))
print(obj1.add(1,2,3,4))
print(obj1.add(1,2,3,4,5))