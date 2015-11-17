from random import shuffle

def main():
   
	players = [	{ 'name' : "Mark" },
				{ 'name' : "Kate"},
				{ 'name' : "Neil" },
				{ 'name' : "Debs"},
				{ 'name' : "Richard"},
				{ 'name' : "Gerry"},
				{ 'name' : "Joe" }, 
				{ 'name' : "Katie"}]

	shuffle(players)

	couples = []
	for l in xrange(0,len(players) - 1, 2):
		couples.append( (players[l], players[l+1]) )

	for x in xrange(0, len(couples)):
		pair = couples[x]
		print( "{0} will buy for {1}".format(pair[0]['name'],pair[1]['name']) )


if __name__ == "__main__":
    main()
