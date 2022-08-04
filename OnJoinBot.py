import math

modifier = 25

def CreateSentences(whatToWrite, wordEmoji, fillEmoji):
    arr = []
    arr[0] = ["", "", "", "", "", "", ""]

    AddSpace(arr[0], fillEmoji)

    i = 1
    arrIndex = 0
    for c in whatToWrite:
        if i % modifier == 0:
            arrIndex = math.floor(i / modifier)
            arr[arrIndex] = ["", "", "", "", "", "", ""]
            AddSpace(arr[arrIndex], fillEmoji)
            i += 1
        GetCharacter(arr[arrIndex], c, wordEmoji, fillEmoji)
        AddSpace(arr[arrIndex], fillEmoji)
        i += 1

    return arr

def AddSpace(arr, fillEmoji):
        arr[0] += fillEmoji
        arr[1] += fillEmoji
        arr[2] += fillEmoji
        arr[3] += fillEmoji
        arr[4] += fillEmoji
        arr[5] += fillEmoji
        arr[6] += fillEmoji

def printA(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + wordEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printB(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + wordEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printC(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printD(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printE(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + fillEmoji
    arr[3] += wordEmoji + wordEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + fillEmoji
    arr[5] += wordEmoji + wordEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printF(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + fillEmoji
    arr[3] += wordEmoji + wordEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + fillEmoji
    arr[5] += wordEmoji + fillEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printG(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + fillEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printH(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + wordEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printI(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + fillEmoji
    arr[2] += fillEmoji + fillEmoji + fillEmoji
    arr[3] += fillEmoji + wordEmoji + fillEmoji
    arr[4] += fillEmoji + wordEmoji + fillEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printJ(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + fillEmoji + wordEmoji
    arr[2] += fillEmoji + fillEmoji + wordEmoji
    arr[3] += fillEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printK(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + wordEmoji + fillEmoji
    arr[3] += wordEmoji + wordEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printL(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + fillEmoji
    arr[3] += wordEmoji + fillEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + fillEmoji
    arr[5] += wordEmoji + wordEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printM(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + wordEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printN(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + fillEmoji + fillEmoji
    arr[2] += fillEmoji + wordEmoji + fillEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printO(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printP(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + wordEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + fillEmoji
    arr[5] += wordEmoji + fillEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printQ(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += fillEmoji + wordEmoji + wordEmoji
    arr[4] += fillEmoji + fillEmoji + wordEmoji
    arr[5] += fillEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printR(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + fillEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + wordEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printS(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += fillEmoji + wordEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + fillEmoji
    arr[3] += fillEmoji + wordEmoji + fillEmoji
    arr[4] += fillEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printT(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + wordEmoji
    arr[2] += fillEmoji + wordEmoji + fillEmoji
    arr[3] += fillEmoji + wordEmoji + fillEmoji
    arr[4] += fillEmoji + wordEmoji + fillEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printU(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + wordEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printV(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printW(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += wordEmoji + fillEmoji + wordEmoji
    arr[4] += wordEmoji + wordEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printX(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += fillEmoji + wordEmoji + fillEmoji
    arr[4] += wordEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + fillEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printY(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + fillEmoji + wordEmoji
    arr[2] += wordEmoji + fillEmoji + wordEmoji
    arr[3] += fillEmoji + wordEmoji + fillEmoji
    arr[4] += fillEmoji + wordEmoji + fillEmoji
    arr[5] += fillEmoji + wordEmoji + fillEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def printZ(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji + fillEmoji + fillEmoji
    arr[1] += wordEmoji + wordEmoji + wordEmoji
    arr[2] += fillEmoji + wordEmoji + fillEmoji
    arr[3] += fillEmoji + fillEmoji + wordEmoji
    arr[4] += fillEmoji + fillEmoji + wordEmoji
    arr[5] += wordEmoji + wordEmoji + wordEmoji
    arr[6] += fillEmoji + fillEmoji + fillEmoji

def GetCharacter(arr, c, wordEmoji, fillEmoji):
    if c == 'a': printA(arr, wordEmoji, fillEmoji)
    elif c =='b': printB(arr, wordEmoji, fillEmoji)
    elif c == 'c': printC(arr, wordEmoji, fillEmoji)
    elif c == 'd': printD(arr, wordEmoji, fillEmoji)
    elif c == 'e': printE(arr, wordEmoji, fillEmoji)
    elif c == 'f': printF(arr, wordEmoji, fillEmoji)
    elif c == 'g': printG(arr, wordEmoji, fillEmoji)
    elif c == 'h': printH(arr, wordEmoji, fillEmoji)
    elif c == 'i': printI(arr, wordEmoji, fillEmoji)
    elif c == 'j': printJ(arr, wordEmoji, fillEmoji)
    elif c == 'k': printK(arr, wordEmoji, fillEmoji)
    elif c == 'l': printL(arr, wordEmoji, fillEmoji)
    elif c == 'm': printM(arr, wordEmoji, fillEmoji)
    elif c == 'n': printN(arr, wordEmoji, fillEmoji)
    elif c == 'o': printO(arr, wordEmoji, fillEmoji)
    elif c == 'p': printP(arr, wordEmoji, fillEmoji)
    elif c == 'q': printQ(arr, wordEmoji, fillEmoji)
    elif c == 'r': printR(arr, wordEmoji, fillEmoji)
    elif c == 's': printS(arr, wordEmoji, fillEmoji)
    elif c == 't': printT(arr, wordEmoji, fillEmoji)
    elif c == 'u': printU(arr, wordEmoji, fillEmoji)
    elif c == 'v': printV(arr, wordEmoji, fillEmoji)
    elif c == 'w': printW(arr, wordEmoji, fillEmoji)
    elif c == 'x': printX(arr, wordEmoji, fillEmoji)
    elif c == 'y': printY(arr, wordEmoji, fillEmoji)
    elif c == 'z': printZ(arr, wordEmoji, fillEmoji)