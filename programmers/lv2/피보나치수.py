# https://school.programmers.co.kr/learn/courses/30/lessons/12945

import sys

sys.setrecursionlimit(1000000)

def solution(n):
    cache = [0] * (n+2)

    def calc(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1

        if cache[x] != 0:
            return cache[x]   
        cache[x] = calc(x-1) + calc(x-2
                                    )
        return cache[x] % 1234567
    return calc(n)
    
print(solution(1000))
print(solution(5))