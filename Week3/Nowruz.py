#Farinaz Fallahpour

'''Using List Comprehensions
List comprehensions are a third way of making lists.
 squares = []
for i in range(10):
 squares.append(i * i)
the first example in just a single line of code:
squares = [i * i for i in range(10)]
 squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

new_list = [expression for member in iterable]
Every list comprehension in Python includes three elements:

expression is the member itself, a call to a method,
or any other valid expression that returns a value.
In the example above, the expression i * i is the square of the member value.
member is the object or value in the list or iterable.
In the example above, the member value is i.
iterable is a list, set, sequence, generator,
or any other object that can return its elements one at a time.
In the example above, the iterable is range(10).

 '''
prompt = input()
strList = prompt.split(' ')
floatList = []
for i in range(0, len(strList)):
    floatList.append(float(strList[i]))
floatList.sort()
distance= ((floatList[2] - floatList[1]) + (floatList[1] - floatList[0]))
dot=str(distance).split('.')
if dot[1] =='0':
    print(dot[0])
else:
    print(distance)

