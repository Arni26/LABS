# Operators
print(5 + 4 - 7 + 3)


#Lists


thislist = ["apple", "banana", "cherry"]
print(thislist)

#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Access to Lists
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Change Lists Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Add List Items (second position)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#(last item)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#loop lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#copy lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


