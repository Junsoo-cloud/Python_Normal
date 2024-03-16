# Packing % Unpaking

# *args(tuple)


def args_func(*args):
  for num, arg in enumerate(args):
    print(f'result : {num} {arg}')
  print('-------')


args_func('foo', 'bar', 'baz')

# **kwargs(dict)


def kwargs_func(**kwargs):
  for n in kwargs.keys():
    print(f'result : {n} {kwargs[n]}')
  print('--------')


dicts = {
    'foo': 'bar',
    'baz': 'qux',
}
kwargs_func(foo='bar', baz='qux')
