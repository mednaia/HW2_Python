# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



def create_sequence(num: int):
    list = []
    for num in range(1, num+1):
        digit = round(((1+1/num)**num),2)
        list.append(digit)
    return list

def find_sum(series: list):
    result = 0
    for i in range(len(series)):
        result += series[i]
    return result


number = int(input('Input a number: '))
sequence = create_sequence(number)
print(f'Resulting sequence: {sequence}')
summ = find_sum(sequence)
print(f'Sum of sequences elements = {summ}')



# Приведенная формула и пример не связаны друг с другом. Для вычисления последовательности, приведенной в примере
# используется формула (n*3)+1. На всякий случай выполнила задания и для закономерности, описанной в примере.

# def form_sequence(num: int):
#     list = []
#     for num in range(1, num+1):
#         digit = (num*3)+1
#         list.append(f'{num}: {digit}')
#     return list


# def create_sequence(num: int):
#     arr = []
#     for num in range(1, num+1):
#         digit = (num*3)+1
#         arr.append(digit)
#     return arr


# def find_sum(series: list):
#     result = 0
#     for i in range(len(series)):
#         result += series[i]
#     return result


# number = int(input('Input a number: '))
# print(form_sequence(number))
# sequence = create_sequence(number)
# summ = find_sum(sequence)
# print(f'Sum of sequences elements = {summ}')