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
    print(weights, W)
    weights = list(filter(lambda item: item < K, weights))
    print(weights)
    if W == 0 or len(weights) == 0:
        return True
    if W < 0:
        return False
    if sum(weights) == W:
        return True
    if len(weights) == 1 and weights[0] != W:
        return False
    return can_return_to_earth(weights, W - weights[0], K)


print(can_return_to_earth([5, 2, 6, 4, 2], 8, 3))


#########################################
# Question 4 - do not delete this comment
#########################################
# def is_changeable(n, lst):
# Write the rest of the code for question 4 below here.


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
