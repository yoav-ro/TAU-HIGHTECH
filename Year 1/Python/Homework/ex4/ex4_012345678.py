# Python Programming - Ex4


#########################################
# Question 1 - do not delete this comment
#########################################
def lists_to_simple_dict(names, dates):
    # Write the rest of the code for question 1 below here.
    covidTest = {}
    for i, name in enumerate(names):
        covidTest[name] = dates[i]
    return covidTest


# #########################################
# Question 2 - do not delete this comment
#########################################
def lists_to_complex_dict(names, dates):
    # Write the rest of the code for question 2 below here.
    covidTest = {}
    for i, name in enumerate(names):
        if name not in covidTest:
            covidTest[name] = dates[i]
        else:
            if dates[i][0] > covidTest[name][0]:  # Year comparison
                covidTest[name] = dates[i]
            elif dates[i][1] > covidTest[name][1]:  # If year is same, month comparison
                covidTest[name] = dates[i]
            elif dates[i][2] > covidTest[name][2]:  # If month is same, day comparison
                covidTest[name] = dates[i]
    return covidTest


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_location(s, k):
    # Write the rest of the code for question 3a below here.
    strCopy = str(s)
    result = [{}]
    for i, char in enumerate(strCopy):
        if (i + k) < len(s):
            currSub = s[i : i + k]
            print(currSub)
            result[0][currSub] = s.count(
                currSub
            )  # bug! The python "count" function doesnt count overlaps (counting "cc" in "cccc" only returns 2)

    result.append(max(result[0], key=result[0].get))

    return result


def countSubStrings(mainStr, subStr):
    subCount = 0
    for i, char in enumerate(mainStr):
        if (i + len(subStr)) < len(mainStr):
            for j, subChar in enumerate(subStr):
                if mainStr[i] != subStr[j]:
                    continue
                elif j == len(subStr):
                    subCount += 1
    return subCount


print(countSubStrings("cccc", "cc"))

# txt = "abdsfabababsfasf"
# res = find_substring_location(txt, 1)
# print(res[0])
# print(res[1])

txt = "abcabcbaaaccccscscscffgf"
res = find_substring_location(txt, 2)
print(res[0])
print(res[1])

#########################################
# Question 4 - do not delete this comment
#########################################de
# def mul_sparse_matrices(d1, d2):
# Write the rest of the code for question 4 below here.
