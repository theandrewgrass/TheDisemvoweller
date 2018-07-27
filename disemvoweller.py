class Disemvoweller(object):
	
	def __init__(self, unluckyString):
		self.unluckyString = unluckyString
		
	def removeVowels(self):
		i = 0
		vowels = ['a', 'e', 'i', 'o', 'u', ' ']
		self.weepers = []
		
		while i < len(self.unluckyString):
			if self.unluckyString[i] in vowels:
				if self.unluckyString[i] != ' ':
					self.weepers.append(self.unluckyString[i])
				self.unluckyString = self.unluckyString[:i] + self.unluckyString[i+1:]
			else:
				i += 1

	def printDisemvowelled(self):
		print(self.unluckyString, end=" ")
		print(''.join(str(losers) for losers in self.weepers))

def runDisemvoweller():
	unluckyString = input("Enter string to be disemvowelled: ")

	if unluckyString == "quit":
		exit()
	
	devStr = Disemvoweller(unluckyString)
	devStr.removeVowels()
	devStr.printDisemvowelled()

while True:
	runDisemvoweller()