from itertools import *


numbers = product('01234567', repeat = 5) #  <=== важная херня
cnt = 0

for n in numbers:
    number = ''.join(n)
    if number.count('6') == 1 and number[0] != '0':                            # условие можно переносит с помощью '\'
        if '61'  in number or '16'  in number or '36'  in number or\
            '63'  in number or '56'  in number or '65'  in number or\
                    '67'  in number or '76'  in number:
            continue                              #continue пропускаем это значение в цикле(cnt не прибавляется)
        cnt +=1
print (cnt)
            



# вот что бывает если пытаться изобрести велосипед
# i = 0
# for x1 in range(8):
#     for x2 in range(8):
#         for x3 in range(8):
#             for x4 in range(8):
#                 for x5 in range(8):
#                     figurs = str(x1)+str(x2)+str(x3)+str(x4)+str(x5)
#                     if figurs.count('6') == 1:
#                         if not(figurs.('16','36','56','76','61','63','65','67')):     <==== не ебу как это сделать
#                             i += 1
# print(i)
# p.s. своим способом нихуя не вышло
