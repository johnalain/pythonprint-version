# class Person:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age

#      def __repr__(self):
#          return f"Person(name={self.name}, age={self.age})"
# p = Person("Mike", 25)
# p1 = Person("rita",27)
# p2 = Person("josephine",27)
# print(p)
# print(p1)
# print(p2)
#===============================
class Person:
        def __init__(self,name,age,grade,address):
                self.name = name
                self.age = age
                self.grade = grade
                self.address = address
        def __repr__(self):
                return f"Person(name= {self.name} age ={self.age} grade = {self.grade} address = {self.address})"
p = ("rita",27,95,"st francisco")
p1 = ("josephine",26,90,"paris")
p2 = ("michel",26,90,"beirut")
print(p)
print(p1)
print(p2)
"""output:
('rita', 27, 95, 'st francisco')
('josephine', 26, 90, 'paris')
('michel', 26, 90, 'beirut')
"""