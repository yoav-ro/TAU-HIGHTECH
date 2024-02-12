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

print(count2("cccc", "cc"))