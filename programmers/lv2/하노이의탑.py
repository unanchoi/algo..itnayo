def solution(n):

    def seq(start, target, temp, N):
        if N == 1:
            return [[start, target]]
        return seq(start, temp, target, N-1) + [[start, target]] + seq(temp, target, start, N-1)
    
    return seq(1,3,2,n)