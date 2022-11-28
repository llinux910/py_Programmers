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








def solution(s):
    cnt = 0
    for c in s:
        if cnt<0:
            return False
        cnt = cnt+1 if c=="(" else cnt-1 if c==")" else cnt
    return cnt==0
        





s = '"()()"	true "(())()"	true ")()("	false "(()("	false'
run(s,1,"solution")





            
             
        
            
            
            




