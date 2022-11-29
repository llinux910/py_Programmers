from hwcounter import Timer, count, count_end
from time import sleep


def getCleanList(s,resultIndex):
    f = s.split("	")
    d_char = ","
    c =""
    cnt = 0
    _list = []
    for x in f:
        if cnt==resultIndex:
            if x.count('"')==4:
                c = c[0:len(c)-1]
                xx = x[x.find('"'):x.find('"',1)+1]
                y = x[x.find('"',2)+1:len(x)]
                c+="#"
                c+=xx
                _list.append(c)
                c = y+d_char
                cnt = 1
            else:
                ff = x.split(" ")
                c = c[0:len(c)-1]
                c+="#"
                c+= ff[0]
                _list.append(c)
                c = x[x.find(" ")+1:len(x)]+d_char
                cnt = 1
        else:
            c+=x+d_char
            cnt+=1
    return _list

def run(argString,resultIndex,excFunc):
    s = getCleanList(argString,resultIndex)
    cnt = 1
    for i in s:
        ii = i.split("#")
        s = 'res ='+excFunc+'('+ii[0]+')'
        result = "FALSE"
        start = count()
        
        exec(s,globals())
        sleep(1)
        elapsed = count_end() - start
        print(f'Elapsed cycles: {elapsed:,}')
        match = ii[1].replace('"','')
        if match =="true":
            match="True"
        elif match =="false":
            match ="False"

        if str(res) == match:
            result = "TRUE"
        print(str(cnt)+": "+result)
        cnt+=1




from math import gcd

import math

def solution(brown, yellow):
    sum = brown+yellow
    cnt = 0
    answer = []

    while(True):
        a,b = divmod(sum,2)
        if b is not 0:
            answer.append(cnt*2)
            answer.append(sum)
            break
        else:
            cnt+=1
            sum = a
        
    sorted(answer)

   

    return answer




s = '10	2	[4, 3] 8	1	[3, 3] 24	24	[8, 6]'
run(s,2,"solution")





            
             
        
            
            
            




