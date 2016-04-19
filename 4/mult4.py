import pickle

f1=open('wsw.txt', 'r')
f3=open('vocap.txt', 'w')
f4=open('vocan.txt', 'w')
list1=[]
list2=[]
list3=[]
list0=[]
cp=0
cn=0
vp=0
vn=0

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
	
cp=cp-255
cn=cn-255

PosList=[]
NegList=[]

for item in list1:
	if list2[list1.index(item)] >= 2:
		vp=vp+1

for item in list0:
	if list3[list0.index(item)] >= 2:
		vn=vn+1

for item in list1:
	if list2[list1.index(item)] >= 2:
		f3.write(item + ' ')
		x=list2[list1.index(item)]
		y=(float(x)+1)/(cp+vp+1)
		f3.write("%f" % y )
		f3.write('\n')
		PosList.append("Word: %s PosProbability: %f" %(item,y))

for item in list0:
	if list3[list0.index(item)] >= 2:
		f4.write(item + ' ')
		x=list3[list0.index(item)]
		y=(float(x)+1)/(cn+vn+1)
		f4.write("%f" % y)
		f4.write('\n')
		NegList.append("Word: %s NegProbability: %f" %(item,y))

file_name= "MultinomialNBP"
file_pos=open(file_name,'wb')
file_name= "MultinomialNBN"
file_neg=open(file_name,'wb')
pickle.dump(PosList,file_pos)
pickle.dump(NegList,file_neg)
file_pos.close()
file_neg.close()

vnotp=float(1)/cp
vnotn=float(1)/cn

f3.close()
f4.close()


stopwords = []
sm = []
f2 = open('stopwords.txt', 'r')

s = raw_input("Enter a review");

for line in f2: 
	w1 = line.split()
	for word in w1:
		stopwords.append(word)

for word in s.split():
	if word not in stopwords:
		sm.append(word)

pp=1

def counting(item):
	prob=-1
	f3=open('vocap.txt', 'r')
	for line in f3:
		if item in line.split():
			 prob=float(line.split()[1])
	return prob




for item in sm:
	x=counting(item)
	if(x==-1):
		x=vnotp

	print x

	pp=pp*x

print float(pp)


np=1

def counting2(item):
	prob=-1
	f6=open('vocan.txt', 'r')
	for line in f6:
		if item in line.split():
			 prob=float(line.split()[1])
	return prob




for item in sm:
	x=counting2(item)
	if(x==-1):
		x=vnotn

	print x

	np=np*x

print float(np)

if float(pp)>float(np):
	print "It is positive"
else:
	print "It is negative"

#	if item in line.split():
#			 prob=float(line.split()[1])
#			 pp=pp*prob
#		else:
#			pp=pp*vnotp
