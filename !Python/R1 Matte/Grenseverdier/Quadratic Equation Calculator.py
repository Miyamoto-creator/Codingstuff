
#imports the math function that finds the square root
import math

#while loop that defines the variables of the equation
a = int(input("Hva er A i andregradslikningen: "))
if a == 0:
    print("The first number cannot be zero.")
    exit()

b = int(input("Enter in the x value coefficient: "))

c = int(input("Enter the third number: "))

#the values under the sqare root
under_the_root = (b**2)-((4*a)*c)
if under_the_root < 0:
    print("\nThe number under the radical is negative. There are no answers.")
    exit()
root_result = math.sqrt(under_the_root)

#bottom portion of equation
bottom = (2*a)

#top positive
positive = (b*-1) + (root_result)
answer1 = positive/bottom

#top negative
negative = (b*-1) - (root_result)
answer2 = negative/bottom

#results
print("\nThe positive result is: " + str(answer1))
print("The negative result is: " + str(answer2))
fac1 = int(answer1) * -1
fac2 = int(answer2) * -1
if fac1 >= 0 and fac2 >= 0:
    print("\nThe answers factored out: (x+" + str(fac1) + ") (x+" + str(fac2) + ")\n")
elif fac1 >= 0 and fac2 < 0:
    print("\nThe answers factored out: (x+" + str(fac1) + ") (x" + str(fac2) + ")\n")
elif fac1 < 0 and fac2 >= 0:
    print("\nThe answers factored out: (x" + str(fac1) + ") (x+" + str(fac2) + ")\n")
else:
    print("\nThe answers factored out: (x" + str(fac1) + ") (x" + str(fac2) + ")\n")