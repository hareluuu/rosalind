with open("Data/rosalind_ini2.txt") as input_data:
	a, b = map(int, input_data.read().strip().split())
	
	

c = (a*a) + (b*b)
print(c)

with open("Output/001_INI2.txt", "w") as output_data:
		output_data.write(str(c))
