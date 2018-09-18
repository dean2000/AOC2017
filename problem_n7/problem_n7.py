import string

file = open('data.txt', 'r').read().split('\n')

dict = {}
list_of_p = []

for word in file:
	list_of_p.append(word[0:word.find('(')-1])
	if (word.find('->') != -1):
		dict[word[0:word.find('(')-1]] \
		 = word[word.find('>')+1::].split(",")

b = ''
for l in list_of_p:
	b += (l)
	b += (" ")
b = (b.split(" "))	

list1 = []
list2 = []

for list in (dict.values()):
	for name1 in list:
		list2.append(name1[1::])

for name in b:
	list1.append(name)

# print(set(list1) & set(list2))
print(dict)

