class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

class Person:
  pass

p1 = Person()
p1.name = "Tobias" # properti dimasukkan secara manual
p1.age = 25

print(p1.name) #Tobias
print(p1.age)  

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
print(p1.name, p1.age) #Emil 18

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self): #self digunakan mengakses properti kelas
    print("Hello, my name is " + self.name)

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet() # Hello, my name is Emil

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info() # 2020 Toyota Corolla

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome() # Hello, Tobias! Welcome to our website

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome() # Hello, Tobias! Welcome to our website

class Person:
  Person.lastname = "" # ini properti Class

  def __init__(self, name):
    self.name = name # ini properti objrk

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)    # Emil
print(p2.name)    # Tobias 

Person.lastname = "Refsnes"
print(p1.lastname) # Refsnes

p1.city = "Oslo" # menambahkan properti baru ke objek yang sudah ada.

class Calculator:
  def add(self, a, b): 
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))      # 8
print(calc.multiply(4, 7)) # 28

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info()) # Tobias is 28 yaers old

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday() # Happy birthday! You are now 26
p1.celebrate_birthday() # Happy birthday! You are now 27

# Tanpa __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1) # <__main__.Person object at 0x15o39e602100>

# Dengan __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1) # Tobias (36)
