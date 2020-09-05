# Return Values

def full_name(first,last):
    """Return full name"""
    # print(f"{first.title()} {last.title()}")
    return f"{first.title()} {last.title()}"

def adding(a,b):
    return  a+b
total =adding(456, 987)

def full_name_dict(first:str,last:str) -> dict:
    """Returns dictionary with first_name,last
    -name"""
    result = {'first_name': first.title(),'last_name': last.title()}
    return  result







# print(f"Total is {total}")
# print(f"Total is {adding(456, 987)}")
#
# full_name('dilovar','ibragimov')
# name = full_name('john','doe')
# # removed_value = list.pop()
# print(f"{name}, Welcome to the class!")
#
# student1 = full_name_dict('tatiana','shark')
# print(student1)


def find_num(num_list,number):
    for num in num_list:
        if num == number:
            print(f"{number} is found!!")
            break

# nums = [5 , 55 , 76 , 1 ,-9, 0 ,1 , 456]
# find_num(nums,1)

def desc_pizza(*toppings):
    print("We have only cheese pizza with following toppings:")
    print(toppings)

desc_pizza('chicken')
desc_pizza('chicken','peperoni','bbq chicken')