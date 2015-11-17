# https://codility.com/programmers/task/tape_equilibrium
def main():
    print(solution([3,1,2,4,3])) # 1

def solution(A):

    head = A[0]
    tail = sum(A[1:]) 

    smallest_difference = abs(head-tail)

    for x in xrange(1,len(A)-1):

        head += A[x]
        tail -= A[x]

        diff = abs(head - tail)
        if diff < smallest_difference:
            smallest_difference = diff
        
    return smallest_difference

if __name__ == "__main__":
    main()