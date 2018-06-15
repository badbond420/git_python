import os

def add_nums(input_list):
    result = 0
    for num in input_list:
        result += num

    return result

arr = [9,7,8,9]
print(add_nums(arr))