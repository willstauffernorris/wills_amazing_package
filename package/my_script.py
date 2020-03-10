
import pandas as pd

from package.my_mod import mega

print('hell ya')


x=5
print("number", x)

print("mega number", mega(x))

from package.my_mod import list_to_series

wills_list = [1,2,3]
print('before')
print(type(wills_list))
wills_list = list_to_series(wills_list)
print('after')
print(type(wills_list))
