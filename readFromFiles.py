def readFromFiles(userFile):
    with open(userFile, "r") as users:
        for user in users:
            print(user)


def writeToFile(userFile, dataToWrite):
    with open (userFile, "a") as users:
        users.write(dataToWrite)


readFromFiles("users.txt")
writeToFile("users.txt","Hello there!")
readFromFiles("users.txt")