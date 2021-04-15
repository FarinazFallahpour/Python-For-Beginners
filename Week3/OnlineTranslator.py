#Farinaz Fallahpour
number = int(input())
enFaDic = {}
for i in range(0, number):
    element = input()
    enFa = element.split(" ")
    enFaDic[enFa[0]] = enFa[1]

sentence = input()
senList = sentence.split(" ")
output = ""
for i in range(0, len(senList)):
    if senList[i] in enFaDic.keys():
        output = output + " " + enFaDic[senList[i]]
    else:
        output = output + " " + senList[i]
print(output.strip())
