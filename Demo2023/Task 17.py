with open("Assets/DataFor17.txt") as f:
    data = [int(i) for i in f]
    max = -1000000
    for i in data:
        if abs(i) % 10 == 3 and i > max:
            max = i
    count = 0
    max_count = 0
    for i in range(len(data)-1):
        if ((abs(data[i]) % 10 == 3 and abs(data[i+1]) % 10 != 3) or\
            (abs(data[i+1]) % 10 == 3 and abs(data[i]) % 10 != 3)) and\
            (data[i]**2 + data[i+1]**2) >= max**2:
            count +=1
            if data[i]**2 + data[i+1]**2 > max_count:
                max_count = data[i]**2 + data[i+1]**2

print(count, max_count)