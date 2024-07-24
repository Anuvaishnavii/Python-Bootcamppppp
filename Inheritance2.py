class father:
    def father_speak():
        return "I'm her father"
class mother:
    def mother_speaks():
        return "I'm her mother"
class kid:
    def kid_speaks():
        return"I'm a product of my parents"
obj1=kid
obj2=mother
obj3=father
print(obj3.father_speak())
print(obj2.mother_speaks())
print(obj1.kid_speaks())