#ECE2524 Project3
#Hangman Game
#Jisu Park

#instruction
print "Hangman Game!!"
print "Guess the correct word in 10 tries"
print " "

#variables
tries = 10
words = ["pineapple", "banana", "strawberry", "watermelon", "blueberry",
	 "pear", "orange", "cherry", "pomegranate", "cantaloupe"]
import random
randNum = random.randint(0,9)
myWord = words[randNum]
count = len(myWord)
answer = ['_'] * count

while(tries > 0):
	print "Tries: %d" % tries
	print ' '.join(answer)

