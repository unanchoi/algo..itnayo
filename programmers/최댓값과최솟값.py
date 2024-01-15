# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numbers = list(map(int,s.split()))
    return f"{min(numbers)} {max(numbers)}"
