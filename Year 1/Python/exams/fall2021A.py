def max_in_tree(lst, max=0):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 0:
        return None
    if type(lst[0]) == int:
        higher = max
        if lst[0] > max:
            higher = lst[0]
        return max_in_tree(lst[:1], higher)
    if type(lst[0]) == list:
        return max_in_tree(lst[0], max)
    # if len(lst) == 1:
    #     return lst[0]
    # if type(lst[0]) == list:
    #     return max(max_in_tree(lst[0], max_in_tree(lst[1:])))
    # elif type(lst[0]) == int:
    #     return max(lst[0], max_in_tree(lst[1:]))


lst = [1, 2, 5, 1]
lst2 = [2, 8, 123, 1, 7]

# print(list(set(lst.extend(lst2))).sort())

lst = [1, 5]
# print(max_in_tree(lst))


testDict = {"yoav": "hi", "asaw": "bi"}
print("yoav" in testDict)
test = {"test": [1, 5, 2], "noo": [2]}
print(test.items())


testS = "book"
testD = {"b": 1, "o": 2, "k": 1}


def can_create_str(s, d):
    if len(s) == 0:
        return True
    currChar = s[0]
    if currChar in d and d[currChar] > 0:
        dCopy= d.copy()
        dCopy[currChar] = dCopy[currChar] - 1
        return can_create_str(s[1:], dCopy)
    return False

print(can_create_str(testS,testD))
print(testD)

st = 'netta'
print(st[::-1])