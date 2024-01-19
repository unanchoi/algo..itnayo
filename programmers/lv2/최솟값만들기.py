# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    C = sorted(A, reverse=True)
    D = sorted(B)
    for i in range(len(A)):
        answer += C[i] * D[i]

    return answer
