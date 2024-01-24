# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    if n == 1:
        return 1
    
    answer = 0
    for i in range(1, n):
        s = (n - (i * (i-1) // 2))  
        if s < 0 or s == 0:
            break

        if s % i == 0:
            answer += 1
    return answer

print(solution(1))
print(solution(15))
# i * a + i(i-1) //  2 = n 