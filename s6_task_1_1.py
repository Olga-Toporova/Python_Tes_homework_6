'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
- 4 -> [1, 2, 6, 24]
- 6 -> [1, 2, 6, 24, 120, 720]
'''

from math import factorial

number = int(input("Введите число: "))
def num(n): return 1 if n == 1 else n*factorial(n-1)
print(list(num(i) for i in range(1, number+1)))

# Прошлое решение:
# result = 1
# result_list = list()
# for n in range(1, number + 1):
#      result *= n
#      result_list.append(result)
# print(result_list)
