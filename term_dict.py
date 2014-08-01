afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
	term, score = line.split("\t") # tab delimited
	scores[term] = int(score) #convert the score into an integer
print scores.items() # print every (term,score) pair in the dict
