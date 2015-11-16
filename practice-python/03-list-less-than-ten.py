
# write a program that prints out all the elements of the list that are less than 5.
def main():
    
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	predicated = [x for x in a if x < 5]
	print (predicated)


if __name__ == "__main__":
    main()