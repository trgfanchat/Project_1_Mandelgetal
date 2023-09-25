import math
import numpy as np
from tkinter import Frame, OptionMenu, StringVar
from tkinter import Label, Button, Entry
from PIL.ImageTk import PhotoImage
from PIL import Image
from PIL.ImageDraw import Draw


def MandelBrotAlgoritm():
    
    maxHerhalingen = int(invoerMaxHerhalingen.get())
    xMiddel = float(invoerXCoord.get())
    yMiddel = float(invoerYCoord.get())
    schaal = float(invoerSchaal.get())
    colorPattern= variableKleurenschema.get()
    
    print(plaatje.size)
    (plaatjeX, plaatjeY) = plaatje.size
    xMin= (-plaatjeX*schaal)/2
    xMax= (plaatjeX*schaal)/2
    yMin= (-plaatjeY*schaal)/2
    yMax=(plaatjeY*schaal)/2
    
    print(f"xmin:{xMin}, xMax:{xMax}, yMin:{yMin}, yMax:{yMax}")
    for xCoord in np.arange(float(xMin),float(xMax), schaal):
        for yCoord in np.arange(float(yMin),float(yMax), schaal):
            MandelNumber = GetMandelNumber(float(xCoord), float(yCoord), maxHerhalingen)
            paintPixel((xCoord+xMax), (yCoord+yMax), MandelNumber, schaal, colorPattern)
    global variabelePhotoImage
    variabelePhotoImage = PhotoImage(plaatje)
    afbeelding.configure(image=variabelePhotoImage)

def PresetMandelBrot(maxHerhalingen, xMiddel, yMiddel, schaal, colorPattern):
        
    maxHerhalingenVar = maxHerhalingen
    xMiddelVar = xMiddel
    yMiddel = yMiddel
    schaalVar = schaal
    colorPatternVar = colorPattern
    
    (plaatjeX, plaatjeY) = plaatje.size
    xMin= (-plaatjeX*schaalVar)/2
    xMax= (plaatjeX*schaalVar)/2
    yMin= (-plaatjeY*schaalVar)/2
    yMax=(plaatjeY*schaalVar)/2
    
    print(f"xmin:{xMin}, xMax:{xMax}, yMin:{yMin}, yMax:{yMax}")
    for xCoord in np.arange(float(xMin),float(xMax), schaalVar):
        for yCoord in np.arange(float(yMin),float(yMax), schaalVar):
            MandelNumber = GetMandelNumber(float(xCoord), float(yCoord), maxHerhalingenVar)
            paintPixel((xCoord+xMax), (yCoord+yMax), MandelNumber, schaalVar, colorPatternVar)
    global variabelePhotoImage
    variabelePhotoImage = PhotoImage(plaatje)
    afbeelding.configure(image=variabelePhotoImage)
   

def GetMandelNumber(x,y, maxHerhalingen):
    a=0
    b=0
    MandelNumber=1
    for i in range(maxHerhalingen):
        xCoord = (a * a) - (b * b) + float(x)
        yCoord = (2 * a * b) + float(y)
        afstandXenY = (xCoord * xCoord) + (yCoord * yCoord)
        maxAfstand = 2
        if(afstandXenY < (maxAfstand * maxAfstand)):
            MandelNumber = MandelNumber + 1
            a=xCoord
            b=yCoord
            if(i == (maxHerhalingen-1)):
                # het maakt niet uit welk getal dit is, zolang het maar een even getal is!
                MandelNumber = 0
                return MandelNumber
        else:
            return MandelNumber
    
    
    
def paintPixel(xCoord, yCoord, MandelNumber, schaal, colorPattern):
    if(colorPattern==("zwart en wit")):
        if(MandelNumber%2==0):    
            draw.rectangle(((((xCoord/schaal),(yCoord/schaal))),((((xCoord+1)/schaal)),((yCoord+1)/schaal))), ((0), (0), (0)))
        else:        
            draw.rectangle(((((xCoord/schaal),(yCoord/schaal))),((((xCoord+1)/schaal)),((yCoord+1)/schaal))), ((255), (255), (255)))
    elif(colorPattern==("blauw")):
            draw.rectangle(((((xCoord/schaal),(yCoord/schaal))),((((xCoord+1)/schaal)),((yCoord+1)/schaal))), ((MandelNumber+50), (MandelNumber+100), (MandelNumber+150)))
    elif(colorPattern==("test2")):
            draw.rectangle(((((xCoord/schaal),(yCoord/schaal))),((((xCoord+1)/schaal)),((yCoord+1)/schaal))), ((MandelNumber+150), (MandelNumber+100), (MandelNumber+50)))
    elif():
        pass
        


schermpje = Frame()
schermpje.master.title("Mandelbrood")
schermpje.configure(width=400, height=600)

tekstXCoord = Label (schermpje)
tekstYCoord = Label (schermpje)
tekstSchaal = Label (schermpje)
tekstMaxHerhalingen = Label (schermpje)
tekstPresetOpties = Label (schermpje)
tekstKleurenSchemaOpties = Label (schermpje)

invoerXCoord = Entry (schermpje)
invoerYCoord = Entry (schermpje)
invoerSchaal = Entry (schermpje)
invoerMaxHerhalingen = Entry (schermpje)

tekstXCoord.place(x=20, y=20)
tekstXCoord.configure(text="X midden:")
invoerXCoord.place(x=150, y=20)
invoerXCoord.configure(width=20)
 
tekstYCoord.place(x=20, y=40)
tekstYCoord.configure(text="Y midden:")
invoerYCoord.place(x=150, y=40)
invoerYCoord.configure(width=20)

tekstSchaal.place(x=20, y=60)
tekstSchaal.configure(text="schaal")
invoerSchaal.place (x=150, y=60)
invoerSchaal.configure(width=20)

tekstMaxHerhalingen.place(x=20, y=80)
tekstMaxHerhalingen.configure(text="maximale herhalingen")
invoerMaxHerhalingen.place(x=150, y=80)
invoerMaxHerhalingen.configure(width=20)

tekstPresetOpties.place(x=20, y=175)
tekstPresetOpties.configure(text="Presets:")

tekstKleurenSchemaOpties.place(x=20, y=103)
tekstKleurenSchemaOpties.configure(text="Kleurenschema:")


presetsOpties = ["standaard", "Test2", "Test3"]
variablePresets = StringVar(schermpje)
variablePresets.set(presetsOpties[0])
presets_dropdown = OptionMenu(schermpje, variablePresets, *presetsOpties)
presets_dropdown.place(x=63, y=170)

kleurenschemaOpties = ["zwart en wit", "blauw", "test2"]
variableKleurenschema = StringVar(schermpje)
variableKleurenschema.set(kleurenschemaOpties[0])
kleurenschema_dropdown = OptionMenu(schermpje, variableKleurenschema, *kleurenschemaOpties)
kleurenschema_dropdown.place(x=150, y=100)

knop = Button(schermpje)
knop.place(x=150,y=135)
knop.configure(text="bereken")
knop.configure(command=MandelBrotAlgoritm)

plaatje = Image.new(mode="RGBA", size=(400,400))
afbeelding = Label(schermpje)
afbeelding.place(x=0, y=200)
afbeelding.configure(background="white")
draw = Draw(plaatje)
PresetMandelBrot(100, 0, 0, 0.01, "zwart en wit")


schermpje.pack()
schermpje.mainloop()


