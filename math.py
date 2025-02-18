import math

degree=int(input("Input degree: "))
rad= degree * (math.pi / 180)
print ("Output radian: ",rad)
print()

a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
h=int(input("Height: "))
area=((a + b) * h) / 2
print("Area =",area)
print()

x=int(input("Number of sides: "))
y=int(input("Lenght of a side: "))
pol=(x * y**2) / (4 * math.tan(math.pi / x))
print("The area of the polygon is:",pol)
print()

l=int(input("Length of base: "))
hh=int(input("Height of parallelogram: "))
print (l*hh)