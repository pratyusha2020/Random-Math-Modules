import math
print("These letters correspond with the trig fuction")
print("A. Sine")
print("B. Cosine")
print("C. Tangent")
y= input("Pick a letter:")
x= int(input("Enter the angle:"))
if y==("A"):
    print(math.sin(x))
elif y==("B"):
    print(math.cos(x))
elif y==("C"):
    print(math.tan(x))
else:
    print("Invalid input")


