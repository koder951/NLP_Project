stopwords = []
f1 = open('stopwords.txt', 'r')
f2 = open('data.txt', 'r+')
f3 = open('wswtmp.txt', 'a+')
f4 = open('wsw.txt', 'a+')

for line in f1: 
	w1 = line.split()
	for word in w1:
		stopwords.append(word)

import re
regex = re.compile('[^a-zA-Z+-]')
for line in f2:
	if line.strip():
		w2 = line.split()
		for word in w2:
			word = regex.sub(' ', word)
			if word.lower() not in stopwords:
				f3.write(word.lower() + ' ')
		f3.write('\n')
f3.close()
f3 = open('wswtmp.txt', 'r+')

for line in f3:
	w3 = line.split()
	for word in w3:
		if word.lower() not in stopwords:
			f4.write(word.lower() + ' ')
	f4.write('\n')	

f1.close()
f2.close()
f4.close()
