
def main():
    l,w,h = parse("2x3x4")
    print(surface_area(l,w,h)) # 52

    l,w,h = parse("1x1x10")    
    print(surface_area(l,w,h)) # 42

    print(iterateFile("02_data_1.txt")) # 1586300
    l,w,h = parse("2x3x4")
    print(calculate_ribbon(l,w,h)) # 34

    l,w,h = parse("1x1x10")
    print(calculate_ribbon(l,w,h)) # 14

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

def iterateFile(filename):
    
    total = 0 
    with open(filename) as f:
        for line in f:
            l,w,h = parse(line.strip())
            total += calculate_wrapping(l,w,h)

    return total


if __name__ == "__main__":
    main()
