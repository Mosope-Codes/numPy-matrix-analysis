import numpy as np
import random as random



alphabethToLetter = {" " : 0, "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5,
                     "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10,
                     "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15,
                     "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
                     "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25,
                     "z" : 26, "A" : 27, "B" : 28, "C" : 29, "D" : 30,
                     "E" : 31, "F" : 32, "G" : 33, "H" : 34, "I" : 35,
                     "J" : 36, "K" : 37, "L" : 38, "M" : 39, "N" : 40,
                     "O" : 41, "P" : 42, "Q" : 43, "R" : 44, "S" : 45,
                     "T" : 46, "U" : 47, "V" : 48, "W" : 49, "X" : 50,
                     "Y" : 51, "Z" : 52, "." : 53, "," : 54, ";" : 55,
                     ":" : 56, "\n" : 57}   


def convertWordsToArrayOfNumbers(words):
    arrayOfNumbers = []
    for letter in words:
            arrayOfNumbers.append(alphabethToLetter[letter])

    return arrayOfNumbers

def convertFileToArray(file):
    with open(file, "r") as openFile:
        fileAsString = openFile.read()
        print(fileAsString)
        arrayOfNumbersFromLetters = convertWordsToArrayOfNumbers(fileAsString)

    return arrayOfNumbersFromLetters

def convertArrayToMatrix(array):
    matrix = np.zeros((3, (len(array) // 3) + 1), int)
    flattenedMatrix = matrix.flatten()

    for i, num in enumerate(array):
        if i < len(array):
            flattenedMatrix[i] = num
        else:
            break

    reshapedMatrix = flattenedMatrix.reshape(3, (len(array) // 3) + 1)

    return reshapedMatrix

def encodeMatrix(matrix):
    secretKey = np.array([[0, 2, 2],
                          [2, 3, 0],
                          [0,  2, 1]]) 

    encryptedMatrix = np.dot(secretKey, matrix)
    encryptedText = np.array2string(encryptedMatrix)
    print(np.array2string(encryptedMatrix))

    file = open("encoded.txt", "w") 
    file.write(encryptedText)
    file.close()

    return encryptedMatrix


print("Welcome to Encrypto-Chat")
fileConvertedToArray = convertFileToArray("new.txt")
arrayConvertedtoMatrix = convertArrayToMatrix(fileConvertedToArray)
encryptedMessage = encodeMatrix(arrayConvertedtoMatrix)

