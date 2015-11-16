
# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

def main():
    
    number = raw_input("Give me a number: ")
    number = int(number)

    if number % 2 == 0 :
        print ("Even")
    else:
        print ("Odd") 

if __name__ == "__main__":
    main()
