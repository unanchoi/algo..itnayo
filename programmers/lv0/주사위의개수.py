def solution(box, n):
    x, y, z = box

    a = x // n
    b = y // n
    c = z // n
    return a * b * c

print(solution([1,1,1], 1))
print(solution([10, 8, 6], 3))