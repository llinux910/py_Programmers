def solution(brown, yellow):
    factors = []
    for i in range(1,yellow+1):
        if yellow%i==0:
            factors.append(i)
    for i in factors:
        for j in factors:
            if i*j == yellow:
                y_width = max(i,j)
                y_height = min(i,j)
                if brown == (y_width+2) *2 + (y_height*2):
                    return [y_width+2,y_height+2]

    return 



                
_list  = []
for i in range(1,1000):
    for j in range(1,1000):
        brown = (i+2)*2 + (j*2)
        yellow = i*j
        _min = min(i+2,j+2)
        _max = max(i+2,j+2)
        _list.append([brown,yellow,_max,_min])

for i in _list:
    res = solution(i[0],i[1])
    if i[2] != res[0] or i[3] != res[1]:
        print("{},{},{}".format(i[0],i[1],i[2]))
        break

    print("pass")
    