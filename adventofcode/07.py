# turn on 489,959 through 759,964

def main():

    print(iterateFile_part1("07_data.txt")) 
    # print(iterateFile_part2("06_data.txt"))

assignments = []
operations =[]

def parse(command) :

    # 123 -> x        means that the signal 123 is provided to wire x.
    # x AND y -> z    means that the bitwise AND of wire x and wire y is provided to wire z.
    # p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    # NOT e -> f      means that the bitwise complement of the value from wire e is provided to wire f.
    # Other possible gates include OR (bitwise OR) and RSHIFT (right-shift)

    bits = command.split()
    # reverse the array
    # [{output}, ->, number]
    # [{output}, ->, {input}, AND, {input}]
    # [{output}, ->, {input2}, OR, {input1}]
    # [{output}, ->, number, LSHIFT, {input}]
    # [{output}, ->, number, RSHIFT, {input}]
    # [{output}, ->, NOT, {input}]
    # bits = bits[::-1] 

    if len(bits) == 3 :
        # its an assignment
        assignments.append(command)
    else :

        replaced = command.replace('AND', '&').replace('OR', '|').replace('NOT ', '~').replace('RSHIFT', '>>').replace('LSHIFT', '<<')
        operations.append(replaced)

def iterateFile_part1(filename):
    
    with open(filename) as f:
        for line in f:
            parse(line.strip())

    print(assignments)
    print(operations)

if __name__ == "__main__":
    main()
