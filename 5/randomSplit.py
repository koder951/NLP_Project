import random
with open('wsw.txt','r') as source:
	data = [ (random.random(), line) for line in source ]
data.sort()
with open('rndm.txt','w') as target:
	for _, line in data:
		target.write( line )

no_of_lines_read = 0
file_no = 1
with open ("rndm.txt","r") as fin:
	for line in fin:
		if no_of_lines_read> 459:
			with open ("file10.txt", "a") as fout10:
				fout10.write(line)
		elif no_of_lines_read > 408:
			with open ("file9.txt", "a") as fout9:
				fout9.write(line)
		elif no_of_lines_read > 357:
			with open ("file8.txt", "a") as fout8:
				fout8.write(line)
		elif no_of_lines_read > 306:
			with open ("file7.txt", "a") as fout7:
				fout7.write(line)
		elif no_of_lines_read > 255:
			with open ("file6.txt", "a") as fout6:
				fout6.write(line)
		elif no_of_lines_read > 204:
			with open ("file5.txt", "a") as fout5:
				fout5.write(line)
		elif no_of_lines_read > 153:
			with open ("file4.txt", "a") as fout4:
				fout4.write(line)
		elif no_of_lines_read > 102:
			with open ("file3.txt", "a") as fout3:
				fout3.write(line)
		elif no_of_lines_read >=51:
			with open ("file2.txt", "a") as fout2:
				fout2.write(line)
		else:
			with open ("file1.txt", "a") as fout1:
				fout1.write(line)
		no_of_lines_read+=1
