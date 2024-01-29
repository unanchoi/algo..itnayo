def solution(s):
    words =  s.split(" ")
    answer = 0

    for i in range(len(words)):
        if words[i] == "Z":
            answer -= int(words[i-1])
        else:
            answer += int(words[i])
    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))