
def main():
    
    print(solve(">")) # 2
    print(solve("^>v<")) # 4
    print(solve("^v^v^v^v^v")) # 2
    print(load_from_file("03_data.txt", solve)) # 2592
    print(solve_with_robot("^v")) # 3
    print(solve_with_robot("^>v<")) # 3
    print(solve_with_robot("^v^v^v^v^v")) # 11
    print(load_from_file("03_data.txt", solve_with_robot)) # 2360

def solve(directions):

    current_x = 0
    current_y = 0
    visited = {get_key(0,0): 1}

    for x in xrange(0,len(directions)):

        current_x, current_y = move(current_x, current_y, directions[x])

        key = get_key(current_x, current_y)

        if key in visited :
            visited[key] += 1
        else : 
            visited[key] = 1

    return houses_visited_twice(visited)

def solve_with_robot(directions) :

    santa_x = 0 
    santa_y = 0
    robo_x = 0
    robo_y = 0

    visited = {get_key(0,0): 1}
    
    for x in xrange(0,len(directions)):
        if x % 2 == 0 :
            santa_x, santa_y = move(santa_x, santa_y, directions[x])
            key = get_key(santa_x, santa_y)
        else :
            robo_x, robo_y = move(robo_x, robo_y, directions[x])
            key = get_key(robo_x, robo_y)

        if key in visited :
            visited[key] += 1
        else : 
            visited[key] = 1

    return houses_visited_twice(visited)

def get_key(x,y) :
    return  "{0}{1}".format(x, y)

def houses_visited_twice(hash_of_visited) :
    predicated = { k: v for k, v in hash_of_visited.iteritems() if v > 0 }
    return len(predicated)    

def move(current_x, current_y, direction) :

    if direction == "<" :
        current_x = current_x - 1
    if direction == ">" :
        current_x = current_x + 1
    if direction == "^" :
        current_y = current_y + 1
    if direction == "v" :
        current_y = current_y - 1

    return current_x, current_y

def load_from_file(filename, func):
    with open(filename) as f:
        data = f.read().strip()
        return func(data)


if __name__ == "__main__":
    main()
