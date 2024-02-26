def countSubStrings(mainStr, subStr):
    subCount = 0
    for i, char in enumerate(mainStr):
        if (i + len(subStr)) < len(mainStr):
            for j, subChar in enumerate(subStr):
                print(char, subChar)
                if char != subChar:
                    break
                elif j == len(subStr):
                    subCount += 1
    return subCount


print(countSubStrings("asfasccccasd", "cc"))


def count2(mainStr, subStr):
    return sum(
        1
        for i in range(len(mainStr) - len(subStr) + 1)
        if mainStr[i : i + len(subStr)] == subStr
    )


# print(count2("cccc", "cc"))


def subListSum(numList, target):
    print(numList, target)
    if target == 0:
        return True
    elif len(numList) == 0:
        return False
    else:
        option1 = subListSum(numList[:-1], target - numList[-1])
        option2 = subListSum(numList[:-1], target)
    return option1 or option2


print(subListSum([-5,0,-5,5,7,-1], 1))
