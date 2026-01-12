# a = 101
# print(a)
# print(type(a))
# a = a + 6
# print(a)
# a = a - 890
# print(a)
# a = a /12
# print(a)
# flag = bool()
# flag = True
# print(flag)
# a = "rita josephine"
# print(a.title())
# print(a)
# print(a.upper())
# print(a)
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]
# list3 = list1 + list2
# print(list3)
# list3.append(98)
# print(list3)
# print(len(list3))
# new_list = [1,2,3,"rita","josephine",[2,3,5,6]]
# print(new_list)
# print(new_list[5][0])
# print(new_list[5][1])
# new_list[0]='josephine'
# print(new_list)
import pandas as pd
from sympy import series


df = pd.read_csv('/Users/michelkadi/Desktop/annual.csv')
series = pd.Series([1, 2, 3])
series = series.plot.bar  # ❌ now series is a function

print(df.head())
print(df.head())
# print(df.shape)
# print(df.columns)
print("====================")
# print(df.head(1))
# print(df.count())
print("====================")
# print(df.mean())
# print(df.max())
print("====================")
# print(df.min())
print("====================")
# print(df.median())

# https://youtu.be/bRog9Drs4kU?t=6277
# https://youtu.be/bRog9Drs4kU?t=6394
# 
print(df.describe())
print(df.plot.line())
print(series)
# print(df)
# import chardet
# with open('people.csv', 'rb') as f:
#     result = chardet.detect(f.read())
#     print(result)
#banda cheat sheet in samsung download


