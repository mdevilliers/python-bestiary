# https://codility.com/programmers/task/brackets

def main():
    print(solution("{[()()]}")) # 1
    print(solution("([)()]")) # 0

def solution(A):
    
    stack = []
    
    for c in A:
        
        if len(stack) == 0 :
            stack.append(c)
        else :
            peek = stack.pop()
            
            if peek == "(" and c == ")" :
                continue
            elif peek == "{" and c == "}" :
                continue
            elif peek == "[" and c == "]" :
                continue
            else :
                stack.append(peek)
                stack.append(c)
     
    if len(stack) == 0 :
        return 1
     
    return 0

if __name__ == "__main__":
    main()
