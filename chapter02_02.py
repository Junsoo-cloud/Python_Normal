# Chpater02-02
# python class


class Car(object):
  '''
  Car Class
  Author : KIM
  Date: 2024.02.28
  '''
  # class variable: Shared with all instance
  car_count = 0

  def __init__(self, company, details):
    self._company = company
    self._details = details
    # self.car_count = 10
    Car.car_count += 1

  def __str__(self):  # User level
    return f'Car: {self._company} {self._details}'

  def __repr__(self):  # Developer level
    return f'Car: {self._company} {self._details}'

  def __del__(self):
    Car.car_count -= 1

  def detail_info(self):
    print('Car Detail info: {} {}'.format(self._company,
                                          self._details.get('price')))


# Instance
car1 = Car('Ferrari', {'color': 'white', 'price': '1.5M'})
car2 = Car('BMW', {'color': 'black', 'price': '2.5M'})
car3 = Car('Audi', {'color': 'blue', 'price': '3.5M'})
# Mean of self
print(car1._company == car2._company)  # False(value)
print(car1 is car2)  # False(id)

# dir
print(dir(car1))
print(dir(car2))

# Namespace
# __dict__
print(car1.__dict__)

# __doc__
print(car1.__doc__)

# id compare -> Many instance of one class
print(id(car1.__class__), id(car2.__class__))

# Error
# Car.detail_info() -> Need self argument

# NoneError
Car.detail_info(car2)
car1.detail_info()

# class variable
print(car1.__dict__)  # can't see class variable
print(car1.car_count)  # But can access class variable
print(dir(car1))  # can see class variable

# class variable access

print(Car.car_count)
print(car1.car_count)

# config del
del car2
print(Car.car_count)

# If argument is not in instance variable, it will be looked up in the class namespace.
# So, you can make variable with same name(Class & Instance) -> Instance variable will be # used first, but None -> Class variable will be used.
