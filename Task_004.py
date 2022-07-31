# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.



def create_list(num: int) -> list: 
    from random import randint
    n_list = []
    for i in range(0, num):
        n_list.append(randint(-num, num+1))
    return n_list


# Чтобы числа в списке не повторялись можно использовать этот код
# def create_list(num: int) -> list:
#     from random import randint
#     n_list = []
#     while len(n_list) < num:
#         for digit in range(0, num):
#             digit = randint(-num, num+1)
#             if digit in n_list:
#                 n_list.pop()
#             else:
#                 n_list.append(digit)
#     return n_list



def multiplication_digit(lst_1: list)-> int:
    lst_2 = input(f'Select positions of numbers to multiply (from 0 to {len(lst_1)-1}) separated by spaces:').split()
    product = 1
    for digit in lst_2:
        index = int(digit)
        product *= lst_1[index]
    return product


number = int(input('Input a number: '))
lst = create_list(number)
print(lst)
print(multiplication_digit(lst))


