#Farinaz Fallahpour

str = input()
stra = str.replace('a', '')
stre = stra.replace('e', '')
stri = stre.replace('i', '')
stro = stri.replace('o', '')
stru = stro.replace('u', '')
strA = stru.replace('A', '')
strE = strA.replace('E', '')
strI = strE.replace('I', '')
strO = strI.replace('O', '')
strU = strO.replace('U', '')
length = len(strU)
dotStr = ''

for i in range(0, length):
    dotStr = dotStr + '.' + strU[i]

print(dotStr.lower())
