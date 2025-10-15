# class Car:
#     def __init__(self, name = '', age = ''):
#         print('klll');
#         self.name = name
#         self.age = age
#     name = 'My Car'
#     color = '#00AABA'

# car1 = Car('Toyota', 5)
# print(car1.name)
# print(car1.age)
# print(car1.color)
# print(car1.name)

# car2 = Car()
# print(car2.name)


# class Car:
#     name = "Default Car"  # Class variable

#     def __init__(self, name):
#         self.name = name  # Instance variable overrides class variable

# car1 = Car("Tesla")
# # car2 = Car()

# print(car1.name)  # Tesla  (instance variable)
# # print(car2.name)  # BMW    (instance variable)
# print(Car.name)   # Default Car (class variable)

# x = 256
# y = 256
# print(x is y)  # True → Python caches small integers

# x = 257
# y = 257
# print(x is y)  # False → new objects created

# List Comprehension

# list1 = [1, 2, 3, 4, 5]
# list2 = [x**2 for x in list1 if x%2 == 0]
# print(list2)  # [4, 8]

# list = ['apple', 'banana', 'cherry']
# new_list = [x for x in list if x != 'banana']
# print(new_list)

#  Deep copy vs Shallow copy

import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)
original[0][0] = 99
print(original)         # [[99, 2, 3], [4, 5, 6]]
print(shallow_copied)  # [[99, 2, 3], [4, 5, 6]]
print(deep_copied)     # [[1, 2, 3], [4, 5, 6]]

# Lambda Function

x = lambda a : a+10
print(x(5))  # 15

y = lambda a, b,c  : a if a > b and a>c else b if b>c else c
print(y(2, 10, 3))  # 10

list1 = [5, 2, 9, 1]
new_list = list(map(lambda x: x*2, list1))
print(new_list)  # [10, 4, 18, 2]
print(list1)  # [5, 2, 9, 1]

list4 = [5, 2, 9, 1]
def square(x):
    return x*x
squared_list = list(map(square, list1))
print(squared_list)  # [25, 4, 81, 1]