import hashlib

def main():    
    print(solve("abcdef", "00000")) # 609043
    print(solve("pqrstuv", "00000")) # 1048970
    print(solve("bgvyzdsv", "00000")) # 254575
    print(solve("bgvyzdsv", "000000")) # 1038736

def solve(secretkey, prefix):

    i = 0
    while True:
        m = hashlib.md5()
        m.update(secretkey + str(i))

        hashed = m.hexdigest()

        if hashed.startswith(prefix) :
            return i

        i += 1


if __name__ == "__main__":
    main()
