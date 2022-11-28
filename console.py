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
            if '"' in x:
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
        if str(res) == ii[1].replace('"',''):
            result = "TRUE"
        print(str(cnt)+": "+result)
        cnt+=1











def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]
        

def solution(A,B):
    _list = []
    for i in range(3**6):
        x = convert_notation(i,3)
        x = x.zfill(7 - len(x))
        _list.append(x)

    a = 1
    b = _list[len(_list)-1]
    c = 1




    





                


            






s = '[1, 4, 2]	[5, 4, 4]	29 [1,2]	[3,4]	10'
run(s,2,"solution")





            
             
        
            
            
            




