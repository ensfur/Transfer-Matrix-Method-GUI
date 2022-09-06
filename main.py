from glob import glob
from pydoc import locate
import tkinter as tk
from tkinter import DISABLED, OptionMenu, StringVar
from tkinter import IntVar
from click import command
from sympy import false
import numpy as np
import threading
import guiLib
import tkinter.font as tkFont


def parameterWindow():
    paramPopUp = tk.Toplevel(form)
    paramPopUp.iconbitmap('icon.ico')
    paramPopUp.title("Parameters of Materials")
    paramPopUp.geometry("500x500-2080+200")

    paramSaveButton = tk.Button(paramPopUp, text="Save Parameters", bg="red", font="Times 12 bold", command=saveParam)

    #Label
    paramTitle = tk.Label(paramPopUp, text="Enter Parameters")
    refractiveTitle = tk.Label(paramPopUp, text="Refractive Index")
    thicknessTitle = tk.Label(paramPopUp, text="Thickness")
    lambdaTitle = tk.Label(paramPopUp, text="Centeral Wavelength")
    ATitle = tk.Label(paramPopUp, text="A")
    BTitle = tk.Label(paramPopUp, text="B")
    CTitle = tk.Label(paramPopUp, text="C")
    DTitle = tk.Label(paramPopUp, text="D")
    ETitle = tk.Label(paramPopUp, text="E")
    FTitle = tk.Label(paramPopUp, text="F")
    subTitle = tk.Label(paramPopUp, text="Substrate")

    # Refractive Entry
    global ARefText
    global BRefText
    global CRefText
    global DRefText
    global ERefText
    global FRefText
    global subRefText
    ARefText = tk.Entry(paramPopUp)
    BRefText = tk.Entry(paramPopUp)
    CRefText = tk.Entry(paramPopUp)
    DRefText = tk.Entry(paramPopUp)
    ERefText = tk.Entry(paramPopUp)
    FRefText = tk.Entry(paramPopUp)
    subRefText = tk.Entry(paramPopUp)

    # Thickness Entry
    global AThickText
    global BThickText
    global CThickText
    global DThickText
    global EThickText
    global FThickText
    AThickText = tk.Entry(paramPopUp)
    BThickText = tk.Entry(paramPopUp)
    CThickText = tk.Entry(paramPopUp)
    DThickText = tk.Entry(paramPopUp)
    EThickText = tk.Entry(paramPopUp)
    FThickText = tk.Entry(paramPopUp)

    # Lambda0 Entry
    global lambdaText
    lambdaText = tk.Entry(paramPopUp)

    # Hint Text
    ARefText.insert(0, "1")
    ARefText.configure(state=DISABLED)
    y_focus_in = ARefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(ARefText))
    y_focus_out = ARefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(ARefText, '1'))

    # Hint Text
    BRefText.insert(0, "1")
    BRefText.configure(state=DISABLED)
    y_focus_in = BRefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(BRefText))
    y_focus_out = BRefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(BRefText, '1'))

    # Hint Text
    CRefText.insert(0, "1")
    CRefText.configure(state=DISABLED)
    y_focus_in = CRefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(CRefText))
    y_focus_out = CRefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(CRefText, '1'))


    # Hint Text
    DRefText.insert(0, "1")
    DRefText.configure(state=DISABLED)
    y_focus_in = DRefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(DRefText))
    y_focus_out = DRefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(DRefText, '1'))

    # Hint Text
    ERefText.insert(0, "1")
    ERefText.configure(state=DISABLED)
    y_focus_in = ERefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(ERefText))
    y_focus_out = ERefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(ERefText, '1'))

    # Hint Text
    FRefText.insert(0, "1")
    FRefText.configure(state=DISABLED)
    y_focus_in = FRefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(FRefText))
    y_focus_out = FRefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(FRefText, '1'))

    # Hint Text
    subRefText.insert(0, "1")
    subRefText.configure(state=DISABLED)
    y_focus_in = subRefText.bind('<Button-1>', lambda x: guiLib.on_focus_in(subRefText))
    y_focus_out = subRefText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(subRefText, '1'))

    # Hint Text
    AThickText.insert(0, "-1")
    AThickText.configure(state=DISABLED)
    y_focus_in = AThickText.bind('<Button-1>', lambda x: guiLib.on_focus_in(AThickText))
    y_focus_out = AThickText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(AThickText, '-1'))

    # Hint Text
    BThickText.insert(0, "-1")
    BThickText.configure(state=DISABLED)
    y_focus_in = BThickText.bind('<Button-1>', lambda x: guiLib.on_focus_in(BThickText))
    y_focus_out = BThickText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(BThickText, '-1'))

    # Hint Text
    CThickText.insert(0, "-1")
    CThickText.configure(state=DISABLED)
    y_focus_in = CThickText.bind('<Button-1>', lambda x: guiLib.on_focus_in(CThickText))
    y_focus_out = CThickText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(CThickText, '-1'))

    # Hint Text
    DThickText.insert(0, "-1")
    DThickText.configure(state=DISABLED)
    y_focus_in = DThickText.bind('<Button-1>', lambda x: guiLib.on_focus_in(DThickText))
    y_focus_out = DThickText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(DThickText, '-1'))

    # Hint Text
    EThickText.insert(0, "-1")
    EThickText.configure(state=DISABLED)
    y_focus_in = EThickText.bind('<Button-1>', lambda x: guiLib.on_focus_in(EThickText))
    y_focus_out = EThickText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(EThickText, '-1'))

    # Hint Text
    FThickText.insert(0, "-1")
    FThickText.configure(state=DISABLED)
    y_focus_in = FThickText.bind('<Button-1>', lambda x: guiLib.on_focus_in(FThickText))
    y_focus_out = FThickText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(FThickText, '-1'))

    # Thickness List
    thicknessList = ["m", "mm", "um", "nm"]
    global thicknessVar
    thicknessVar = StringVar(paramPopUp)
    thicknessVar.set(thicknessList[0]) #default value "m"

    # Menu for Thickness
    AThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    AThicknessMenu.place(relx=0.85, rely=0.17)
    BThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    BThicknessMenu.place(relx=0.85, rely=0.27)
    CThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    CThicknessMenu.place(relx=0.85, rely=0.37)
    DThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    DThicknessMenu.place(relx=0.85, rely=0.47)
    EThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    EThicknessMenu.place(relx=0.85, rely=0.57)
    FThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    FThicknessMenu.place(relx=0.85, rely=0.67)
    lambdaThicknessMenu = OptionMenu(paramPopUp, thicknessVar, *thicknessList)
    lambdaThicknessMenu.place(relx=0.65, rely=0.84)

    ### Popup Desing
    # Label Design
    paramTitle.pack()
    ATitle.place(relx=0.05, rely=0.18)
    BTitle.place(relx=0.05, rely=0.28)
    CTitle.place(relx=0.05, rely=0.38)
    DTitle.place(relx=0.05, rely=0.48)
    ETitle.place(relx=0.05, rely=0.58)
    FTitle.place(relx=0.05, rely=0.68)
    subTitle.place(relx=0.05, rely=0.78)
    refractiveTitle.place(relx=0.25, rely=0.08)
    thicknessTitle.place(relx=0.6, rely=0.08)
    lambdaTitle.place(relx=0.12, rely=0.85)

    # Refractive Entry Design
    ARefText.place(relx=0.25, rely=0.18)
    BRefText.place(relx=0.25, rely=0.28)
    CRefText.place(relx=0.25, rely=0.38)
    DRefText.place(relx=0.25, rely=0.48)
    ERefText.place(relx=0.25, rely=0.58)
    FRefText.place(relx=0.25, rely=0.68)
    subRefText.place(relx=0.25, rely=0.78)

    # Refractive Entry Design
    AThickText.place(relx=0.6, rely=0.18)
    BThickText.place(relx=0.6, rely=0.28)
    CThickText.place(relx=0.6, rely=0.38)
    DThickText.place(relx=0.6, rely=0.48)
    EThickText.place(relx=0.6, rely=0.58)
    FThickText.place(relx=0.6, rely=0.68)

    # Lambda0 Entry Design
    lambdaText.place(relx=0.4, rely=0.85)
    paramSaveButton.place(relx=0.35, rely=0.92)


def saveDesign():
    mixText = designText.get()
    global fixText
    fixText = guiLib.setMixText(mixText)

def saveRange():
    global minValue
    global maxValue
    minValue = float(minLambda.get())
    maxValue = float(maxLambda.get())

def saveSampling():
    global samplingNum
    samplingNum = int(samplingEnter.get())

def saveAngle():
    global angleInDegree
    angleInDegree = float(angleEntry.get())

def saveParam():
    # Global Variables
    global centeralWave
    global refList
    global thickList

    # Convert string to float number
    ARef = complex(ARefText.get())
    BRef = complex(BRefText.get())
    CRef = complex(CRefText.get())
    DRef = complex(DRefText.get())
    ERef = complex(ERefText.get())
    FRef = complex(FRefText.get())
    SubRef = complex(subRefText.get())

    AThick = float(AThickText.get())
    BThick = float(BThickText.get())
    CThick = float(CThickText.get())
    DThick = float(DThickText.get())
    EThick = float(EThickText.get())
    FThick = float(FThickText.get())
    centeralWave = float(lambdaText.get())

    refList = np.array([ARef, BRef, CRef, DRef, ERef, FRef, SubRef])
    thickList = np.array([AThick, BThick, CThick, DThick, EThick, FThick])

def finalCalculation():
    threading.Thread(guiLib.calculate(modeVar.get(), centeralWave, minValue, maxValue,
                                    samplingNum, rangeVar, thick, refList, thickList, 
                                    fixText, angleInDegree, checkMatrix)).start

def calculation():
    global thick
    global rangeVar
    global checkMatrix

    checkMatrix = np.array([checkRefVar.get(), checkTransVar.get(), checkAbsVar.get()])

    if thicknessVar.get() == "m":
        thick = 1
    elif thicknessVar.get() == "mm":
        thick = 10**-3
    elif thicknessVar.get() == "um":
        thick = 10**-6
    else:
        thick = 10**-9

    if waveRangeVar.get() == "m":
        rangeVar = 1
    elif waveRangeVar.get() == "mm":
        rangeVar = 10**-3
    elif waveRangeVar.get() == "um":
        rangeVar = 10**-6
    else:
        rangeVar = 10**-9
    
    finalCalculation()

# Create Main Window
form = tk.Tk()
form.iconbitmap('icodeneme.ico')
form.title("GRADUATION PROJECT")
form.geometry("1600x800+100+100")
form.resizable(false, false)

# Defination of Variable
checkRefVar = IntVar()
checkTransVar = IntVar()
checkAbsVar = IntVar()
modeVar = StringVar(form)
waveRangeVar = StringVar(form)

# Create Label, Button, Entry Place....
titleLabel = tk.Label(form, text="Multilayer Structure Design", font="Times 30 bold")
modeLabel = tk.Label(form, text="Choose Propagation Mode", font="Times 20 bold")
angleLabel = tk.Label(form, text="Enter Angle in Degree", font="Times 20 bold")
designText = tk.Entry(font=("Times 15 bold"))
saveDesignButton = tk.Button(form, text="Save The Design", fg="white", bg="blue", font="Times 20 bold", command=saveDesign)
drawButton = tk.Button(form, text="Calculate", fg="white", bg="blue", font="Times 25 bold", command=calculation)
paramButton = tk.Button(form, text="Click to Enter Parameters", fg="white", bg="green", font="Times 20 bold", command=parameterWindow)
refCheck = tk.Checkbutton(form, text="Reflectance", variable=checkRefVar, onvalue=1, offvalue=0, font="Times 15 bold")
transCheck = tk.Checkbutton(form, text="Transmittance", variable=checkTransVar, onvalue=1, offvalue=0, font="Times 15 bold")
absCheck = tk.Checkbutton(form, text="Absorption", variable=checkAbsVar, onvalue=1, offvalue=0, font="Times 15 bold")
minMaxText = tk.Label(form, text="Enter Minimum and Maximum\nWavelength Range", font="Times 20 bold")
minLambda = tk.Entry(font="Times 15 bold")
maxLambda = tk.Entry(font="Times 15 bold")
angleEntry = tk.Entry(font="Times 15 bold")
saveRangeButton = tk.Button(form, text="Save Range", fg="white", bg="blue", font="Times 20 bold", command=saveRange)
samplingText = tk.Label(form, text="Enter Sampling Number", font="Times 20 bold")
samplingEnter = tk.Entry(font="Times 15 bold")
saveSamplingButton = tk.Button(form, text="Save Sampling", fg="white", bg="blue", font="Times 20 bold", command=saveSampling)
graphText = tk.Label(form, text="Choose Graphic", font="Times 20 bold")
saveAngleButton = tk.Button(form, text="Save Angle", fg="white", bg="blue", font="Times 20 bold", command=saveAngle)

# Mode Menu
modeList = ["TE", "TM"]
modeVar.set(modeList[0])                            #default value "TE"
modeMenu = OptionMenu(form, modeVar, *modeList)
modeMenu.config(font = "Times 20 bold", width=10)
modeMenu.place(relx=0.68, rely=0.61)
helv20 = tkFont.Font(family='Helvetica', size=20)
menuSize = form.nametowidget(modeMenu.menuname)     # Get menu widget.
menuSize.config(font="Times 20")

# Range Menu
waveRangeList = ["m", "mm", "um", "nm"]
waveRangeVar.set(waveRangeList[0])                  #default value "m"
rangeMenu = OptionMenu(form, waveRangeVar, *waveRangeList)
rangeMenu.config(font = "Times 15 bold")
rangeMenu.place(relx=0.295, rely=0.475)

# Hint Text
designText.insert(0, "Enter Your Design")
designText.configure(state=DISABLED)
y_focus_in = designText.bind('<Button-1>', lambda x: guiLib.on_focus_in(designText))
y_focus_out = designText.bind('<FocusOut>', lambda x: guiLib.on_focus_out(designText, 'Enter Your Design'))

# Hint Text
angleEntry.insert(0, "Angle")
angleEntry.configure(state=DISABLED)
y_focus_in = angleEntry.bind('<Button-1>', lambda x: guiLib.on_focus_in(angleEntry))
y_focus_out = angleEntry.bind('<FocusOut>', lambda x: guiLib.on_focus_out(angleEntry, 'Angle'))

# Hint Text
minLambda.insert(0, "Min Wavelength")
minLambda.configure(state=DISABLED)
y_focus_in = minLambda.bind('<Button-1>', lambda x: guiLib.on_focus_in(minLambda))
y_focus_out = minLambda.bind('<FocusOut>', lambda x: guiLib.on_focus_out(minLambda, 'Min Wavelength'))

# Hint Text
maxLambda.insert(0, "Max Wavelength")
maxLambda.configure(state=DISABLED)
y_focus_in = maxLambda.bind('<Button-1>', lambda x: guiLib.on_focus_in(maxLambda))
y_focus_out = maxLambda.bind('<FocusOut>', lambda x: guiLib.on_focus_out(maxLambda, 'Max Wavelength'))

# Hint Text
samplingEnter.insert(0, "Sampling Number")
samplingEnter.configure(state=DISABLED)
y_focus_in = samplingEnter.bind('<Button-1>', lambda x: guiLib.on_focus_in(samplingEnter))
y_focus_out = samplingEnter.bind('<FocusOut>', lambda x: guiLib.on_focus_out(samplingEnter, 'Sampling Number'))

# Place of Object
designText.place(relx = 0.05, rely = 0.2, width = 468, height = 45)
modeLabel.place(relx=0.64, rely=0.56)
titleLabel.pack(anchor="n")
saveDesignButton.place(relx = 0.12, rely = 0.27)
drawButton.place(relx = 0.43, rely = 0.87)
paramButton.place(relx = 0.6, rely = 0.22, width=450, height=100)
refCheck.place(relx=0.67, rely=0.74)
transCheck.place(relx=0.67, rely=0.79)
absCheck.place(relx=0.67, rely=0.84)
minMaxText.place(relx=0.08, rely=0.37)
minLambda.place(relx=0.05, rely=0.47, width=180, height=45)
maxLambda.place(relx=0.18, rely=0.47, width=180, height=45)
saveRangeButton.place(relx = 0.135, rely = 0.54)
samplingText.place(relx=0.09, rely=0.64)
samplingEnter.place(relx=0.12, rely=0.69, width=200, height=45)
saveSamplingButton.place(relx=0.12, rely=0.76, width=200)
graphText.place(relx=0.67, rely=0.69)
angleLabel.place(relx=0.67, rely=0.37)
angleEntry.place(relx=0.67, rely=0.42, width=180, height=45)
saveAngleButton.place(relx=0.67, rely=0.49, width=180)


form.mainloop()

