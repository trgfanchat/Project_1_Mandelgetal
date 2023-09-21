
import math
from tkinter import Canvas, Frame, OptionMenu, StringVar
from tkinter import Label, Button, Entry
from PIL.ImageTk import PhotoImage
from PIL import Image
from PIL.ImageDraw import Draw


def MandelBrotAlgoritm():
    GetMandelNumber()

def GetMandelNumber():
    x = float(invoerXCoord. get())
    y = float(invoerYCoord.get())
    maxHerhalingen = int(invoerMaxHerhalingen.get())
    a=0
    b=0
    MandelNumber=1
    for i in range(maxHerhalingen):
        MandelNumber = MandelNumber + 1
        xCoord = (a * a) - (b * b) + x
        yCoord = ((2 * a) * b) + y
        afstandXenY = math.sqrt((xCoord * xCoord) + (yCoord * yCoord))
        maxAfstand = 2
        if(afstandXenY < maxAfstand):
            a=xCoord
            b=yCoord
        else:
            variabelePhotoImage = PhotoImage(plaatje)
            afbeelding.configure(image=variabelePhotoImage)
            print(f"{MandelNumber}")
            break
    
    
    
def paintPixel(xCoord, yCoord):
    draw.rectangle(((xCoord, yCoord), (xCoord, yCoord)) ,outline="black")     


schermpje = Frame()
schermpje.master.title("Mandelbrood")
schermpje.configure(width=500, height=600)

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

plaatje = Image.new(mode="RGBA", size=(600,480))
afbeelding = Label(schermpje)
afbeelding.place(x=0, y=120)
afbeelding.configure(background="white")
draw = Draw(plaatje)

variabelePhotoImage = PhotoImage(plaatje)
afbeelding.configure(image=variabelePhotoImage)
schermpje.pack()
schermpje.mainloop()



