#Farinaz Fallahpour

strTeacher = input()
strList = strTeacher.split("+")
intList = []
for i in range(0, len(strList)):
    intList.append(int(strList[i]))

intList.sort()
strStd = ''
for i in range(0, len(intList)):
    if i != len(intList) - 1:
        strStd = strStd + str(intList[i]) + '+'
    else:
        strStd = strStd + str(intList[i])

print(strStd)
