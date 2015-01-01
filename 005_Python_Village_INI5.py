f = open("Data/rosalind_ini5.txt", "r")
output = open("Output/005_INI5.txt", "w")
i = 1

for line in f.readlines():
	if i % 2 == 0:
		output.write(line)
	i = i + 1
	

