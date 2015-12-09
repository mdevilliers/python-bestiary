# turn on 489,959 through 759,964

def main():
    # ( (turn on/off) / toggle) n,n through n,n 
    # print(parse("turn on 489,959 through 759,964"))
    # print(parse("turn off 489,959 through 759,964"))
    # print(parse("toggle 489,959 through 759,964"))

    # board = create_board(10,10)
    # toggle(board,0,0,5,5) # first quadrent
    # debug_board(board)
    # print(count_lights_on(board)) 
    # on(board,5,5,9,9) # last quadrent
    # debug_board(board)
    # print(count_lights_on(board)) 
    # off(board, 4,4,5,5) # turn of four midddle
    # debug_board(board)
    # print(count_lights_on(board)) 
    # off(board,0,0,9,0) # swith off first row
    # debug_board(board)
    # print(count_lights_on(board)) 
    print(iterateFile_part1("06_data.txt")) # 569999
    print(iterateFile_part2("06_data.txt")) # 17836115

def do(board, startx, starty, endx, endy, func) :
    length = len(board[0])
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            board[x][y] = func(board[x][y])

def create_board(length = 1000, height = 1000, value=False) :
    return [[value] * length for n in range(height)]

def parse(command) :

    bits = command.split()

    if bits[1] == "on" :
        start = parse_coords(bits[2])
        end = parse_coords(bits[4])
        return "on", start, end
    if bits[1] == "off" :
        start = parse_coords(bits[2])
        end = parse_coords(bits[4])
        return "off", start, end
    if  bits[0] == "toggle" :
        start = parse_coords(bits[1])
        end = parse_coords(bits[3])
        return "toggle", start, end

def parse_coords(coords_str):
    return[int(x) for x in coords_str.split(",")]

def iterateFile_part1(filename):
    
    board = create_board()

    with open(filename) as f:
        for line in f:
            command, start, end = parse(line.strip())
            print(command, start, end)
            if command == "on" :
                do(board, start[0], start[1], end[0], end[1],lambda x: True )
            if command == "off" :
                do(board, start[0], start[1], end[0], end[1],lambda x: False)
            if command == "toggle" :
                do(board, start[0], start[1], end[0], end[1],lambda x: False if x else True )

    return count_lights_on(board)

def iterateFile_part2(filename):
    
    board = create_board(value=0)

    with open(filename) as f:
        for line in f:
            command, start, end = parse(line.strip())
            print(command, start, end)
            if command == "on" :
                do(board, start[0], start[1], end[0], end[1],lambda x: x + 1 )
            if command == "off" :
                do(board, start[0], start[1], end[0], end[1],lambda x: max(x - 1, 0))
            if command == "toggle" :
                do(board, start[0], start[1], end[0], end[1],lambda x: x + 2 )

    return count_brightness(board)

def count_lights_on(board) :
    count = 0
    length = len(board[0])
    for x in xrange(length):
        for y in xrange(length):      
          count += 1 if board[x][y] == True else 0
    return count

def count_brightness(board) :
    count = 0
    length = len(board[0])
    for x in xrange(length):
        for y in xrange(length):      
          count += board[x][y]
    return count

def debug_board(board) :
    length = len(board[0])
    for x in xrange(0,length):
        for y in xrange(0,length):      
          print(1 if board[x][y] == True else 0),
        print("")

if __name__ == "__main__":
    main()
