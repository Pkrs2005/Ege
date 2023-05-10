#Вот сое решение, пока сделал, 5 раз выключился пк изза переполнения оперативы. Неправильно прочитал условие
# и усложнил его настолько сильно что он переполнял оперативку(14 гб)
def condition_while(number):
    if number.count('>1') or number.count('>2') or number.count('>0'):
        return True
    return False

def easy_num(num):
    cnt = num.count('1') + num.count('2') * 2    
    for i in range(2, cnt):
        if cnt == i:
            continue
        if cnt % i == 0:
            return False
    return True

def main():
    for n in range(2,2000):
        number = '>'+ '0'*39+ '1'*n+'2'*39
        while condition_while(number):
            number = number.replace('>1', '22>')
            number = number.replace('>2', '2>')
            number = number.replace('>0', '1>')            
        number = number.replace('>', '') 
        if easy_num(number):
            print (n)
            break


main()


# а вот для пидарасов решение из инета:
#
#
# def f(a):
#     for i in range(2,a):
#         if a % i ==0:
#             return False
#     return True

# for n in range(999):
#     s= ">" + 39 *"0"+  n*"1" + 39 *"2"
#     while ">1" in s or ">2" in s or ">0" in s:
#         s=s.replace(">1" , "22>" , 1)
#         s=s.replace(">2" , "2>" , 1)
#         s=s.replace(">0" , "1>" , 1)
#     t=s.count("1") + s.count("2")*2
#     if f(t):
#         print(n)
#         break
#      
# Ну и что что блять короче??? мое то круче