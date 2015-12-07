#ECE2524 Project3
#Hangman Game
#Jisu Park
#December 2015


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
guessedLetters = [' '] * 26
countGuess = 0

while(tries > 0):
	print " "
	print "Tries Left: %d" % tries
	print ' '.join(answer)
	print " "
	guess = raw_input("Guess: ")

	#check whether guess is a proper input (single alphabet)
	if((guess.isalpha() != True) or (len(guess) != 1)):
		tries = tries - 1 
		print "Improper Guess: make sure that your guess is one letter alphabet :("
	else:
		guess = guess.lower()

		#check whether new letter was guessed
		guessed = False
		for i in range (0, 25):
			if guess == guessedLetters[i]:
				guessed = True
		if guessed == True:
			tries = tries - 1
			print "This letter was already guessed :("
		else:
			guessedLetters[countGuess] = guess
			countGuess = countGuess + 1
	
			correct = False
			for i in range(0, count):
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
	print "YOU LOST :( The answer was %s" % ''.join(myWord)
	print " "
	print " "
elif tries == -1:
	print " "
	print " "
	print "CONGRATULATIONS :) YOU GUESSED THE CORRECT ANSWER"
	print " "
	print " "






