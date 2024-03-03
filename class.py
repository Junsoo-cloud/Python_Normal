class MyClass:
  # class variable
  class_variable = 0

  # __init__ method: 객체가 생성될 때 호출되며 객체의 초기화를 담당합니다.
  # self: 현재 인스턴스를 가리키는 참조로, 생성된 객체 자신을 가리킵니다.
  def __init__(self, param1, param2):
    # instance variable: 객체의 상태를 나타냅니다.
    self.param1 = param1
    self.param2 = param2

  # instance method: 객체에 대한 동작을 정의합니다.
  def instance_method(self):
    return self.param1 + self.param2

  # class method: 클래스와 관련된 동작을 정의합니다.
  @classmethod
  def class_method(cls):
    return cls.class_variable
