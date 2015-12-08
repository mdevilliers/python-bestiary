import hashlib

def main():

    print(has_overlapping_pairs("qjhvhtzxzqqjkmpb")) # True
    print(has_matching_letter_seperated_by_one("qjhvhtzxzqqjkmpb")) #True
    print(solve_part_two("qjhvhtzxzqqjkmpb")) # True

    print(has_overlapping_pairs("xxyxx")) # True
    print(has_matching_letter_seperated_by_one("xxyxx")) # True
    print(solve_part_two("xxyxx")) # True

    print(has_overlapping_pairs("uurcxstgmygtbstg")) # True
    print(has_matching_letter_seperated_by_one("uurcxstgmygtbstg")) # False
    print(solve_part_two("uurcxstgmygtbstg")) # False

    print(has_overlapping_pairs("ieodomkazucvgmuy")) # False
    print(has_matching_letter_seperated_by_one("ieodomkazucvgmuy")) # True
    print(solve_part_two("ieodomkazucvgmuy")) # False

    print(solve_part_one("ugknbfddgicrmopn")) # True
    print(solve_part_one("aaa")) # True
    print(solve_part_one("jchzalrnumimnmhp")) # False
    print(solve_part_one("haegwjzuvuyypxyu")) # False
    print(solve_part_one("dvszwmarrgswjxmb")) # False
    print(iterateFile("05_data.txt", solve_part_one)) # 236
    print(iterateFile("05_data.txt", solve_part_two)) # 50 but wrong


def solve_part_one(somestring):
   # print(somestring, contains_three_vowels(somestring), contains_letter_twice_in_a_row(somestring), does_not_contain_specific_strings(somestring) )
   return contains_three_vowels(somestring) and contains_letter_twice_in_a_row(somestring) and does_not_contain_specific_strings(somestring)

def solve_part_two(somestring):
   # print(somestring, has_overlapping_pairs(somestring), has_matching_letter_seperated_by_one(somestring)  )
   return has_overlapping_pairs(somestring) and has_matching_letter_seperated_by_one(somestring) 


def has_matching_letter_seperated_by_one(somestring):

    previous = somestring[0]

    for x in xrange(2,len(somestring)):
        current = somestring[x]

        if previous == current :
            # print(somestring, previous, current)
            return True

        previous = somestring[x-1]

    # print("no matching",somestring)
    return False


def has_overlapping_pairs(somestring):

    found = {}

    previous = somestring[0]

    for x in xrange(1,len(somestring)):
        current = somestring[x]        
        key = previous + current

        if key in found :
            arr = found[key]
            arr.append(x)
        else :
            found[key] = [x]

        previous = current

    predicated = { k: v for k, v in found.iteritems() if len(v) > 1 }

    for key, value in predicated.iteritems():

        if len(value) > 3: 
            # print(key,value)
            return True
        if value[1] - value[0] > 1:
            # print(key,value)
            return True

    return False

def contains_three_vowels(somestring):

    count = 0

    for x in xrange(0,len(somestring)):

        current = somestring[x]

        if current == "a" or current == "e" or current == "i" or current == "o" or current == "u" :
            count += 1
    
    return count >= 3

def contains_letter_twice_in_a_row(somestring):

    previous = somestring[0]

    for x in xrange(1,len(somestring)):

        current = somestring[x]
       
        if previous == current :
            return True

        previous = current

    return False

def does_not_contain_specific_strings(somestring):

    if "ab" in somestring:
        return False
    if "cd" in somestring:
        return False
    if "pq" in somestring:
        return False        
    if "xy" in somestring:
        return False

    return True

def iterateFile(filename, func):
    
    total = 0 

    with open(filename) as f:
        for line in f:
            if func(line.strip()) :
                total += 1

    return total

if __name__ == "__main__":
    main()
