def solution(x):
    n = 0

    for i in str(x):
        n += int(i)
        
    if x % n == 0:
        return True
    else:
        return False
    
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))