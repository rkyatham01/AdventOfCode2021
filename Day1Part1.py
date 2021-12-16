

filebeingread = open("day1input.txt", "r")


countshere = 0

filehere = filebeingread.readlines()
fileherestripped = [line.rstrip() for line in filehere]

countoftotal = 0
index = 0
for x in fileherestripped:
   countoftotal = countoftotal + 1

j = 1
i = 0

while i < countoftotal-1:
    if int(fileherestripped[j]) > int(fileherestripped[i]):
       countshere = countshere + 1
    i = i + 1
    j = j + 1

print(countshere)








