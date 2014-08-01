#
# HEADER HERE
#

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
	tweet_file = json.load( open(sys.argv[2]) )

	#Prepare the score dictionary
	scores = {} # initialize an empty dictionary
	prepsentidict(senti_file, scores)
        try:
                tweet_text = tweet_file["text"]
        except (KeyError, UnicodeEncodeError):
                tweet_text = "none"


if __name__ == '__main__':
        main()
