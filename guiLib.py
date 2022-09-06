from pydoc import locate
from click import command
from sympy import false
import numpy as np
import matplotlib.pyplot as plt
import TMMlib


class Materiel():
    def __init__(self, n, lambda0,  d = -1):
        self.n = n
        self.lambda0 = lambda0
        self.d = d
        if self.d < 0:
            self.d = self.lambda0 / (4 * self.n)

def finalText(text, numbers):
    textSize = len(text)
    i = 0
    finishNumberLetter = False
    dotCount = 0
    newNumbers = np.array([])
    openPlace = 0
    closePlace = 0
    dotPlace = 0
    
    while i < textSize:
        if finishNumberLetter == False:
            if text[i] == ".": 
                if text[i+1] != "(":
                    text = text[:i] + text[i+1] * int(numbers[dotCount]) + text[i+2:]
                    textSize = len(text)
                
                else:
                    newNumbers = np.append(newNumbers, numbers[dotCount])
                
                dotCount += 1

        if finishNumberLetter:
            if text[i] == ".":
                dotCount += 1
                dotPlace = i
                openPlace = i + 1
            
            if text[i] == ")":
                closePlace = i
            
            if openPlace != 0 and closePlace != 0:
                text = text[:dotPlace] + text[openPlace+1 : closePlace] * int(newNumbers[dotCount-1]) + text[closePlace+1:]
                newNumbers = np.delete(newNumbers, dotCount-1)
                i = 0
                closePlace = 0
                openPlace = 0
                dotPlace = 0
                dotCount = 0
                textSize = len(text)               
                continue       
        
        i += 1     
        if i == textSize and finishNumberLetter == False:
            finishNumberLetter = True
            dotCount = 0
            i = 0
        
        if i == textSize and len(newNumbers) == 0:
            break
    
    return text

def setMixText(text):
    numbers = np.array([])
    numberText = ""
    newText = ""
    textSize = len(text)
    i = 0
    findNumber = True

    while i < textSize:
        asciiResult = ord(text[i])
        if asciiResult > 47 and asciiResult < 58:
            numberText += text[i]
            
            if i == (textSize-1):
                number = int(text[i])
                numbers = np.append(numbers, number)
            
            if findNumber:
                newText += "."
                findNumber = False

        else:
            newText += text[i]
            findNumber = True
            if numberText != "":
                number = int(numberText)
                numbers = np.append(numbers, number)
                numberText = ""
        i += 1
    i = 0
    lastText = finalText(newText, numbers)
    
    return lastText

def calculate(mode, lambda0, minLambda, maxLambda, sampling, rangeVar, thick, refArray, thickArray, series, waveAngle, checkMatrix):
    lambdaspace = np.linspace(minLambda, maxLambda, sampling)*rangeVar
    angles = np.array([waveAngle])

    A = Materiel(refArray[0], lambda0*thick, thickArray[0]*thick)
    B = Materiel(refArray[1], lambda0*thick, thickArray[1]*thick)
    C = Materiel(refArray[2], lambda0*thick, thickArray[2]*thick)
    D = Materiel(refArray[3], lambda0*thick, thickArray[3]*thick)
    E = Materiel(refArray[4], lambda0*thick, thickArray[4]*thick)
    F = Materiel(refArray[5], lambda0*thick, thickArray[5]*thick)
    air = Materiel(1, lambda0, 0)
    substrate = Materiel(refArray[6], lambda0, 0)

    materiels = [A, B, C, D, E, F]

    layers = TMMlib.makeLayers(series, materiels)
    structure = np.array([air])
    structure = np.append(structure, layers[:])
    structure = np.append(structure, substrate)

    resultR, resultT, resultA = TMMlib.resultTMM(structure, lambdaspace, angles, mode)
    drawGraph(resultR, resultT, resultA, checkMatrix, lambdaspace)

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

def drawGraph(resultR, resultT, resultA, checkMatrix, lambdaspace):
    sumMatrix = np.sum(checkMatrix)
    plt.figure(figsize=(8, 6), dpi=120)
    
    if sumMatrix == 1:
        if checkMatrix[0] == 1:
            plt.plot(lambdaspace, resultR[0,:])
            plt.xlabel("Wavelength")
            plt.ylabel("Reflectance")
        
        elif checkMatrix[1] == 1:
            plt.plot(lambdaspace, resultT[0,:])
            plt.xlabel("Wavelength")
            plt.ylabel("Transmittance")
        else:
            plt.plot(lambdaspace, resultA[0,:])
            plt.xlabel("Wavelength")
            plt.ylabel("Absorptance")

    elif sumMatrix == 2:
        if checkMatrix[0] == 1 and checkMatrix[1] == 1:
            plt.subplot(2,1,1)
            plt.plot(lambdaspace, resultR[0,:])
            plt.ylabel("Reflectance")
            plt.subplot(2,1,2)
            plt.plot(lambdaspace, resultT[0,:])
            plt.ylabel("Transmittance")
            plt.xlabel("Wavelength")
            
        elif checkMatrix[0] == 1 and checkMatrix[2] == 1:
            plt.subplot(2,1,1)
            plt.plot(lambdaspace, resultR[0,:])
            plt.ylabel("Reflectance")
            plt.subplot(2,1,2)
            plt.plot(lambdaspace, resultA[0,:])
            plt.ylabel("Absorptance")
            plt.xlabel("Wavelength")

        else:
            plt.subplot(2,1,1)
            plt.plot(lambdaspace, resultT[0,:])
            plt.ylabel("Transmittance")
            plt.subplot(2,1,2)
            plt.plot(lambdaspace, resultA[0,:])
            plt.ylabel("Absorptance")
            plt.xlabel("Wavelength")
    
    else:
        plt.subplot(3,1,1)
        plt.plot(lambdaspace, resultR[0,:])
        plt.ylabel("Reflectance")
        plt.subplot(3,1,2)
        plt.plot(lambdaspace, resultT[0,:])
        plt.ylabel("Transmittance")
        plt.subplot(3,1,3)
        plt.plot(lambdaspace, resultA[0,:])
        plt.ylabel("Absorptance")
        plt.xlabel("Wavelength")
    
    plt.show()