

filebeingread = open("day3input.txt", "r")

filehere = filebeingread.readlines()

fileheregettingstripped = [line.rstrip() for line in filehere]

countoftotal = 0

for x in fileheregettingstripped:
   countoftotal = countoftotal + 1
   #countoftotal has the # of total lines read of file

k = 0
countofbinary = 0
for x in fileheregettingstripped[0]:
    k = k + 1
k = k - 1
m = k

i = 0
j = 0
comp1 = 0
comp2 = 0
b = 0
l = k

sumofgammarate = 0

while i < k + 1:
    while b < countoftotal:
        if fileheregettingstripped[b][i] == "0":
            comp1 = comp1 + 1

        if fileheregettingstripped[b][i] == "1":
            comp2 = comp2 + 1

        b = b + 1 #index for this

    if comp1 > comp2:
       sumofgammarate = sumofgammarate
       l = l - 1

    if comp1 < comp2:
        sumofgammarate = sumofgammarate + pow(2, l)
        l = l - 1
    b = 0 #setting it back because its inside
    comp1 = 0 #resseting the comps
    comp2 = 0 #resseting the comps
    i = i + 1

i = 0
b = 0
comp3 = 0
comp4 = 0
l = k
epsilonrate = 0

while i < k + 1:
    while b < countoftotal:
        if fileheregettingstripped[b][i] == "0":
            comp3 = comp3 + 1

        if fileheregettingstripped[b][i] == "1":
            comp4 = comp4 + 1

        b = b + 1 #index for this

    if comp3 < comp4:
       epsilonrate = epsilonrate
       l = l - 1

    if comp3 > comp4:
        epsilonrate = epsilonrate + pow(2, l)
        l = l - 1

    b = 0 #setting it back because its inside
    comp3 = 0 #resseting the comps
    comp4 = 0 #resseting the comps
    i = i + 1

print(epsilonrate * sumofgammarate)








