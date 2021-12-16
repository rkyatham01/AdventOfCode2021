
filebeingread = open("day1input.txt", "r")

filehere = filebeingread.readlines()
fileherebeingstripped = [line.rstrip() for line in filehere]


countoftotal = 0

for x in fileherebeingstripped:
   countoftotal = countoftotal + 1

i = 0
j = 1
k = 2
sum1 = 0
sum2 = 0
counter = 0
index = 0

while index < countoftotal-3:
    sum1 = int(fileherebeingstripped[i]) + int(fileherebeingstripped[j]) + int(fileherebeingstripped[k])
    sum2 = int(fileherebeingstripped[i+1]) + int(fileherebeingstripped[j+1]) + int(fileherebeingstripped[k+1])

    if sum2 > sum1:
        counter = counter + 1
    index = index + 1
    i = i + 1
    j = j + 1
    k = k + 1

print(counter)
