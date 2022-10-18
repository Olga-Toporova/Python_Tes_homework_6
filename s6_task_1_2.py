'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in -> out
- 6782 -> 23
- 0.67 -> 13
- 198.45 -> 27
'''
from re import sub

print(sum(map(int, list(sub('[.,]', '', input(('Введите число: ')))))))

# Прошлое решение:
# result = 0
# for n in number:
#     if n != "." and n != ",":
#         result += int(n)
# print(result)