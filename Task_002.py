# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplicity(n: int):
    product = []
    factorial = 1
    for i in range(1, n+1):
        factorial = i*factorial
        product.append(factorial)
    return product


number = int(input('Input a number: '))
print(f'-->{multiplicity(number)}')



# Variant 2

# import math


# def multiplicity(n: int):
#     product = []
#     for i in range(1, n+1):
#         factorial = math.factorial(i)
#         product.append(factorial)
#     return product


# number = int(input('Input a number: '))
# print(f'-->{multiplicity(number)}')


# Variant 3

# def multiplicity(n: int):
#     product = []
#     factorial = 1
#     i=1
#     while i<=n:
#         factorial *= i
#         i+=1
#         product.append(factorial)
#     return product


# number = int(input('Input a number: '))
# print(f'-->{multiplicity(number)}')



# Variant 4

# def multiplicity(n: int):
#     product = []
#     for i in range(0, n):
#         def factorial(i):
#             return 1 if (i == 1 or i == 0) else i * factorial(i - 1)
#         i += 1
#         product.append(factorial(i))
#     return product


# number = int(input('Input a number: '))
# print(f'-->{multiplicity(number)}')