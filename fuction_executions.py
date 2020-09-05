from function.functions_return import *
from function.functions_return import find_num, desc_pizza

print(f"Total is {total}")
print(f"Total is {adding(456, 987)}")

full_name('dilovar', 'ibragimov')
name = full_name('john', 'doe')
# removed_value = list.pop()
print(f"{name}, Welcome to the class!")

student1 = full_name_dict('tatiana', 'shark')
print(student1)

nums = [5, 55, 76, 1, -9, 0, 1, 456]
find_num(nums, 1)

desc_pizza('chicken')
desc_pizza('chicken', 'peperoni', 'bbq chicken')
