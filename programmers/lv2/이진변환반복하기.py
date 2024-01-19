# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(word):
    answer = [0,0]

    while word != "1":
        n = word.count("0")
        answer[1] += n
        word = word.replace("0","")
        word = bin(len(word))[2:]
        answer[0] += 1
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))