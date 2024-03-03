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

  # Instance Method
  def get_price_culc(self):
    return 'After Car Price -> company: {} Price: {}'.format(
        self._company,
        self._details.get('price') * Car.price_per_raise)

  # Class Method: To render our class variable
  @classmethod
  def raise_price(cls, per):
    if per <= 1:  # Can make a logic or some additional code
      print('Please enter 1 or more')
      return
    cls.price_per_raise = per
    print('Success!')


# Instance
car1 = Car('Ferrari', {'color': 'white', 'price': 5000})
car2 = Car('BMW', {'color': 'black', 'price': 8000})
car3 = Car('Audi', {'color': 'blue', 'price': 4000})

# PriceInfo(Before, unused class method)

print(car1.get_price())
print(car2.get_price())

# PriceInfo(After, unused class method)

Car.price_per_raise = 1.4

print(car1.get_price_culc())
print(car2.get_price_culc())

# PriceInfo(After, used class method)

Car.raise_price(1)
Car.raise_price(1.8)

print(car1.get_price_culc())
print(car2.get_price_culc())

# https://www.inflearn.com/course/lecture?courseSlug=%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90&unitId=28602&tab=curriculum 5분
