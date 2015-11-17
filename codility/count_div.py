# https://codility.com/programmers/task/count_div
def main():
    print(solution(6,11,2)) # 3

def solution(A,B,K):

    if A % K == 0:  return (B - A) // K + 1
    else:           return (B - (A - A % K )) // K

if __name__ == "__main__":
    main()