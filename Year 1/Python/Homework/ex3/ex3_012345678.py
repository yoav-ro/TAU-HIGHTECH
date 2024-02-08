# Python Programming - Ex3


#########################################
# Question 1 - do not delete this comment
#########################################
def is_in_range(lst1, a, b):
    # Write the rest of the code for question 1 below here.
    if len(lst1) == 0:
        return True
    res = True

    for num in lst1:
        if num <= a or num >= b:
            res = False
    return res


#########################################
# Question 2 - do not delete this comment
#########################################
def first_upper_str(lst2):
    # Write the rest of the code for question 2 below here.
    if len(lst2) == 0:
        return -1
    for index, item in enumerate(lst2):
        itemStringNoSpaces = str(item).replace(" ", "")
        if itemStringNoSpaces.isalpha() and itemStringNoSpaces.isupper():
            return index
        elif index == len(lst2) - 1:
            return -1


print(first_upper_str([1, 2, 3, 55, "FF", 11, False]))
print(first_upper_str([]))
print(first_upper_str([1, 2, 3, 55, "FF ", 11, False]))
print(first_upper_str([1, 2, 3, 55, "aBCD", 11, False]))


#########################################
# Question 3 - do not delete this comment
#########################################
def drop_duplicates(lst3):
    # Write the rest of the code for question 3a below here.
    filteredList = []
    for item in lst3:
        if filteredList.count(item) == 0:
            filteredList.append(item)

    return filteredList


print(drop_duplicates([1, 2, 3, 3, 4, 2, 5, 6, 6]))


def drop_duplicates_in_place(lst3):
    # Write the rest of the code for question 3b below here.
    for index, item in enumerate(lst3):
        if lst3.count(item) > 1:
            for indexToPop, itemPopScan in enumerate(lst3):
                if item == itemPopScan and indexToPop != index:
                    lst3.pop(indexToPop)

    print(lst3)


print(drop_duplicates_in_place([1, 2, 3, 3, 4, 2, 5, 6, 6]))


#########################################
# Question 4 - do not delete this comment
#########################################
def is_contain(lst4, lst5):
    # Write the rest of the code for question 4 below here.
    if len(lst5) == 0:
        return lst5
    resList = []
    for item5 in lst5:
        if lst4.count(item5) == 0:
            resList.append(-1)
        else:
            for item4 in lst4:
                if item5 == item4:
                    if lst4.count(item5) >= 1:
                        resList.append(lst4.index(item5))
                        break

    return resList


lst4 = [1, 2, 4, 2, 7, 9, 12]
lst5 = [0, 2, 4, 11, 2, 21, 12, 13]
# lst4 = [] 
# lst5 = [0,2,4,11,2,21,12,13]
# lst4 = [1,2,5,2,31,2,4,6] 
# lst5 = [] 
print(is_contain(lst4, lst5))

#########################################
# Question 5 - do not delete this comment
#########################################
# def mul_elementwise(mat1, mat2):
# Write the rest of the code for question 5 below here.


#########################################
# Question 6 - do not delete this comment
#########################################
# def mat_mul_vec(mat3, vec):
# Write the rest of the code for question 6 below here.
