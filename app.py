import os
import sys

def add_nums(input_list):
    result = 0
    for num in input_list:
        result += num
    return result


def mul_nums(input_list):
    result = 1
    for num in input_list:
        result *= num
    return result

if __name__ == "__main__":
    arr = [9,7,8,9,10]
    print(add_nums(arr))
