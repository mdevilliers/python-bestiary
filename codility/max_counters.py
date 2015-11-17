# https://codility.com/programmers/task/max_counters
# :-( 77%
def main():
    print(solution(5, [3,4,4,6,1,4,4])) # [3, 2, 2, 4, 2] 

def solution(N,A):

    rank = [0]* (N +1)
    max_increment = 0 

    for x in xrange(0,len(A)):
        t = A[x]

        if t > N:
            rank = [max_increment] * (N + 1)
        else :
            
            rank[t] += 1

            if rank[t] > max_increment :
                max_increment = rank[t]
        print( rank , t, max_increment)
    
    return rank[1:]

if __name__ == "__main__":
    main()