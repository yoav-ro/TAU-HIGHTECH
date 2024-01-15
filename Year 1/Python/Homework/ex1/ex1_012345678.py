""" Exercise #1. Python Programming."""

#########################################
# Question 1 - do not delete this comment
#########################################
name = "Yoav"  # Replace ??? with a string of your choice.
age = 23  # Replace ??? with a number of your choice.
# Write the rest of the code for question 1 below here.
print("My name is %s and I am %s years old." % (name, age))

#########################################
# Question 2 - do not delete this comment
#########################################
a = 3  # Replace ??? with a positive float of your choice.
b = 4  # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 2 below here.
print("Length of diagonal is: " + (str)((a * a + b * b) ** 0.5))
print("Circumference is: " + str((2 * a + 2 * b)))
print("Area is: " + str(a * b))

#########################################
# Question 3 - do not delete this comment
#########################################
number = "7"  # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.
if int(number) % 3 == 0:
    print("I am %s and I am divisble by 3" % (number))
else:
    print("I am %s and I am not divisible by 3" % (number))

#########################################
# Question 4 - do not delete this comment
#########################################
a = 2  # Replace ??? with a int of your choice.
b = 9  # Replace ??? with a int of your choice.
c = 8  # Replace ??? with a int of your choice.
# Write the rest of the code for question 4 below here.
print((a * b) ** (1 / c))
print((b**a) ** (1 / c))
print((b / a) - (c / a))

#########################################
# Question 5 - do not delete this comment
#########################################
text = "Python is fun"  # Replace ??? with a string of your choice.
copies = 2  # Replace ??? with a int of your choice.
# Write the rest of the code for question 5 below here.
str1 = text[1::2].upper()
str2 = text[::2].lower()
new_str = str1 + str2
if copies > 0:
    print(new_str * copies)
else:
    print("Invalid Input!!!")
