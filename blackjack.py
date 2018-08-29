import random
import time
import sys

sys.setrecursionlimit(2147000)

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
deck = deck * 24 #times 24 for six decks
playerHand = []
dealerHand = []
playerValue = 0
dealerValue = 0
playerSoft = 0
dealerSoft = 0
wins = 0
loses = 0
draws = 0
hands = 100
hands2 = 100
def setDefaults():
	global playerHand
	global dealerHand
	global playerSoft
	global dealerSoft
	global playerValue
	global dealerValue
	global deck
	global hands
	if hands > 0:
		if (len(deck)) < 10:
			del(deck)
			deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
			deck = deck * 24
		del(playerHand)
		del(dealerHand)
		playerHand = []
		dealerHand = []
		playerValue = 0
		dealerValue = 0
		playerSoft = 0
		dealerSoft = 0
		hands = hands - 1
		dealHand()
	else:
		showResults()

def dealHand():
	random.shuffle(deck)
	playerHand.append(deck.pop())
	dealerHand.append(deck.pop())
	playerHand.append(deck.pop())
	dealerHand.append(deck.pop())
	checkBlackjack()

def checkBlackjack():
	if playerHand[0] == 1 and playerHand[1] == 10 or playerHand[0] == 10 and playerHand[0] == 1:
		doBlackjack("dealer")
	elif dealerHand[0] == 1 and dealerHand[1] == 10 or dealerHand[0] == 10 and dealerHand[0] == 1:
		doBlackjack("player")
	else:
		valueHands("player")

def valueHands(person):
	global playerValue
	global dealerValue
	global playerSoft
	global dealerSoft

	if person == "player":
		for x in range(len(playerHand)):
			if playerHand[x] == 1:
				playerHand[x] = 11
				playerSoft = 1
			playerValue = playerValue + playerHand[x]
		if playerValue > 21:
			if playerSoft == 1:
				playerValue = playerValue - 10
				playerSoft = 0
				determineMovePlayer()
			else:
				doBust("player")
		else:
			determineMovePlayer()
	if person == "dealer":
		for x in range(len(dealerHand)):
			if dealerHand[x] == 1:
				dealerHand[x] = 11
				dealerSoft = 1
			dealerValue = dealerValue + dealerHand[x]
		if dealerValue > 21:
			if dealerSoft == 1:
				dealerValue = dealerValue - 10
				dealerSoft = 0
				determineMoveDealer()
			else:
				doBust("dealer")
		else:
			determineMoveDealer()

def determineMovePlayer():
	if playerSoft == 0:
		if playerValue > 16:
			standPlayer()
		if playerValue == 16:
			if dealerHand[0] < 7 and dealerHand[0] != 1:
				standPlayer()			
			else:
				hitCard("player")
		if playerValue == 15:
			if dealerHand[0] < 7 and dealerHand[0] != 1:
				standPlayer()			
			else:
				hitCard("player")
		if playerValue == 14:
			if dealerHand[0] < 7 and dealerHand[0] != 1:
				standPlayer()			
			else:
				hitCard("player")
		if playerValue == 13:
			if dealerHand[0] < 7 and dealerHand[0] != 1:
				standPlayer()			
			else:
				hitCard("player")
		if playerValue == 12:
			if dealerHand[0] > 3 and dealerHand[0] < 7:
				standPlayer()
			else:
				hitCard("player")
		if playerValue < 12:
			hitCard("player")
	else:
		if playerValue == 19 or playerValue == 20 or playerValue == 21:
			standPlayer()
		if playerValue == 18:
			if dealerHand[0] > 8 or dealerHand[0] == 1:
				hitCard("player")
			else:
				standPlayer()
		if playerValue < 18:
			hitCard("player")

def standPlayer():
	valueHands("dealer")

def determineMoveDealer():
	if dealerSoft == 0:
		if dealerValue > 16 and dealerValue < 22:
			standDealer()
		else:
			hitCard("dealer")
	else:
		if dealerValue > 16 and dealerValue < 22:
			standDealer()
		elif dealerValue > 21:
			doBust("dealer")
		else:
			hitCard("dealer")

def standDealer(): 
	doShowdown()

def hitCard(person):
	if person == "player":
		playerHand.append(deck.pop())
		valueHands("player")
	if person == "dealer":
		dealerHand.append(deck.pop())
		valueHands("dealer")

def doShowdown():
	global wins
	global loses
	global draws
	if playerValue > dealerValue:
		wins = wins + 1
	elif playerValue == dealerValue:
		draws = draws + 1
	else:
		loses = loses + 1
	setDefaults()

def doBust(person):
	global wins
	global loses
	if person == "player":
		loses = loses + 1
	else:
		wins = wins + 1
	setDefaults()

def doBlackjack(person):
	global wins
	global loses
	if person == "player":
		loses = loses + 1
	else:
		wins = wins + 1
	setDefaults()

def showResults():
	global hands2
	print("Wins: " + str((wins/hands2)*100) + "%")
	print("Losses: " + str((loses/hands2)*100) + "%")
	print("Draws: " + str((draws/hands2)*100) + "%")
	time.sleep(20)
dealHand()
