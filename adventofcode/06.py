# turn on 489,959 through 759,964

def main():
    # ( (turn on/off) / toggle) n,n through n,n 
    # print(parse("turn on 489,959 through 759,964"))
    # print(parse("turn off 489,959 through 759,964"))
    # print(parse("toggle 489,959 through 759,964"))
    
    # print(board)
    # # toggle(board,0,0,10,10) # all on
    # # print(board)
    board = create_board(10,10)
    toggle(board,0,0,5,5) # first quadrent
    debug_board(board,10,10)
    print(count_lights_on(board)) # 25
    on(board,5,5,10,10) # last quadrent
    debug_board(board,10,10)
    print(count_lights_on(board)) # 50
    off(board, 4,4,6,6) # turn of four midddle
    debug_board(board,10,10)
    print(count_lights_on(board)) # 48
    off(board,0,0,10,0) # swith off first row
    debug_board(board,10,10)
    # print(iterateFile("06_data.txt"))

def debug_board(board, length=1000, height=1000) :
    for x in xrange(0,length):
        for y in xrange(0,height):
          key = get_key(x,y)         
          print(board[key]),
        print("")

def get_key(x,y) :
    return "{0}{1}".format(x,y)

def toggle(board, startx, starty, endx, endy) :    
    points = [ (x,y) for x in xrange(startx,endx) for y in xrange(starty,endy)]
    for x in xrange(0, len(points)):
        key = get_key(points[x][0],points[x][1])
        board[key] = 0 if board[key] == 1 else 1

def on(board, startx, starty, endx, endy) :    
    points = [ (x,y) for x in xrange(startx,endx) for y in xrange(starty,endy)]
    set_positions(board,points,1)

def off(board, startx, starty, endx, endy) :    
    points = [ (x,y) for x in xrange(startx,endx) for y in xrange(starty,endy)]
    set_positions(board,points,0)

def set_positions(board, points, value) :
    for x in xrange(0, len(points)):
        key = get_key(points[x][0],points[x][1])
        board[key] = value

def create_board(length = 1000, height = 1000) :

    arr = {}

    for x in xrange(0,length):
        for y in xrange(0,height):
          key = get_key(x,y)         
          arr[key] = 0

    return arr

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

def iterateFile(filename):
    
    board = create_board(999,999)

    with open(filename) as f:
        for line in f:
            command, start, end = parse(line.strip())
            print(command, start, end)
            if command == "on" :
                on(board, start[0], start[1], end[0], end[1])
            if command == "off" :
                off(board, start[0], start[1], end[0], end[1])
            if command == "toggle" :
                toggle(board, start[0], start[1], end[0], end[1])

    return count_lights_on(board)

def count_lights_on(board) :
    predicated = { k: v for k, v in board.iteritems() if v == 1 }
    return len(predicated)  

if __name__ == "__main__":
    main()
