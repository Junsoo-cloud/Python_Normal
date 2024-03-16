# Chpater02-03


class Car(object):
  '''
  Car Class
  Author : KIM
  Date: 2024.02.28
  Description: Class, Static, Instance Method
  '''
  # class variable: Shared with all instance
  price_per_raise = 1.0

  def __init__(self, company, details):
    self._company = company
    self._details = details

  def __str__(self):  # User level
    return f'Car: {self._company} {self._details}'

  def __repr__(self):  # Developer level
    return f'Car: {self._company} {self._details}'

  # Instance Method
  # Self: Using a unique attribute of object
  def detail_info(self):
    print('Car Detail info: {} {}'.format(self._company,
                                          self._details.get('price')))

  # Instance Method
  def get_price(self):
    return 'Before Car Price -> company: {} Price: {}'.format(
        self._company, self._details.get('price'))

  def get_price_culc(self):
    return 'After Car Price -> company: {} Price: {}'.format(
        self._company,
        self._details.get('price') * Car.price_per_raise)


# Instance
car1 = Car('Ferrari', {'color': 'white', 'price': '1.5M'})
car2 = Car('BMW', {'color': 'black', 'price': '2.5M'})
car3 = Car('Audi', {'color': 'blue', 'price': '3.5M'})

# PriceInfo(Before)

print(car1.get_price())
print(car2.get_price())

# PriceInfo(After, unused class method)

Car.price_per_raise = 1.4

print(car1.get_price_culc())
print(car2.get_price_culc())
# d
