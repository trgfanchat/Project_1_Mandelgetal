
from tkinter import BUTT, Canvas, Frame, OptionMenu, StringVar
from tkinter import Label, Button, Entry
from PIL.ImageTk import PhotoImage
from PIL import Image
from PIL.ImageDraw import Draw

def Mantelbrot(a, b):
    x = a * a - b * b + x
    y = 2 * a * b + y
    BerekenAfstand(x,y)
    
def BerekenAfstand(x, y):    
    afstandXenY = x*x + y*y
    maxAfstand = 2
    if(afstandXenY < maxAfstand*maxAfstand):
        paintPixel(x, y)
    else:
        return


def paintPixel(xCoord, yCoord):
    Canvas.create_rectangle(xCoord, yCoord, xCoord, yCoord ,outline="black")     


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

knop = Button(schermpje)
knop.place(x=300,y=80)
knop.configure(text="bereken")

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

plaatje = Image.new(mode="RGBA", size=(600,480))
afbeelding = Label(schermpje)
afbeelding.place(x=0, y=120)
afbeelding.configure(background="white")
draw = Draw(plaatje)
omgezetPlaatje = PhotoImage(plaatje)
afbeelding.configure(image=omgezetPlaatje)


knop.configure(command=BerekenAfstand)
schermpje.pack()
schermpje.mainloop()

global mantelGetal
mantelGetal = 0



