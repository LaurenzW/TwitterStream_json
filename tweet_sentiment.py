import sys
import json

def prepsentidict(senti_file, sentiscores):
	for line in senti_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		sentiscores[term] = int(score)  # Convert the score to an integer.

def count_positives(scores, words):
	positives = 0
	for word in words:
		if(word in scores and scores[word] > 0):
			positives += 1
	return positives

def count_negatives(scores, words):
	negatives = 0
	for word in words:
		if(word in scores and scores[word] < 0):
			negatives += 1
	return negatives	
	
def nonexistent_term_score(scores, words, positives, negatives):
	score = 0
	for word in words:
		## identify the word that do not have a score yet
		if(word not in scores and len(word) > 1 and word.isalnum()):
			if(negatives > 0 or negatives < 0):
				score = positives / negatives
			else:
				score = positives
			if score > 0 or score < 0:
				print word.encode('utf-8'), " ", score
				print score
	
def main():
	## Open the files
	senti_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2]) 
	
	## Prepare the scores dictionary
	scores = {} # initialize an empty dictionary
	prepsentidict(senti_file, scores)
	#print scores.items() # Print every (term, score) pair in the dictionary
	
	#python dictionary for the tweets from output.txt
	tweets={}
	i = 0
	#run through each tweet to calculate the total senti score
	for line in tweet_file:
		tweets[i] = json.loads(line)
		# Calculate the score
		if("text" in tweets[i]):
			text = tweets[i]["text"]
			words = text.split(" ")
			p = count_positives(scores, words)
			n = count_negatives(scores, words)
			nonexistent_term_score(scores, words, p, n)
		i += 1


if __name__ == '__main__':
    main()
