# Test Module


def test_func():
  return 'test func'


print('------------')

# testing -> Should not seen in another file
# print(f'testing function : {test_func()} ')

# hide our testing code

if __name__ == '__main__':
  print(f'testing function : {test_func()} ')
