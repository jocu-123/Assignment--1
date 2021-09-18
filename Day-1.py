#reverse the items in a list after sorting
x= input('Enter the values:')
li = [int(i) for i in x.split()]
print(li)
li.sort()
print(li)
li.reverse()
print(li)
