#ECE2524 Project3
#Hangman Game
#Jisu Park

#instruction
print " "
print "Hangman Game!!"
print "Guess the correct word in 10 tries"

#variables
tries = 10
words = ["pineapple", "banana", "strawberry", "watermelon", "blueberry",
	 "pear", "orange", "cherry", "pomegranate", "cantaloupe"]
import random
randNum = random.randint(0,9)
myWord = list(words[randNum])
count = len(myWord)
correctGuess = 0
answer = ['_'] * count

while(tries > 0):
	print " "
	print "Tries Left: %d" % tries
	print ' '.join(answer)
	print " "
	guess = raw_input("Guess: ")

	correct = False
	for i in range(0, count-1):
		if guess == myWord[i]:
			answer[i] = guess
			correctGuess = correctGuess + 1		
			correct = True
	#check whether correct letter was guessed 
	if correct == True:
		print "Correct Guess :)"
		print " "
	else: 
		tries = tries - 1
		print "Incorrect Guess :("
		print " "
	#check whether correct word was guessed
	if correctGuess == count: 
		tries = -1

#print results
if tries == 0:
	print " "
	print " "
	print "YOU LOST :( THE ANSWER WAS %s" % myWord
elif tries == -1:
	print " "
	print " "
	print "CONGRATULATIONS :) YOU GUESSED THE CORRECT ANSWER"







