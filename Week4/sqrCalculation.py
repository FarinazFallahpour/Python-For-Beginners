#Farinaz Fallahpour
import math

number = int(input())
list = []
for i in range(0, number):
    list.append(str(math.sqrt(int(input()))))

for i in range(0, number):
    this = list[i].split(".")
    if len(this[1]) > 4:
        floatpart = this[1][:4]
    else:
        floatpart = "0000"
    print(this[0] + "." + floatpart)
