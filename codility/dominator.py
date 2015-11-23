# https://codility.com/programmers/task/dominator

# from math import ceil

def main():
    print(solution([3,4,3,2,3,-1,3,3])) # 0 OR 2 OR 4 OR 6 OR 7

def solution(A):
    
    more_than_half = len(A) / 2
    found = {}
    found_index = {}
    
    for x in xrange(0,len(A)):
        i = A[x]
        
        if i in found :
            found[i] += 1
        else :
            found[i] = 0
            found_index[i] = x
     
    max_key = max(found, key=found.get)
    
    if found.get(max_key) >= more_than_half :
        return found_index.get(max_key)
    else :
        return -1
    
    

if __name__ == "__main__":
    main()
