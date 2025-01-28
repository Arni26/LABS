# Tuple

#Tuples are used to store multiple items in a single variable.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#allows duplicates, can access with index []


#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#sets
#duplicate sets will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#dictonary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#output will be Ford

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])
#OUtput Tobias


#If else
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#while
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#exit the loop when x=banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

