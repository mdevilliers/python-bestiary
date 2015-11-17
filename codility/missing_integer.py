# https://codility.com/programmers/task/missing_integer
def main():
    print(solution([1,3,6,4,1,2])) # 5
    print(solution([1])) # 2

def solution(A):

    numbers = set(A)
    length = len(A) + 1

    for l in xrange(1,length):
    	if l not in numbers:
    		return l

    return length

if __name__ == "__main__":
    main()