# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

def main():
    name = raw_input("Give me your name: ")
    age = raw_input("Give me your age: ")
    age = int(age)

    current_year = 2015
    age_at_100 = (100 - age) + current_year

    print(name + " will by 100 years old on " + str(age_at_100)) 

if __name__ == "__main__":
	main()
