import numpy as np
import random as random
from encryption import encryptedMessage as encrypt


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


def decodeMatrix(encryptedMatrix):
    secretKey = np.array([[0, 2, 2],
                          [2, 3, 0],
                          [0,  2, 1]])
    decryptionKey = np.linalg.inv(secretKey)
    decryptedMatrix = np.dot(decryptionKey, encryptedMatrix)
         
    return decryptedMatrix

def convertDecryptedMatrixToWords(decryptedMatrix):
    decryptedWords = ""
    matrixToArray = decryptedMatrix.flatten()
    for number in matrixToArray:
        for key, value in alphabethToLetter.items():
            if value == number:
                decryptedWords += key

    file = open("decoded.txt", "w") 
    file.write(decryptedWords)
    file.close()

    return decryptedWords


print("Welcome to Decrypto-Chat")
print(encrypt)
decodedMatrix = decodeMatrix(encrypt)
message = convertDecryptedMatrixToWords(decodedMatrix)

print(message)

# [[ 46,   0,  16,  42,  54,   2], [139,  24,   5,  48,  6,  21], [ 42,   0,   9,  21,  29,   2]]