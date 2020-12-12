# An object could represent an animal with proerties like name, age, breed, behaviors etc
# Classes include methods, variables and can be used as a blueprint to produce many objects with the same properties and behaviors. The obects of a class are called instances.
class Dog:
  species = 'mammal'
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def humanTime(self, dogAge):
    self.dogAge = dogAge * 7
  print (species)

dog1 = Dog('Daneil', '')
dog2 = Dog('Dog2', 10)

print (dog1.name)
print (dog2.name, dog2.age)



