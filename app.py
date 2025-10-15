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

list1 = [1, 2, 3, 4, 5]
list2 = [x**2 for x in list1 if x%2 == 0]
print(list2)  # [4, 8]

list = ['apple', 'banana', 'cherry']
new_list = [x for x in list if x != 'banana']
print(new_list)