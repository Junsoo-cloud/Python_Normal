# Chpater02-01
# python class
'''
OOP(Object Oriented Programming) : reuse of code, prevent resubmission of code, proper to big-scale project, easy to maintain
In python, class main -> data main -> manage to object

In Python, a namespace is a system that ensures that names in a program are unique and can be used without any conflict. It serves as a container for mapping names to objects, such as variables, functions, classes, etc. Namespaces are fundamental to Python's scoping rules and play a crucial role in organizing and accessing identifiers within a program.
'''


class Car(object):

  def __init__(self, company, details):
    self._company = company
    self._details = details

  def __str__(self):  # User level
    return f'Car: {self._company} {self._details}'

  def __repr__(self):  # Developer level
    return f'Car: {self._company} {self._details}'


car1 = Car('Ferrari', {'color': 'white', 'price': '1.5M'})  # car1 : instance

print(car1)
print(car1.__dict__)  # to see namespace
print(dir(car1))  # Built-in
