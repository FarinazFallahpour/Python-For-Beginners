#Farinaz Fallahpour

n = int(input())
country = {}
for i in range(0, n):
    element = input()
    if element in country.keys():
        country[element] += 1
    else:
        country[element] = 1


for key in sorted(country.keys()):
    print(key, country[key])
