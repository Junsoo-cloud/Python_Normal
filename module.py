# Python Module

import sys

print(sys.path)
print(type(sys))
print(type(sys.path))  # Type: list , so you can append some path to use.

import test_module

print(test_module.test_func())
