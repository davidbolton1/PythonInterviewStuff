#Data types can be floating, integer, complex, strings, or chars
# 

class CreateValues:
  #The __init__ method demands a "value" when someone will #call the class CreateValues
  # It willautomatically craete an object which is called self in the class
  # An attatch # to it this value, then print

  def __init__ (self, value):
    self.value = value
    print(value)
    
  def printValueType(self):
    print("This is an object from the" + str(type(self.value)) + " " + str(self.value) )
  
  def changeValue(self, value):
    self.value = value

integer_value = CreateValues(2)
float_value = CreateValues(3.2)
float_value.printValueType()
print(float_value.value)
float_value.changeValue(.2)
float_value.printValueType()
boolean_value = CreateValues("tester")
boolean_value = CreateValues(bool())
print(boolean_value)



