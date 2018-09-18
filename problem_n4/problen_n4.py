
file = open('input4.txt', 'r').read().split("\n")

sum_of_valids = 0 

def Check_Words(sentence):
	global sum_of_valids
	sentence = sentence.split(" ")
	# print(sentence)
	for word in sentence:
		if sentence.count(word) > 1:
			sum_of_valids -= 1
			break
		else:
			sum_of_valids += 1
			break
	
for line in file:
	Check_Words(line)

print(f"There are {sum_of_valids} valid passphrases")
