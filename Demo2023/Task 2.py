print('x2,y1,z3,w4')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(y <= x) or (z <= w) or not(z)): #условие
                    print(x,y,z,w)