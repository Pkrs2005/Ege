from math import factorial

print (factorial(2023)/factorial(2020))




# Такое решение возсможно, 
# если числа(глубина рекурсии) не превышает +- 900
#
#
# def f(x):
#     if x == 1:
#         return 1
#     return x * f(x-1)

# T = f(2023)/f(2020)
# print (T)