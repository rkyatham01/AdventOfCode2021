filebeingread = open("day3input.txt", "r")

filehere = filebeingread.readlines()

fileheregettingstripped = [line.rstrip() for line in filehere] #used for First calculation

fileheregettingstripped2 = [line.rstrip() for line in filehere] #used for Second calculation

countoftotal = 0
for x in fileheregettingstripped:
   countoftotal = countoftotal + 1
   #countoftotal has the # of total lines read of file

temp3 = countoftotal

i = 0
j = 0
k = 0
b = 0

for x in fileheregettingstripped[0]:
    k = k + 1
k = k - 1

sum1 = 0
sum2 = 0
z = 0

SumOfOxygenRating = 0
counttemp = 0
#This is for the Oxygen Generator Rating
while i <= k:
    while b < countoftotal:
        if fileheregettingstripped[b][i] == "1":
            sum1 = sum1 + 1
        if fileheregettingstripped[b][i] == "0":
            sum2 = sum2 + 1
        b = b + 1

    if sum1 >= sum2: #keep values of 1 in position
        b = 0
        while b < countoftotal:
            if fileheregettingstripped[b][i] == "0":
                fileheregettingstripped.remove(fileheregettingstripped[b])
                countoftotal = countoftotal - 1
                b = 0
            b = b + 1

    if sum1 < sum2: #if zero is the most common
        b = 0
        while b < countoftotal:
            if fileheregettingstripped[b][i] == "1":
                fileheregettingstripped.remove(fileheregettingstripped[b])
                countoftotal = countoftotal - 1
                b = 0
            b = b + 1
    b = 0
    i = i + 1
    sum1 = 0
    sum2 = 0
#Now SumOfOxygenRating has the binary of oxygen generating rating

SumOfOxygenRating = fileheregettingstripped

i = 0
sum3 = 0
sum4 = 0
b = 0
countoftotal2 = temp3

while i <= k:
    while b < countoftotal2:
        if fileheregettingstripped2[b][i] == "1":
            sum3 = sum3 + 1
        if fileheregettingstripped2[b][i] == "0":
            sum4 = sum4 + 1
        b = b + 1

    if sum3 < sum4: #keep values of 1 in position
        b = 0
        while b < countoftotal2:
            if fileheregettingstripped2[b][i] == "0":
                fileheregettingstripped2.remove(fileheregettingstripped2[b])
                countoftotal2 = countoftotal2 - 1
                b = 0
            b = b + 1

    if sum3 >= sum4: #if zero is the most common
        b = 0
        while b < countoftotal2:
            if fileheregettingstripped2[b][i] == "1":
                fileheregettingstripped2.remove(fileheregettingstripped2[b])
                countoftotal2 = countoftotal2 - 1
                b = 0
            b = b + 1
    b = 0
    i = i + 1
    sum3 = 0
    sum4 = 0
    if countoftotal2 == 1:
        CO2ScrubberRating = fileheregettingstripped2[b]

#This is the CO2ScrubberRating

#CO2ScrubberRating has the binary representation of CO2 Scrubber rating
#Now SumOfOxygenRating has the binary of oxygen generating rating

SumOfOxygenRatingFinal = SumOfOxygenRating[0]

FinalOxygenRating = 0
FinalCO2Rating = 0
z = 0
lengthofthem = 0

for x in SumOfOxygenRatingFinal:
    lengthofthem = lengthofthem + 1

decrease = lengthofthem - 1
decrease2 = lengthofthem - 1
lengthofthem2 = lengthofthem - 1
index = 0

for x in range(0, lengthofthem2+1):
    if SumOfOxygenRatingFinal[index] == "1":
        FinalOxygenRating = FinalOxygenRating + pow(2, decrease)

    decrease = decrease - 1
    index = index + 1

index2 = 0

for x in range(0, lengthofthem2+1):
    if CO2ScrubberRating[index2] == "1":
        FinalCO2Rating = FinalCO2Rating + pow(2, decrease2)

    decrease2 = decrease2 - 1
    index2 = index2 + 1

print(FinalCO2Rating * FinalOxygenRating)















