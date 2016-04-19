from nltk.util import ngrams

import nltk

f1=open('wsw.txt', 'r')
f2=open('posonly.txt', 'w')
f3=open('negonly.txt', 'w')

for line in f1:

	if line.split(None, 1)[0] == '+':
		s=line.split(' ',1)[1]
		f2.write(s)

f1.close()

f1=open('wsw.txt', 'r')

for line in f1:

	if line.split(None, 1)[0] == '-':
		s=line.split(' ',1)[1]
		f3.write(s)

f2.close()
f3.close()

f2=open('posonly.txt', 'r')
f3=open('negonly.txt', 'r')
f4=open('posonly1.txt', 'w')
f5=open('negonly1.txt', 'w')
bgs=[]

for line in f2:
	sentence = line
	n = 2
	bigrams = ngrams(sentence.split(), n)
	bgs.extend(bigrams)
fdist=nltk.FreqDist(bgs)
for i,j in fdist.items():
	if j>=2:
		f4.write(i[0])
		f4.write(" ")
		f4.write(i[1])
		f4.write(" ")
		f4.write(str(j))
		f4.write("\n")

bgs=[]

for line in f3:
	sentence = line
	n = 2
	bigrams = ngrams(sentence.split(), n)
	bgs.extend(bigrams)
fdist=nltk.FreqDist(bgs)
for i,j in fdist.items():
	if j>=2:
		f5.write(i[0])
		f5.write(" ")
		f5.write(i[1])
		f5.write(" ")
		f5.write(str(j))
		f5.write("\n")

