

filebeingread = open("day2input.txt", "r")

filehere = filebeingread.readlines()

fileheregettingstripped = [line.rstrip() for line in filehere]

countoftotal = 0

for x in fileheregettingstripped:
   countoftotal = countoftotal + 1
   #countoftotal has the # of total lines read of file
index = 0
i = 0

sumofdistance = 0
sumofdepth = 0
aim = 0

while i < countoftotal:
    split1 = fileheregettingstripped[i]
    splitline = split1.split(" ")
    if splitline[0] == "forward":
        sumofdistance = sumofdistance + int(splitline[1])
        sumofdepth = sumofdepth + (aim * int(splitline[1]))


    if splitline[0] == "down":
        aim = aim + int(splitline[1])


    if splitline[0] == "up":
        aim = aim - int(splitline[1])


    i = i + 1 #iterates through

multiplyDepthAndSum = sumofdistance * sumofdepth
print(multiplyDepthAndSum)


