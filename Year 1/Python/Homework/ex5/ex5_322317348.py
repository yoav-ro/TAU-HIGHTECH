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
        print("Can't decipher file due to an IO Error")
    finally:
        initFile.close()
        newFile.close()

    print(decodedTtext)


#########################################
# Question 5 - do not delete this comment
#########################################
def process_contacts(contacts_file):
    # Write the rest of the code for question 5 below here.
    try:
        csvFile = open(path + "/" + contacts_file, "r")
        retDict = {}
        dataByLines = csvFile.readlines()
        for personData in dataByLines:
            if personData[0][0] == "#":
                continue
            personDataList = personData.split(",")
            if "" in personDataList:
                raise ValueError("Invalid input file")
            personName = personDataList[0].strip() + " " + personDataList[1].strip()
            personCity = personDataList[3].strip()
            if personCity not in retDict:
                retDict[personCity] = [personName]
            elif retDict[personCity].count(personName) == 0:
                retDict[personCity].append(personName)
        return retDict
    except IOError:
        print("IO Error encountered")
        csvFile.close()
        return {}


# print(process_contacts("q5_good.csv"))


#########################################
# Question 6 - do not delete this comment
#########################################
def get_covid_cases_by_date(filename, date):
    # Write the rest of the code for question 6 below here.
    try:
        csvFile = open(path + "/" + filename, "r", encoding="UTF-8")
        dataList = csvFile.readlines()[1:]
        dataByDate = list(filter(lambda item: item.split(",")[3] == date, dataList))
        retDict = {}
        for dataRow in dataByDate:
            dataRowList = dataRow.split(",")
            if dataRowList[2] in retDict and dataRowList[4] != "<15":
                retDict[dataRowList[2]] += int(dataRowList[4])
            elif dataRowList[4] != "<15":
                retDict[dataRowList[2]] = int(dataRowList[4])
        sortedData = list(
            sorted(retDict.items(), key=lambda item: item[1], reverse=True)
        )
        print(sortedData[0])
        count = 0
        while count < 10:
            print("%s   %s" % (sortedData[count][0], sortedData[count][1]))
            count += 1
    except IOError:
        print("placeholder")
        


get_covid_cases_by_date("geographic-sum-per-day-ver_00588_2021_only.csv", "2021-01-03")
