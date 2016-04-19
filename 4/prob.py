stopwords = []
sm = []
f2 = open('stopwords.txt', 'r')
f1=open('wsw.txt', 'r')
f3=open('vocap.txt', 'a')
f4=open('vocan.txt', 'a')
list1=[]
list2=[]
list3=[]
list0=[]
cp=0
cn=0
for line in f1:
	for word in line.split():
		if line.split(None, 1)[0] == '+':
				word=word.strip()
				if word in list1:
					list2[list1.index(word)]+=1
					cp=cp+1
				else:
					list1.append(word)
					list2.append(1)
					cp=cp+1
f1.close()
f1=open('wsw.txt', 'r')
for line in f1:
	for word in line.split():
		if line.split(None, 1)[0] == '-':
				word=word.strip()
				if word in list0:
					list3[list0.index(word)]+=1
					cn=cn+1
				else:
					list0.append(word)
					list3.append(1)
					cn=cn+1

s = raw_input("Enter a review");

for line in f2: 
	w1 = line.split()
	for word in w1:
		stopwords.append(word)

for word in s.split():
	if word not in stopwords:
		sm.append(word)

print sm

for item in sm:
	