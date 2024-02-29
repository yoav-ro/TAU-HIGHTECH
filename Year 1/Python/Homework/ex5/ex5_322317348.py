# Exercise 5: Python Programming

path = "Year 1\Python\Homework\ex5/"


#########################################
# Question 1 - do not delete this comment
#########################################
def mean_nums(file):
    # Write the rest of the code for question 1 below here.
    f = open(path + "/" + file, "r")
    numList = f.read().split(" ")
    return sum([(int)(num) for num in numList]) / len(numList)


# print(mean_nums("q1.txt"))


#########################################
# Question 2 - do not delete this comment
#########################################
def copy_long_words(infile, outfile, k):
    # Write the rest of the code for question 2 below here.
    initFile = open(path + "/" + infile, "r")
    wordsList = initFile.read().split()
    validWords = []
    for word in wordsList:
        if len(word) >= k:
            validWords.append(word)
    if len(validWords) == 0:
        open("outfile.txt", "x")
    else:
        newFile = open(path + outfile, "x")
        for word in validWords:
            newFile.write(word + "\n")


#########################################
# Question 3 - do not delete this comment
#########################################
def get_x_freqs(infile, outfile, x):
    # Write the rest of the code for question 3 below here.
    if len(infile) == 0 or len(outfile) == 0:
        raise ValueError("Invalid file name")
    initFile = open(path + "/" + infile, "r")
    wordsList = initFile.read().split()
    wordsDir = {}
    for word in wordsList:
        if word in wordsDir:
            wordsDir[word] += 1
        else:
            wordsDir[word] = 1

    sordtedDir = dict(sorted(wordsDir.items(), key=lambda word: word[1], reverse=True))
    newFile = open(path + outfile, "x")
    wordCount = 0
    for word in sordtedDir:
        if wordCount < x:
            newFile.write("%s %s" % (word, sordtedDir[word]) + "\n")
            wordCount += 1


#########################################
# Question 4 - do not delete this comment
#########################################
def decode(in_file, out_file):
    # Write the rest of the code for question 4 below here.
    try:
        initFile = open(path + "/" + in_file, "r")
        wordsList = initFile.read()
        decodedTtext = ""
        for char in wordsList:
            charASCII = ord(char)
            decodedChar = chr(charASCII)
            if decodedChar == "z":
                decodedTtext = decodedTtext + "a"
            elif decodedChar == "Z":
                decodedTtext = decodedTtext + "A"
            elif (charASCII >= 65 and charASCII < 90) or (
                charASCII >= 97 and charASCII < 122
            ):
                decodedTtext = decodedTtext + chr(charASCII + 1)
            else:
                decodedTtext = decodedTtext + char
        newFile = open(path + out_file, "x")
        newFile.write(decodedTtext)

    except IOError:
        raise IOError("Can't decipher file due to an IO Error")
    finally:
        initFile.close()
        newFile.close()

    print(decodedTtext)

#########################################
# Question 5 - do not delete this comment
#########################################
# def process_contacts(contacts_file):
# Write the rest of the code for question 5 below here.

#########################################
# Question 6 - do not delete this comment
#########################################
# def get_covid_cases_by_date(filename, date):
# Write the rest of the code for question 6 below here.
