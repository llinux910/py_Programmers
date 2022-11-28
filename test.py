def solution(s):
    cnt = 0
    for c in s:
        if cnt<0:
            return False
        x = x+1 if c=="(" else x-1 if c==")" else x
    return x==0


solution("()()")