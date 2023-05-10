with open("Assets/DataFor24.txt") as f:
    data = f.readline()
    
    cnt = 0
    cnt_max = 0
    for i in range(len(data)):
        if i == len(data)-1:
            print(data[i-1])
            print(data[i])
            break

        if data[i]+data[i + 1] == "CA" or data[i]+data[i + 1] == "FO" or\
            data[i]+data[i + 1] == "CO" or data[i]+data[i + 1] == "DO" or\
            data[i]+data[i + 1] == "DA" or data[i]+data[i + 1] == "FA":
            cnt +=1
            if cnt > cnt_max:
                cnt_max = cnt
        cnt = 0
        
    print(cnt)