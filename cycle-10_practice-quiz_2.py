# Author: CMOB 1/27/2022

def factorial(num):
    sum = ""
    index = 0
    while index  <= num - 1: # if index is less than num
        sum += (str(index + 1)) # continuously add the next number
        index += 1

    print(sum)


factorial(5)
factorial(88)

