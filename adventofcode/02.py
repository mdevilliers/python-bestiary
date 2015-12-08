
def main():
    l,w,h = parse("2x3x4")
    print(surface_area(l,w,h)) # 52

    l,w,h = parse("1x1x10")    
    print(surface_area(l,w,h)) # 42

    print(iterateFile("02_data.txt", surface_area)) # 1586300
    
    l,w,h = parse("2x3x4")
    print(calculate_ribbon(l,w,h)) # 34

    l,w,h = parse("1x1x10")
    print(calculate_ribbon(l,w,h)) # 14

    print(iterateFile("02_data.txt", calculate_ribbon)) # 3737498

def parse(string) :
    return [int(x) for x in string.split("x")] 

def surface_area(l,w,h):
    return  (2 * l * w) + (2 * w * h) + (2 * h * l)    

def calculate_wrapping(l,w,h):
    smallest, small, _ = sorted([l,w,h])
    wrapping = surface_area(l,w,h)
    return wrapping + (smallest * small)

def calculate_ribbon(l,w,h):
    smallest, small, biggest = sorted([l,w,h])
    return 2 *(smallest + small) + (l*w*h)

def iterateFile(filename, func):
    
    total = 0 
    with open(filename) as f:
        for line in f:
            l,w,h = parse(line.strip())
            # total += calculate_wrapping(l,w,h)
            total += func(l,w,h)

    return total


if __name__ == "__main__":
    main()
