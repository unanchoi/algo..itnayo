def solution(left, right):

    def find_divisiors(n):
        k = 0
        for i in range(1,n+1):
            if n % i == 0:
                k += 1 
        return k

    answer = 0
    for n in range(left, right+1):
        if find_divisiors(n) % 2 == 0:
            answer += n
        else:
            answer -= n        
    return answer

print(solution(13,17))
print(solution(24,27))