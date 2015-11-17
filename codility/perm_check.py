# https://codility.com/programmers/task/perm_check
def main():
    print(solution([4,1,3,2])) # 1
    print(solution([4,1,3])) # 0

def solution(A):

    numbers = set()
    highest = A[0]

    for l in xrange(0,len(A)):

    	t = A[l]

    	if t in numbers:
    		return 0

    	if t > highest:
    		highest = t

    	numbers.add(t)

    if len(numbers) == highest:
    	return 1 

    return 0

if __name__ == "__main__":
    main()