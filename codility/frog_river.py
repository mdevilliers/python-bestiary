# https://codility.com/programmers/task/frog_river_one
def main():
    print(solution(5, [1,3,1,4,2,3,5,4])) # 6

def solution(X,A):

    leafs = set()
    for l in xrange(0,len(A)):
        leafs.add(A[l])
        if len(leafs) == X :
            return l

    return -1   

if __name__ == "__main__":
    main()