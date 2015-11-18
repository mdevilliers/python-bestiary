# https://codility.com/programmers/task/distinct

def main():
    print(solution([2,1,1,2,3,1])) # 3


def solution(A):

	seen = set()
	for x in xrange(0,len(A)):
		seen.add(A[x])

	return len(seen)


if __name__ == "__main__":
    main()