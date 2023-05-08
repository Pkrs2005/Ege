def factorial(x):
    cnt = 1
    while x != 1: 
        cnt = cnt * x
        x-=1
    return cnt

def fucktorial(x):  #способ ебланский, работает при числах x <= 996
    if x == 1:
        return 1
    return x * fucktorial(x-1)
