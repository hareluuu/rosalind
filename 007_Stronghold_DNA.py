f = open("Data/rosalind_dna.txt", "r").readlines()
s = str(f)
a = 0
b = 0
c = 0
d = 0

for i in s:
    if i == "A":
        a += 1
    elif i == "C":
        b += 1
    elif i == "G":
        c += 1
    elif i == "T":
        d += 1

print(a, b, c, d)
