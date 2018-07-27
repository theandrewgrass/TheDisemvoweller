class Disemvoweller:
	
	def __init__(self, unluckyString):
		self.unluckyString = unluckyString
		
	def removeVowels(self):
		i = 0
		vowels = ['a', 'e', 'i', 'o', 'u', ' ']
		self.weepers = [] #list that holds the removed vowels
		
		while i < len(self.unluckyString):
			if self.unluckyString[i] in vowels:
				if self.unluckyString[i] != ' ':
					self.weepers.append(self.unluckyString[i]) #add non-whitespace unwanted chars
				self.unluckyString = self.unluckyString[:i] + self.unluckyString[i+1:] #string without unwanted char
			else:
				i += 1

	def printDisemvowelled(self):
		print(self.unluckyString, end=" ")
		print(''.join(str(losers) for losers in self.weepers)) #output vowels removed with no whitespace 

def runDisemvoweller():
	unluckyString = input("Enter string to be disemvowelled: ")

	if unluckyString == "quit": #if quit entered as string, exit program
		exit()
	
	devStr = Disemvoweller(unluckyString)
	devStr.removeVowels()
	devStr.printDisemvowelled()

while True:
	runDisemvoweller()
