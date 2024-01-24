# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    tmp = n
    while True:
        n += 1
        if str(bin(tmp)[2:]).count("1") == str(bin(n)[2:]).count("1"):
            tmp = n
            break
    return tmp


print(solution(78))
print(solution(15))

