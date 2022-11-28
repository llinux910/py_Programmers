import console
from hwcounter import Timer, count, count_end
from time import sleep



def solution(s):
    min_num = ord('0')
    max_num = ord('9')
    answer = ''

    ss = s.split(" ")
    for i in ss:
        x = ord(i[0])
        if x>= min_num and x<=max_num:
            pass   
        else:
            x = i[0].upper()
            i = x + i[1:len(i)]

        answer+=i+" "


    return answer


argString = '"1 2 3 4"	"1 4" "-1 -2 -3 -4"	"-4 -1" "-1 -1"	"-1 -1"'
solution("1 2 3 4")
console.run(argString,1,"solution")