
file = open('input4.txt', 'r').read().split("\n")

num = 0 

def Check_Words(sentence):
	global num
	sentence = sentence.split(" ")
	# print(sentence)
	for word in sentence:
		if sentence.count(word) > 1:
			num -= 1
			break
		else:
			num += 1
			break
	
for line in file:
	Check_Words(line)

print(f"There are {num} valid passphrases")
