
import math
from tkinter import Canvas, Frame, OptionMenu, StringVar
from tkinter import Label, Button, Entry
from PIL.ImageTk import PhotoImage
from PIL import Image
from PIL.ImageDraw import Draw


def MandelBrotAlgoritm():
    
    maxHerhalingen = int(invoerMaxHerhalingen.get())
    xMiddel = float(invoerXCoord.get())
    yMiddel = float(invoerYCoord.get())
    schaal = float(invoerSchaal.get())
    
    
    (plaatjeX, plaatjeY) = plaatje.size
    xMin= -plaatjeX*schaal
    xMax= plaatjeX*schaal
    yMin= -plaatjeY*schaal
    yMax=plaatjeY*schaal
    
    print(f"xmin:{xMin}, xMax:{xMax}, yMin:{yMin}, yMax:{yMax}")
    for xCoord in range(int(xMin),int(xMax)):
        for yCoord in range(int(yMin),int(yMax)):
            MandelNumber = GetMandelNumber(xCoord, yCoord, maxHerhalingen)
            paintPixel(xCoord, yCoord, MandelNumber)
    global variabelePhotoImage
    variabelePhotoImage = PhotoImage(plaatje)
    afbeelding.configure(image=variabelePhotoImage)
   

def GetMandelNumber(x,y, maxHerhalingen):
    a=0
    b=0
    MandelNumber=1
    for i in range(maxHerhalingen):
        xCoord = (a * a) - (b * b) + x
        yCoord = ((2 * a) * b) + y
        afstandXenY = math.sqrt((xCoord * xCoord) + (yCoord * yCoord))
        maxAfstand = 2
        if(afstandXenY < maxAfstand):
            MandelNumber = MandelNumber + 1
            a=xCoord
            b=yCoord
        if(i == (maxHerhalingen-1)):
            return maxHerhalingen
        else:
            return MandelNumber
    
    
    
def paintPixel(xCoord, yCoord, MandelNumber):
    if(MandelNumber%2==0):
        draw.rectangle(((xCoord,yCoord),((xCoord+1),(yCoord+1))), ((0), (0), (0)))
    else:
        draw.rectangle(((xCoord,yCoord),((xCoord+1),(yCoord+1))), ((255), (255), (255)))


schermpje = Frame()
schermpje.master.title("Mandelbrood")
schermpje.configure(width=400, height=600)

tekstXCoord = Label (schermpje)
tekstYCoord = Label (schermpje)
tekstSchaal = Label (schermpje)
tekstMaxHerhalingen = Label (schermpje)

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

presetOptions = ["Test1", "Test2", "Test3"]
variable = StringVar(schermpje)
variable.set(presetOptions[0])
preset = OptionMenu(schermpje, variable, *presetOptions)
preset.place(x=300, y=20)

presetOptions = ["Zwart Wit", "Regenboog", "Kleur"]
variable = StringVar(schermpje)
variable.set(presetOptions[0])
preset = OptionMenu(schermpje, variable, *presetOptions)
preset.place(x=300, y=50)

knop = Button(schermpje)
knop.place(x=300,y=80)
knop.configure(text="bereken")
knop.configure(command=MandelBrotAlgoritm)

plaatje = Image.new(mode="RGBA", size=(400,400))
afbeelding = Label(schermpje)
afbeelding.place(x=0, y=200)
afbeelding.configure(background="white")
draw = Draw(plaatje)


schermpje.pack()
schermpje.mainloop()



