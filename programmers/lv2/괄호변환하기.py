# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    if s[0] == ")":
        return False
    
    left_count = 0
    right_count = 0
    for a in s:
        if a == "(":
            left_count += 1
        else: # a == ")"
            right_count += 1 
            if left_count > 0:
                right_count -= 1
                left_count -= 1
            else:
                return False

    if left_count > 0 or right_count > 0:
        return False
    
    return True