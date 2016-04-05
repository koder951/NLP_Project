f1=open('wsw.txt', 'r')
f2=open('voca.txt', 'a')
list1=[]
list2=[]
for line in f1:
	for word in line.split():
		word=word.strip()
		if word in list1:
			list2[list1.index(word)]+=1
		else:
			list1.append(word)
			list2.append(1)

for item in list1:
	if list2[list1.index(item)] >= 2:
		f2.write(item + ' ')
		f2.write("%s" % list2[list1.index(item)])
		f2.write('\n')
