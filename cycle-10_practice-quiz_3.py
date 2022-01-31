# Author: CMOB 1/31/2022

def fibonacci(num):
    index = 2 # start with 2 due to list already having indexs 0 and 1
    fib_nums = [0,1]

    while index < num:
            fib_nums.append(fib_nums[-2] + fib_nums[-1]) # adds the current and previous number together
            index += 1

    return fib_nums

print(fibonacci(5) == [0,1,1,2,3])
print(fibonacci(10) == [0,1,1,2,3,5,8,13,21,34])

