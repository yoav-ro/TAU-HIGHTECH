# Python Programming - Ex2


#########################################
# Question 1 - do not delete this comment
#########################################
str1 = "abcfefgcba"  # Replace ??? with a string
# Write the rest of the code for question 1 below here.
res = True
if len(str1) % 2 != 0:
    res = False
firstThree = str1[0:3]
if (
    str1[0] != str1[len(str1) - 1]
    and str1[1] != str1[len(str1) - 2]
    and str1[2] != str1[len(str1) - 3]
):
    res = False
if str1[3] != "F" and str1[3] != "f":
    res = False

if res:
    print("Yes")
else:
    print("No")


#########################################
# Question 2 - do not delete this comment
#########################################
A = [4, 11, 12, 18, 22, 24]  # Replace ??? with a list of numbers (int/float).
a = 3  # Replace ??? with a positive int.
b = 10  # Replace ??? with a positive int.
# Write the rest of the code for question 2 below here.
ret = -1
for idx, num in enumerate(A):
    if num % a == 0 and num % b == 0:
        ret = idx
        break
print(ret)

#########################################
# Question 3 - do not delete this comment
#########################################
C = [3, 1, 10, 21, 2, 2]  # Replace ??? with a list of numbers (int/float).
# Write the rest of the code for question 3 below here.
retSum = 1
if len(C) == 1:
    print(C[0])
elif len(C) != 0:
    for idx, num in enumerate(C):
        if idx != len(C) - 1:
            retSum *= num + C[idx + 1]
    print(retSum)
else:
    print(0)

#########################################
# Question 4 - do not delete this comment
#########################################
D = [0, 2, 3, 11, 2]  # Replace ??? with a list of numbers (int/float).
E = [12, 2, 10, 3, 7, 4]  # ??? with a list of numbers (int/float).
# Write the rest of the code for question 4 below here.
dCountFor = 0
dCountWhile = 0
printListFor = []
printListWhile = []
# For loop solution
for index, numD in enumerate(D):
    dCountFor += numD
dAvgFor = dCountFor / len(D)
for index, numE in enumerate(E):
    if numE > dAvgFor:
        printListFor.append(index)

# While loop solution
dInitLen = len(D)
while len(D) > 0:
    dCountWhile += D.pop()
dAvgWhile = dCountWhile / dInitLen
i = 0
while i < len(E):
    if E[i] > dAvgWhile:
        printListWhile.append(i)
    i += 1
print(printListFor)
print(printListWhile)

#########################################
# Question 5 - do not delete this comment
#########################################
# Write the code for question 5 below here.
my_string = "abaadddefggg"  # Replace ??? with a string
k = 9  # Replace ??? with a positive int.
sameCharCount = 1
if len(my_string) == 0:
    print("Didn't find a substring of length " + str(k))
else:
    for i, char in enumerate(my_string):
        if i == len(my_string) - 2:  # Check if the whole string has been checked with no substrings
            print("Didn't find a substring of length " + str(k))
            break
        # Check if the current substring was increased
        elif char == my_string[i - 1]:
            sameCharCount += 1
        if sameCharCount == k:  # Check if the last found substring is matching k
            print("For length %s ,found the substring %s" % (k, char*k))
            break
