# Author: CMOB 1/27/2022

def factorial(num):
    sum = ""
    index = 0
    while index  <= num - 1:
        sum += (str(index + 1))
        index += 1

    print(sum)


factorial(5)
factorial(88)

