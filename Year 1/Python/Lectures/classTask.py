def addToDB(db, inputList):
    nameToAdd = inputList[0]
    idToAdd = inputList[1]
    gradesToAdd = list(map(int, inputList[1:]))

    newData = {"name": nameToAdd, "grades": gradesToAdd}
    db[idToAdd]= newData
    return db


testInput = ['Martin', 123, 60, 70, 80]
student_grades= {101:{'name': 'Alice', 'grades': [85,90,92]}}
print(addToDB(student_grades, testInput))
