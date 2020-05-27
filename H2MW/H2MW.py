"""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           How 2 MultiWind - Wickelmaschinendemonstrator Anwendung
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 Index:
 Maschine 0 - Flechtmaschine
 Maschine 1 - Multifilamentwickelmaschine 90
 Maschine 2 - Mulftifilamentwickelmaschine 48
 Maschine 3 - Nasswickelmaschine

points = [20, 360, 130, 360, 80, 240, 60, 240]
points2 = [170, 360, 280, 360, 240, 240, 220, 240]
points3 = [60, 240, 150, 240, 100, 120]
points4 = [150, 240, 240, 240, 200, 120]
points5 = [100, 120, 150, 240, 200, 120, 150, 0]
points6 = [80, 240, 130, 360, 170, 360, 220, 240]

"""
# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
root = Tk()
root.title("MyApp")

" TO DO: Deklaration/Initialisierung der Parameter "

abfallProzentsatz = []  # Deklaration der Werte Listen
for i in range(4):
    abfallProzentsatz.append(IntVar())
recyclingAbsolut = []
for i in range(4):
    recyclingAbsolut.append(IntVar())
recyclingRelativ = []
for i in range(4):
    recyclingRelativ.append(DoubleVar())
verbrauchEnergie = []
for i in range(4):
    verbrauchEnergie.append(IntVar())
verbrauchMaterial = []
for i in range(4):
    verbrauchMaterial.append(IntVar())
kostenEffizienz = []
for i in range(4):
    kostenEffizienz.append(DoubleVar())
kostenAufwand = []
for i in range(4):
    kostenAufwand.append(IntVar())
zeitAufwand = []
for i in range(4):
    zeitAufwand.append(DoubleVar())
flexibilität = []
for i in range(4):
    flexibilität.append(IntVar())
zeitEffizienz = []
for i in range(4):
    zeitEffizienz.append(IntVar())
innovativität = []
for i in range(4):
    innovativität.append(IntVar())
flächenVerbrauch = []
for i in range(4):
    flächenVerbrauch.append(DoubleVar())

# Maschine 0


abfallProzentsatz[0].set(64)
recyclingAbsolut[0].set(1440)
recyclingRelativ[0].set(51.2)
verbrauchEnergie[0].set(2524)
verbrauchMaterial[0].set(1375)
kostenEffizienz[0].set(0.91)
kostenAufwand[0].set(40)
zeitAufwand[0].set(3.5)
flexibilität[0].set(5)
zeitEffizienz[0].set(3)
innovativität[0].set(4)
flächenVerbrauch[0].set(25.5)

# Maschine 1


abfallProzentsatz[1].set(90)
recyclingAbsolut[1].set(1440)
recyclingRelativ[1].set(53.5)
verbrauchEnergie[1].set(3051)
verbrauchMaterial[1].set(1250)
kostenEffizienz[1].set(2.56)
kostenAufwand[1].set(60)
zeitAufwand[1].set(1)
flexibilität[1].set(6)
zeitEffizienz[1].set(7)
innovativität[1].set(7)
flächenVerbrauch[1].set(55.5)

# Maschine 2


abfallProzentsatz[2].set(48)
recyclingAbsolut[2].set(1440)
recyclingRelativ[2].set(52.3)
verbrauchEnergie[2].set(3051)
verbrauchMaterial[2].set(1312)
kostenEffizienz[2].set(1.37)
kostenAufwand[2].set(60)
zeitAufwand[2].set(1.5)
flexibilität[2].set(5)
zeitEffizienz[2].set(6)
innovativität[2].set(6)
flächenVerbrauch[2].set(36.5)

# Maschine 3


abfallProzentsatz[3].set(10)
recyclingAbsolut[3].set(1440)
recyclingRelativ[3].set(51.8)
verbrauchEnergie[3].set(2524)
verbrauchMaterial[3].set(1337)
kostenEffizienz[3].set(0.28)
kostenAufwand[3].set(40)
zeitAufwand[3].set(2.5)
flexibilität[3].set(7)
zeitEffizienz[3].set(5)
innovativität[3].set(5)
flächenVerbrauch[3].set(25.5)

" TO DO: Checks für Gültigkeit der Werte im Verhältnis zu den erlaubten Grenzen "


def norm_wert(wert, wertList, min, max, mode: bool):  # normierte Wert Funktion
    if wert < min:
        print("Der von Ihnen gewählte Wert ist kleiner als das Minimum")
    elif wert > max:
        print("Der von Ihnen gewählte Wert ist größer als das Maximum")
    for x in range(4):
        if wertList[x].get() < min:
            if wertList[x].get() < 0:
                min = 0
            else:
                min = wertList[x].get()
        elif wertList[x].get() > max:
            max = wertList[x].get()
    if mode == 0:
        return (max - wert) / (max - min)
    else:
        return ((wert - min) / (max - min))


abfallProzentsatz_norm = []
for i in range(4):
    abfallProzentsatz_norm.append(DoubleVar())
recyclingAbsolut_norm = []
for i in range(4):
    recyclingAbsolut_norm.append(DoubleVar())
recyclingRelativ_norm = []  # Deklaration der normierten Werte
for i in range(4):
    recyclingRelativ_norm.append(DoubleVar())
verbrauchEnergie_norm = []
for i in range(4):
    verbrauchEnergie_norm.append(DoubleVar())
verbrauchMaterial_norm = []
for i in range(4):
    verbrauchMaterial_norm.append(DoubleVar())
kostenEffizienz_norm = []
for i in range(4):
    kostenEffizienz_norm.append(DoubleVar())
kostenAufwand_norm = []
for i in range(4):
    kostenAufwand_norm.append(DoubleVar())
zeitAufwand_norm = []
for i in range(4):
    zeitAufwand_norm.append(DoubleVar())
flexibilität_norm = []
for i in range(4):
    flexibilität_norm.append(DoubleVar())
zeitEffizienz_norm = []
for i in range(4):
    zeitEffizienz_norm.append(DoubleVar())
innovativität_norm = []
for i in range(4):
    innovativität_norm.append(DoubleVar())
flächenVerbrauch_norm = []
for i in range(4):
    flächenVerbrauch_norm.append(DoubleVar())

# Maschine 0-3


" TO DO: Ausrechnung der Nachhaltigkeitswerte "


def update1():
    for i in range(4):
        abfallProzentsatz_norm[i].set(norm_wert(abfallProzentsatz[i].get(), abfallProzentsatz, 10, 90, 0))
        recyclingAbsolut_norm[i].set(norm_wert(recyclingAbsolut[i].get(), recyclingAbsolut, 0, 1440, 1))
        recyclingRelativ_norm[i].set(norm_wert(recyclingRelativ[i].get(), recyclingRelativ, 51.2, 53.5, 1))
        verbrauchEnergie_norm[i].set(norm_wert(verbrauchEnergie[i].get(), verbrauchEnergie, 2524, 3051, 0))
        verbrauchMaterial_norm[i].set(norm_wert(verbrauchMaterial[i].get(), verbrauchMaterial, 1250, 1375, 1))
        kostenEffizienz_norm[i].set(norm_wert(kostenEffizienz[i].get(), kostenEffizienz, 0.28, 2.56, 0))
        kostenAufwand_norm[i].set(norm_wert(kostenAufwand[i].get(), kostenAufwand, 40, 60, 0))
        zeitAufwand_norm[i].set(norm_wert(zeitAufwand[i].get(), zeitAufwand, 1, 3.5, 0))
        flexibilität_norm[i].set(norm_wert(flexibilität[i].get(), flexibilität, 0, 8, 1))
        zeitEffizienz_norm[i].set(norm_wert(zeitEffizienz[i].get(), zeitEffizienz, 0, 8, 1))
        innovativität_norm[i].set(norm_wert(innovativität[i].get(), innovativität, 0, 8, 1))
        flächenVerbrauch_norm[i].set(norm_wert(flächenVerbrauch[i].get(), flächenVerbrauch, 25.5, 55.5, 0))

    print(norm_wert(abfallProzentsatz[0].get(), abfallProzentsatz, 10, 90, 0))
    root.after(1000, update1)


abfallProzentsatz_zg = []  # Deklaration der ZG Werte
for i in range(4):
    abfallProzentsatz_zg.append(DoubleVar())
recyclingAbsolut_zg = []
for i in range(4):
    recyclingAbsolut_zg.append(DoubleVar())
recyclingRelativ_zg = []
for i in range(4):
    recyclingRelativ_zg.append(DoubleVar())
verbrauchEnergie_zg = []
for i in range(4):
    verbrauchEnergie_zg.append(DoubleVar())
verbrauchMaterial_zg = []
for i in range(4):
    verbrauchMaterial_zg.append(DoubleVar())
kostenEffizienz_zg = []
for i in range(4):
    kostenEffizienz_zg.append(DoubleVar())
kostenAufwand_zg = []
for i in range(4):
    kostenAufwand_zg.append(DoubleVar())
zeitAufwand_zg = []
for i in range(4):
    zeitAufwand_zg.append(DoubleVar())
flexibilität_zg = []
for i in range(4):
    flexibilität_zg.append(DoubleVar())
zeitEffizienz_zg = []
for i in range(4):
    zeitEffizienz_zg.append(DoubleVar())
innovativität_zg = []
for i in range(4):
    innovativität_zg.append(DoubleVar())
flächenVerbrauch_zg = []
for i in range(4):
    flächenVerbrauch_zg.append(DoubleVar())

for i in range(4):
    abfallProzentsatz_zg[i].set((abfallProzentsatz_norm[i].get() % 0.5) * 4)
    recyclingAbsolut_zg[i].set((recyclingAbsolut_norm[i].get() % 0.5) * 4)
    recyclingRelativ_zg[i].set((recyclingRelativ_norm[i].get() % 0.5) * 4)
    verbrauchEnergie_zg[i].set((verbrauchEnergie_norm[i].get() % 0.5) * 4)
    verbrauchMaterial_zg[i].set((verbrauchMaterial_norm[i].get() % 0.5) * 4)
    kostenEffizienz_zg[i].set((kostenEffizienz_norm[i].get() % 0.5) * 4)
    kostenAufwand_zg[i].set((kostenAufwand_norm[i].get() % 0.5) * 5)
    zeitAufwand_zg[i].set((zeitAufwand_norm[i].get() % 0.5) * 4)
    flexibilität_zg[i].set((flexibilität_norm[i].get() % 0.5) * 4)
    zeitEffizienz_zg[i].set((zeitEffizienz_norm[i].get() % 0.5) * 4)
    innovativität_zg[i].set((innovativität_norm[i].get() % 0.5) * 4)
    flächenVerbrauch_zg[i].set((flächenVerbrauch_norm[i].get() % 0.5) * 4)

sozial_oekologisch = []
for i in range(4):
    sozial_oekologisch.append(DoubleVar())
oekologisch = []
for i in range(4):
    oekologisch.append(DoubleVar())
oekologisch_oekonomisch = []
for i in range(4):
    oekologisch_oekonomisch.append(DoubleVar())
oekonomisch = []
for i in range(4):
    oekonomisch.append(DoubleVar())
sozial_oekonomisch = []
for i in range(4):
    sozial_oekonomisch.append(DoubleVar())
sozial_oekologisch_oekonomisch = []
for i in range(4):
    sozial_oekologisch_oekonomisch.append(DoubleVar())


def dimension_rechnen(*argv):
    var = 1
    for arg in argv:
        var = var * (arg * arg + (1 - arg) * (1 - arg))
    return var


# Maschine 0


# Maschine 1


# Maschine 2


# Maschine 3


" Ausgabe der Nachhaltigkeitswerte"


# Maschine 0


# Maschine 1


# Maschine 2


# Maschine 3

def mywarWritten(*args):
    print("mywarWritten", abfallProzentsatz_norm[0].get())


test = StringVar()
test.set("test")

abfallProzentsatz_norm[0].trace("r", mywarWritten)


def pass_value():
    label['text'] = abfallProzentsatz[0].get()


def entry():
    text_entry = Entry(root, textvariable=abfallProzentsatz[0])
    text_entry.focus()
    text_entry.pack()
    text_entry.bind("<Return>", lambda x: pass_value())
    label = Label(root, textvariable=test)
    label.pack()
    return text_entry, label


text_entry, label = entry()

root.after(1000, update1)
root.mainloop()
