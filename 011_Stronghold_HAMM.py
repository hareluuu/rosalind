a = "GAGCCTACTAACGGGAT"
b = "CATCGTAATGACGGCCT"

count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        count += 1
    else:
        continue
print(count)