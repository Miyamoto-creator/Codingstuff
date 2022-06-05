letterSortByFrequency = "abcdefghijklmnopqrstuvwxyz"
primeNumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
letterToPrime = {}
for i in range(len(primeNumber)):   # Create a map form letter to prime number, based on the frquency of each letter appear in english word
  letterToPrime[letterSortByFrequency[i]] = primeNumber[i]

hashValue = 1
for i in 'SUNILz'.lower():
  print(i)
  if i in letterToPrime:
    hashValue *= letterToPrime[i]
  print(hashValue)


# correctWord = {}
# input_file = open('wordsEn.txt')   #read the english word list from file
# for line in input_file:
# 	line = line.rstrip('\n') #ignore the '\n' in the file
# 	line = line.rstrip('\r')
# 	if len(line)>=5 and len(line)<=7:
# 		hashValue = 1
# 		for letter in line:       # compute the hash value of each word(multiple all the prime number of each letter) the anagram has the same hash value with the correct word
# 			if letter in letterToPrime:
# 				hashValue *= letterToPrime[letter]
# 		correctWord[hashValue] = line	# Add it to a hashtable
#
# def check(word, hashtable, Prime):      #Computer the anagram's hashvalue then find the correct word in the hashtable
# 	hashV = 1
# 	for letter in word:
# 		if letter in Prime:
# 			hashV *= Prime[letter]
# 	if hashV in hashtable:
# 		return hashtable[hashV]
# 	else:
# 		return False
#
# def test():
# 	if not (check("pplea", correctWord, letterToPrime) == "apple"):
# 		print "Test not pass!"
# 		return
# 	if not (check("ythitr", correctWord, letterToPrime) == "thirty"):
# 		print "Test not pass!"
# 		return
# 	print "Test pass!"

# test()