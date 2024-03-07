# Exercise 6: Python Programming


#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    # Write the rest of the code for question 1 below here.
    if len(s) == 1 or len(s) == 0:
        return s
    return s[len(s) - 1] + reverse_string(s[: len(s) - 1])


#########################################
# Question 2 - do not delete this comment
#########################################
def max_rec(lst):
    # Write the rest of the code for question 2 below here.
    if len(lst) < 2:
        return lst[0]
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
    elif lst[0] <= lst[1]:
        lst.pop(0)
        return max_rec(lst)


#########################################
# Question 3 - do not delete this comment
#########################################
def can_return_to_earth(weights, W, K):
    # Write the rest of the code for question 3 below here.
    if W == 0:
        return True
    elif len(weights) == 0:
        return False
    elif weights[-1] > K:
        return can_return_to_earth(weights[:-1], W, K)
    else:
        option1 = can_return_to_earth(weights[:-1], W - weights[-1], K)
        option2 = can_return_to_earth(weights[:-1], W, K)
    return option1 or option2


# print(can_return_to_earth([5, 2, 6, 4, 2], 8, 5))


#########################################
# Question 4 - do not delete this comment
#########################################
def is_changeable(n, lst):
    # Write the rest of the code for question 4 below here.
    if n == 0:
        return True
    if n < 2 or n == 3:
        return False
    option1 = is_changeable(n - 2, [2, *lst])
    option2 = is_changeable(n - 5, [5, *lst])
    # option1 = is_changeable(n , is_changeable_add2(lst))
    # option2 = is_changeable(n , is_changeable_add5(lst))

    return option1 or option2


def is_changeable_add2(lst):
    lst.append(2)
    return lst


def is_changeable_add5(lst):
    lst.append(5)
    return lst


testList = []
print(is_changeable(7.1, testList))
print(testList)


#########################################
# Question 5a - do not delete this comment
#########################################
# def climb_combinations(n):
# Write the rest of the code for question 5a below here.

#########################################
# Question 5b - do not delete this comment
#########################################
# def climb_combinations_memo(n, memo=None):
# Write the rest of the code for question 5b below here.
