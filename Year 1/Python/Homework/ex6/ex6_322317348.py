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

    lst.append(5)
    if is_changeable(n - 5, lst):
        return True
    lst.pop()

    lst.append(2)
    if is_changeable(n - 2, lst):
        return True
    lst.pop()

    return False


#########################################
# Question 5a - do not delete this comment
#########################################
def climb_combinations(n):
    # Write the rest of the code for question 5a below here.
    if n == 0 or n == 1:
        return 1
    return climb_combinations(n - 1) + climb_combinations(n - 2)


# print(climb_combinations(10))

#########################################
# Question 5b - do not delete this comment
#########################################
# def climb_combinations_memo(n, memo=None):
# Write the rest of the code for question 5b below here.
