# https://codility.com/programmers/task/triangle
def main():
    print(solution([10,2,5,1,8,20])) # 1
    print(solution([10,50,5,1])) # 0

def solution(A):
    if len(A) < 3 :
		return 0
    	
    A.sort()
    
    for x in xrange(0, len(A) -2 ):
        if A[x] + A[x+1] > A[x+2]:
            return 1
    return 0	

if __name__ == "__main__":
    main()