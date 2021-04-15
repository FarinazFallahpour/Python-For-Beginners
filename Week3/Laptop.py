#Farinaz Fallahpour

laptopNumber = int(input())
laptopFeatureList = []

for i in range(0, laptopNumber):
    element = input()
    laptopFeatureList.extend(element.split(" "))

quality = laptopFeatureList[::2]
cost = laptopFeatureList[1::2]

flag = False

for i in range(0, laptopNumber):
    for j in range(0, laptopNumber - 1):
        if int(cost[i]) < int(cost[j]):
            if int(quality[i]) > int(quality[j]):
                flag = True

if flag:
    print("happy irsa")
else:
    print("poor irsa")
