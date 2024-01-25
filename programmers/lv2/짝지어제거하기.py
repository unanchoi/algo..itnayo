# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12973

from collections import deque

def solution(w: str):
    q = deque()

    for i in range(len(w)):
        if i == 0:
            q.append(w[i])
        else:
            if len(q) > 0:
                if w[i] == q[-1]:
                    q.pop()
                else:
                    q.append(w[i])
            else:
                q.append(w[i])
    
    if len(q) == 0:
        return 1
    else:
        return 0
    
print(solution("baabaa"))
print(solution("aabcbc"))
print(solution("cdcd"))