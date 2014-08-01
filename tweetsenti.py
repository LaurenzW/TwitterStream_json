import sys
import json




#Prepare dict for senti scores
def prepsentidict(senti_file, sentiscores):
	for line in senti_file:
		term, score = line.split("\t")  #The file is tab-delimited. "\t" means "tab character"
		sentiscores[term] = int(score) #Convert the score to an integer


def main():
	#open the files AFNNI-111 and the twitterexport
	senti_file = open(sys.argv[1])
	tweet_file = open(sys.argv[1])
	#lines(senti_file)
	#lines(tweet_file)

	#Prepare the score dictionary
	scores = {} # initialize an empty dictionary
	prepsentidict(senti_file, scores)
	#print scores.items() # Print every (term, score) pair in the dictionary
	#python dictionary for tweets from output.txt
	##tweets={}
	#run through each tweet to calculate the total senti score
	##for item in tweets:
	##	tweets = json.loads(item)
	##	print tweets
	##	print type(tweets)
##print tweets	
try:	
	tweets={}
	with tweet_file:
		for line in tweet_file:
			tweets = json.loads(line)
	tweettext = tweets["text"].encode(#utf-8').lower()
except (KeyError, UnicodeEncodeError):
	tweettext = none

if __name__ == '__main__':
   main()
