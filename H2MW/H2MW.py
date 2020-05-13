"""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           How 2 MultiWind - Wickelmaschinendemonstrator Anwendung
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 Index:
 Maschine 0 - Flechtmaschine
 Maschine 1 - Multifilamentwickelmaschine 90
 Maschine 2 - Mulftifilamentwickelmaschine 48
 Maschine 3 - Nasswickelmaschine

"""
# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
master = Tk()

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

abfallProzentsatz_zg = []   # Deklaration der ZG Werte
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

for i in range (4):
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

#get hinzufügen
'''
def dimension_rechnen(*argv):
    var = 1
    for arg in argv:
        var = var * (arg * arg + (1 - arg) * (1 - arg))
    return var
for i in range(4):
    sozial_oekologisch[i].set(dimension_rechnen())
    oekologisch[i].set(dimension_rechnen(abfallProzentsatz_zg[i], recyclingAbsolut_zg[i], recyclingRelativ_zg[i]))
    oekologisch_oekonomisch[i].set(dimension_rechnen(verbrauchEnergie_zg[i], verbrauchMaterial_zg[i], kostenEffizienz_zg[i], kostenAufwand_zg[i]))
    oekonomisch[i].set(dimension_rechnen(zeitAufwand_zg[i], flexibilität_zg[i], zeitEffizienz_zg[i]))
    sozial_oekologisch[i].set(dimension_rechnen())
    sozial_oekologisch_oekonomisch[i].set(dimension_rechnen(innovativität_zg[i], flächenVerbrauch_zg[i]))
    '''




master = Tk()


'''
Sozial_Ökologisch = Frame(master)

button_1_1 = Label(Sozial_Ökologisch, text = "Flechtwickelmaschine")
button_1_2 = Label(Sozial_Ökologisch, text = "Multifilamentwickelmaschine90")
button_1_3 = Label(Sozial_Ökologisch, text = "Multifilamentwickelmaschine48")
button_1_4 = Label(Sozial_Ökologisch, text = "Nasswickelmaschine")



label_1_1 = Label(Sozial_Ökologisch, text ="      Anteil giftige Emissionen/Abfälle")
label_1_2 = Label(Sozial_Ökologisch, text = "Einsatz giftiger/kritischer Materialien")
label_2_1 = Label(Sozial_Ökologisch, text ="      Anteil giftige Emissionen/Abfälle")
label_2_2 = Label(Sozial_Ökologisch, text = "Einsatz giftiger/kritischer Materialien")
label_3_1 = Label(Sozial_Ökologisch, text ="      Anteil giftige Emissionen/Abfälle")
label_3_2 = Label(Sozial_Ökologisch, text = "Einsatz giftiger/kritischer Materialien")
label_4_1 = Label(Sozial_Ökologisch, text ="      Anteil giftige Emissionen/Abfälle")
label_4_2 = Label(Sozial_Ökologisch, text = "Einsatz giftiger/kritischer Materialien")



entry_1_1 = Entry(Sozial_Ökologisch)
entry_1_2 = Entry(Sozial_Ökologisch)
entry_2_1 = Entry(Sozial_Ökologisch)
entry_2_2 = Entry(Sozial_Ökologisch)
entry_3_1 = Entry(Sozial_Ökologisch)
entry_3_2 = Entry(Sozial_Ökologisch)
entry_4_1 = Entry(Sozial_Ökologisch)
entry_4_2 = Entry(Sozial_Ökologisch)



button_1_1.grid(row = 0, column = 1)
button_1_2.grid(row = 0, column = 6)
button_1_3.grid(row = 6, column = 1)
button_1_4.grid(row = 6, column = 6)


label_1_1.grid(row = 1, column = 0)
label_1_2.grid(row = 2, column = 0)
label_2_1.grid(row = 1, column = 5)
label_2_2.grid(row = 2, column = 5)
label_3_1.grid(row = 7, column = 0)
label_3_2.grid(row = 8, column = 0)
label_4_1.grid(row = 7, column = 5)
label_4_2.grid(row = 8, column = 5)

entry_1_1.grid(row = 1, column = 1)
entry_1_2.grid(row = 2, column = 1)
entry_2_1.grid(row = 1, column = 6)
entry_2_2.grid(row = 2, column = 6)
entry_3_1.grid(row = 7, column = 1)
entry_3_2.grid(row = 8, column = 1)
entry_4_1.grid(row = 7, column = 6)
entry_4_2.grid(row = 8, column = 6)


Sozial_Ökologisch.grid()




Ökologisch = Frame(master)

button_1_1 = Label(Ökologisch, text = "Flechtwickelmaschine")
button_1_2 = Label(Ökologisch, text = "Multifilamentwickelmaschine90")
button_1_3 = Label(Ökologisch, text = "Multifilamentwickelmaschine48")
button_1_4 = Label(Ökologisch, text = "Nasswickelmaschine")


label_1_1 = Label (Ökologisch, text = "Abfall")
label_1_2 = Label (Ökologisch, text = "Abfallszenarien")
label_1_3 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Asolut)")
label_1_4 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Relativ)")
label_2_1 = Label (Ökologisch, text = "Abfall")
label_2_2 = Label (Ökologisch, text = "Abfallszenarien")
label_2_3 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Asolut)")
label_2_4 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Relativ)")
label_3_1 = Label (Ökologisch, text = "Abfall")
label_3_2 = Label (Ökologisch, text = "Abfallszenarien")
label_3_3 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Asolut)")
label_3_4 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Relativ)")
label_4_1 = Label (Ökologisch, text = "Abfall")
label_4_2 = Label (Ökologisch, text = "Abfallszenarien")
label_4_3 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Asolut)")
label_4_4 = Label (Ökologisch, text = "Anteil verwendetes Recyclingmaterial(Relativ)")

entry_1_1 = Entry(Ökologisch)
entry_1_2 = Entry(Ökologisch)
entry_1_3 = Entry(Ökologisch)
entry_1_4 = Entry(Ökologisch)
entry_2_1 = Entry(Ökologisch)
entry_2_2 = Entry(Ökologisch)
entry_2_3 = Entry(Ökologisch)
entry_2_4 = Entry(Ökologisch)
entry_3_1 = Entry(Ökologisch)
entry_3_2 = Entry(Ökologisch)
entry_3_3 = Entry(Ökologisch)
entry_3_4 = Entry(Ökologisch)
entry_4_1 = Entry(Ökologisch)
entry_4_2 = Entry(Ökologisch)
entry_4_3 = Entry(Ökologisch)
entry_4_4 = Entry(Ökologisch)

button_1_1.grid(row = 0, column = 1)
button_1_2.grid(row = 0, column = 4)
button_1_3.grid(row = 7, column = 1)
button_1_4.grid(row = 7, column = 4)


label_1_1.grid(row = 1, column = 0)
label_1_2.grid(row = 2, column = 0)
label_1_3.grid(row = 3, column = 0)
label_1_4.grid(row = 4, column = 0)
label_2_1.grid(row = 1, column = 3)
label_2_2.grid(row = 2, column = 3)
label_2_3.grid(row = 3, column = 3)
label_2_4.grid(row = 4, column = 3)
label_3_1.grid(row = 8, column = 0)
label_3_2.grid(row = 9, column = 0)
label_3_3.grid(row = 10, column = 0)
label_3_4.grid(row = 11, column = 0)
label_4_1.grid(row = 8, column = 3)
label_4_2.grid(row = 9, column = 3)
label_4_3.grid(row = 10, column = 3)
label_4_4.grid(row = 11, column = 3)


entry_1_1.grid(row = 1, column = 1)
entry_1_2.grid(row = 2, column = 1)
entry_1_3.grid(row = 3, column = 1)
entry_1_4.grid(row = 4, column = 1)
entry_2_1.grid(row = 1, column = 4)
entry_2_2.grid(row = 2, column = 4)
entry_2_3.grid(row = 3, column = 4)
entry_2_4.grid(row = 4, column = 4)
entry_3_1.grid(row = 8, column = 1)
entry_3_2.grid(row = 9, column = 1)
entry_3_3.grid(row = 10, column = 1)
entry_3_4.grid(row = 11, column = 1)
entry_4_1.grid(row = 8, column = 4)
entry_4_2.grid(row = 9, column = 4)
entry_4_3.grid(row = 10, column = 4)
entry_4_4.grid(row = 11, column = 4)

Ökologisch.grid(row = 0, column = 1)


Ökologisch_Ökonomisch = Frame(master)

button_1_1 = Label(Ökologisch_Ökonomisch, text = "Flechtwickelmaschine")
button_1_2 = Label(Ökologisch_Ökonomisch, text = "Multifilamentwickelmaschine90")
button_1_3 = Label(Ökologisch_Ökonomisch, text = "Multifilamentwickelmaschine48")
button_1_4 = Label(Ökologisch_Ökonomisch, text = "Nasswickelmaschine")

label_1_1 = Label (Ökologisch_Ökonomisch, text = "             Energieverbrauch")
label_1_2 = Label (Ökologisch_Ökonomisch, text = "             Materialverbrauch")
label_1_3 = Label (Ökologisch_Ökonomisch, text = "             Kosteneffizient")
label_1_4 = Label (Ökologisch_Ökonomisch, text = "             Kostenaufwand")
label_2_1 = Label (Ökologisch_Ökonomisch, text = "             Energieverbrauch")
label_2_2 = Label (Ökologisch_Ökonomisch, text = "             Materialverbrauch")
label_2_3 = Label (Ökologisch_Ökonomisch, text = "             Kosteneffizient")
label_2_4 = Label (Ökologisch_Ökonomisch, text = "             Kostenaufwand")
label_3_1 = Label (Ökologisch_Ökonomisch, text = "             Energieverbrauch")
label_3_2 = Label (Ökologisch_Ökonomisch, text = "             Materialverbrauch")
label_3_3 = Label (Ökologisch_Ökonomisch, text = "             Kosteneffizient")
label_3_4 = Label (Ökologisch_Ökonomisch, text = "             Kostenaufwand")
label_4_1 = Label (Ökologisch_Ökonomisch, text = "             Energieverbrauch")
label_4_2 = Label (Ökologisch_Ökonomisch, text = "             Materialverbrauch")
label_4_3 = Label (Ökologisch_Ökonomisch, text = "             Kosteneffizient")
label_4_4 = Label (Ökologisch_Ökonomisch, text = "             Kostenaufwand")

entry_1_1 = Entry(Ökologisch_Ökonomisch)
entry_1_2 = Entry(Ökologisch_Ökonomisch)
entry_1_3 = Entry(Ökologisch_Ökonomisch)
entry_1_4 = Entry(Ökologisch_Ökonomisch)
entry_2_1 = Entry(Ökologisch_Ökonomisch)
entry_2_2 = Entry(Ökologisch_Ökonomisch)
entry_2_3 = Entry(Ökologisch_Ökonomisch)
entry_2_4 = Entry(Ökologisch_Ökonomisch)
entry_3_1 = Entry(Ökologisch_Ökonomisch)
entry_3_2 = Entry(Ökologisch_Ökonomisch)
entry_3_3 = Entry(Ökologisch_Ökonomisch)
entry_3_4 = Entry(Ökologisch_Ökonomisch)
entry_4_1 = Entry(Ökologisch_Ökonomisch)
entry_4_2 = Entry(Ökologisch_Ökonomisch)
entry_4_3 = Entry(Ökologisch_Ökonomisch)
entry_4_4 = Entry(Ökologisch_Ökonomisch)

button_1_1.grid(row = 0, column = 1)
button_1_2.grid(row = 0, column = 4)
button_1_3.grid(row = 7, column = 1)
button_1_4.grid(row = 7, column = 4)


label_1_1.grid(row = 1, column = 0)
label_1_2.grid(row = 2, column = 0)
label_1_3.grid(row = 3, column = 0)
label_1_4.grid(row = 4, column = 0)
label_2_1.grid(row = 1, column = 3)
label_2_2.grid(row = 2, column = 3)
label_2_3.grid(row = 3, column = 3)
label_2_4.grid(row = 4, column = 3)
label_3_1.grid(row = 8, column = 0)
label_3_2.grid(row = 9, column = 0)
label_3_3.grid(row = 10, column = 0)
label_3_4.grid(row = 11, column = 0)
label_4_1.grid(row = 8, column = 3)
label_4_2.grid(row = 9, column = 3)
label_4_3.grid(row = 10, column = 3)
label_4_4.grid(row = 11, column = 3)


entry_1_1.grid(row = 1, column = 1)
entry_1_2.grid(row = 2, column = 1)
entry_1_3.grid(row = 3, column = 1)
entry_1_4.grid(row = 4, column = 1)
entry_2_1.grid(row = 1, column = 4)
entry_2_2.grid(row = 2, column = 4)
entry_2_3.grid(row = 3, column = 4)
entry_2_4.grid(row = 4, column = 4)
entry_3_1.grid(row = 8, column = 1)
entry_3_2.grid(row = 9, column = 1)
entry_3_3.grid(row = 10, column = 1)
entry_3_4.grid(row = 11, column = 1)
entry_4_1.grid(row = 8, column = 4)
entry_4_2.grid(row = 9, column = 4)
entry_4_3.grid(row = 10, column = 4)
entry_4_4.grid(row = 11, column = 4)

Ökologisch_Ökonomisch.grid(row = 0, column = 2)


Ökonomisch = Frame(master)

button_1_1 = Label(Ökonomisch, text = "Flechtwickelmaschine")
button_1_2 = Label(Ökonomisch, text = "Multifilamentwickelmaschine90")
button_1_3 = Label(Ökonomisch, text = "Multifilamentwickelmaschine48")
button_1_4 = Label(Ökonomisch, text = "Nasswickelmaschine")

label_1_1 = Label (Ökonomisch, text = "                              Zeitlicher Aufwand")
label_1_2 = Label (Ökonomisch, text = "                                              Flexibilität")
label_1_3 = Label (Ökonomisch, text = "                                   Zeitliche Effizienz")
label_2_1 = Label (Ökonomisch, text = "                              Zeitlicher Aufwand")
label_2_2 = Label (Ökonomisch, text = "                                              Flexibilität")
label_2_3 = Label (Ökonomisch, text = "                                   Zeitliche Effizienz")
label_3_1 = Label (Ökonomisch, text = "                              Zeitlicher Aufwand")
label_3_2 = Label (Ökonomisch, text = "                                              Flexibilität")
label_3_3 = Label (Ökonomisch, text = "                                   Zeitliche Effizienz")
label_4_1 = Label (Ökonomisch, text = "                              Zeitlicher Aufwand")
label_4_2 = Label (Ökonomisch, text = "                                              Flexibilität")
label_4_3 = Label (Ökonomisch, text = "                                   Zeitliche Effizienz")

entry_1_1 = Entry(Ökonomisch)
entry_1_2 = Entry(Ökonomisch)
entry_1_3 = Entry(Ökonomisch)
entry_2_1 = Entry(Ökonomisch)
entry_2_2 = Entry(Ökonomisch)
entry_2_3 = Entry(Ökonomisch)
entry_3_1 = Entry(Ökonomisch)
entry_3_2 = Entry(Ökonomisch)
entry_3_3 = Entry(Ökonomisch)
entry_4_1 = Entry(Ökonomisch)
entry_4_2 = Entry(Ökonomisch)
entry_4_3 = Entry(Ökonomisch)

button_1_1.grid(row = 0, column = 1)
button_1_2.grid(row = 0, column = 4)
button_1_3.grid(row = 7, column = 1)
button_1_4.grid(row = 7, column = 4)

label_1_1.grid(row = 1, column = 0)
label_1_2.grid(row = 2, column = 0)
label_1_3.grid(row = 3, column = 0)
label_2_1.grid(row = 1, column = 3)
label_2_2.grid(row = 2, column = 3)
label_2_3.grid(row = 3, column = 3)
label_3_1.grid(row = 8, column = 0)
label_3_2.grid(row = 9, column = 0)
label_3_3.grid(row = 10, column = 0)
label_4_1.grid(row = 8, column = 3)
label_4_2.grid(row = 9, column = 3)
label_4_3.grid(row = 10, column = 3)


entry_1_1.grid(row = 1, column = 1)
entry_1_2.grid(row = 2, column = 1)
entry_1_3.grid(row = 3, column = 1)
entry_2_1.grid(row = 1, column = 4)
entry_2_2.grid(row = 2, column = 4)
entry_2_3.grid(row = 3, column = 4)
entry_3_1.grid(row = 8, column = 1)
entry_3_2.grid(row = 9, column = 1)
entry_3_3.grid(row = 10, column = 1)
entry_4_1.grid(row = 8, column = 4)
entry_4_2.grid(row = 9, column = 4)
entry_4_3.grid(row = 10, column = 4)


Ökonomisch.grid(row = 1, column = 0)


Sozial_Ökonomisch = Frame(master)

button_1_1 = Label(Sozial_Ökonomisch, text = "Flechtwickelmaschine")
button_1_2 = Label(Sozial_Ökonomisch, text = "Multifilamentwickelmaschine90")
button_1_3 = Label(Sozial_Ökonomisch, text = "Multifilamentwickelmaschine48")
button_1_4 = Label(Sozial_Ökonomisch, text = "Nasswickelmaschine")

label_1_1 = Label (Sozial_Ökonomisch, text = "                                                      Produktqualität")
label_1_2 = Label (Sozial_Ökonomisch, text = "                                                      Produktqualität")
label_1_3 = Label (Sozial_Ökonomisch, text = "                                                      Produktqualität")
label_1_4 = Label (Sozial_Ökonomisch, text = "                                                      Produktqualität")

entry_1_1 = Entry(Sozial_Ökonomisch)
entry_1_2 = Entry(Sozial_Ökonomisch)
entry_1_3 = Entry(Sozial_Ökonomisch)
entry_1_4 = Entry(Sozial_Ökonomisch)

button_1_1.grid(row = 0, column = 1)
button_1_2.grid(row = 0, column = 3)
button_1_3.grid(row = 7, column = 1)
button_1_4.grid(row = 7, column = 3)

label_1_1.grid(row = 1, column = 0)
label_1_2.grid(row = 1, column = 2)
label_1_3.grid(row = 8, column = 0)
label_1_4.grid(row = 8, column = 2)

entry_1_1.grid(row = 1, column = 1)
entry_1_2.grid(row = 1, column = 3)
entry_1_3.grid(row = 8, column = 1)
entry_1_4.grid(row = 8, column = 3)

Sozial_Ökonomisch.grid(row = 1, column = 0)

'''
Sozial_Ökologisch_Ökonomisch = Frame(master)

button_1_1 = Label(Sozial_Ökologisch_Ökonomisch, text = "Flechtwickelmaschine")
button_1_2 = Label(Sozial_Ökologisch_Ökonomisch, text = "Multifilamentwickelmaschine90")
button_1_3 = Label(Sozial_Ökologisch_Ökonomisch, text = "Multifilamentwickelmaschine48")
button_1_4 = Label(Sozial_Ökologisch_Ökonomisch, text = "Nasswickelmaschine")


label_1_1 = Label (Sozial_Ökologisch_Ökonomisch, text = "                      Innovativität")
label_1_2 = Label (Sozial_Ökologisch_Ökonomisch, text = "             Flächenverbrauch")
label_2_1 = Label (Sozial_Ökologisch_Ökonomisch, text = "                      Innovativität")
label_2_2 = Label (Sozial_Ökologisch_Ökonomisch, text = "             Flächenverbrauch")
label_3_1 = Label (Sozial_Ökologisch_Ökonomisch, text = "                      Innovativität")
label_3_2 = Label (Sozial_Ökologisch_Ökonomisch, text = "             Flächenverbrauch")
label_4_1 = Label (Sozial_Ökologisch_Ökonomisch, text = "                      Innovativität")
label_4_2 = Label (Sozial_Ökologisch_Ökonomisch, text = "             Flächenverbrauch")

entry_1_1 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_1_2 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_2_1 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_2_2 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_3_1 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_3_2 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_4_1 = Entry(Sozial_Ökologisch_Ökonomisch)
entry_4_2 = Entry(Sozial_Ökologisch_Ökonomisch)

button_1_1.grid(row = 0, column = 1)
button_1_2.grid(row = 0, column = 6)
button_1_3.grid(row = 6, column = 1)
button_1_4.grid(row = 6, column = 6)


label_1_1.grid(row = 1, column = 0)
label_1_2.grid(row = 2, column = 0)
label_2_1.grid(row = 1, column = 5)
label_2_2.grid(row = 2, column = 5)
label_3_1.grid(row = 7, column = 0)
label_3_2.grid(row = 8, column = 0)
label_4_1.grid(row = 7, column = 5)
label_4_2.grid(row = 8, column = 5)

entry_1_1.grid(row = 1, column = 1)
entry_1_2.grid(row = 2, column = 1)
entry_2_1.grid(row = 1, column = 6)
entry_2_2.grid(row = 2, column = 6)
entry_3_1.grid(row = 7, column = 1)
entry_3_2.grid(row = 8, column = 1)
entry_4_1.grid(row = 7, column = 6)
entry_4_2.grid(row = 8, column = 6)

Sozial_Ökologisch_Ökonomisch.grid(row = 1, column = 2)


master.mainloop()

# Maschine 0


# Maschine 1


# Maschine 2


# Maschine 3


" Ausgabe der Nachhaltigkeitswerte"

# Maschine 0


# Maschine 1


# Maschine 2


# Maschine 3
