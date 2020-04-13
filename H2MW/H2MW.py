"""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           How 2 MultiWind - Wickelmaschinendemonstrator Anwendung
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 Index:
 Maschine 1 - Flechtmaschine
 Maschine 2 - Multifilamentwickelmaschine 90
 Maschine 3 - Mulftifilamentwickelmaschine 48
 Maschine 4 - Nasswickelmaschine

"""
# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
master = Tk()

" TO DO: Deklaration der Parameter "

# Maschine 1

abfallProzentsatz = DoubleVar()
recyclingAbsolut = IntVar()
recyclingRelativ = DoubleVar()
verbrauchEnergie = IntVar()
verbrauchMaterial = IntVar()
kostenEffizienz = DoubleVar()
kostenAufwand = IntVar()
zeitAufwand = DoubleVar()
flexibilität = IntVar()
zeitEffizienz = IntVar()
innovativität = IntVar()
flächenVerbrauch = DoubleVar()

# Maschine 2



# Maschine 3


abfallProzentsatz = DoubleVar()
recyclingAbsolut = IntVar()
recyclingRelativ = DoubleVar()
verbrauchEnergie = IntVar()
verbrauchMaterial = IntVar()
kostenEffizienz = DoubleVar()
kostenAufwand = IntVar()
zeitAufwand = DoubleVar()
flexibilität = IntVar()
zeitEffizienz = IntVar()
innovativität = IntVar()
flächenVerbrauch = DoubleVar()

abfallProzentsatz_M3.set(48)
recyclingAbsolut_M3.set(1440)
recyclingRelativ_M3.set(52.3)
verbrauchEnergie_M3.set(3051)
verbrauchMaterial_M3.set(1312)
kostenEffizienz_M3.set(1.37)
kostenAufwand_M3.set(60)
zeitAufwand_M3.set(1.5)
flexibilität_M3.set(5)
zeitEffizienz_M3.set(6)
innovativität_M3.set(6)
flächenVerbrauch_M3.set(36.5)

# Maschine 4


abfallProzentsatz = DoubleVar()
recyclingAbsolut = IntVar()
recyclingRelativ = DoubleVar()
verbrauchEnergie = IntVar()
verbrauchMaterial = IntVar()
kostenEffizienz = DoubleVar()
kostenAufwand = IntVar()
zeitAufwand = DoubleVar()
flexibilität = IntVar()
zeitEffizienz = IntVar()
innovativität = IntVar()
flächenVerbrauch = DoubleVar()


abfallProzentsatz_M4.set(10)
recyclingAbsolut_M4.set(1440)
recyclingRelativ_M4.set(51.8)
verbrauchEnergie_M4 = ...
verbrauchMaterial_M4.set(1337)
kostenEffizienz_M4.set(0.28)
kostenAufwand_M4.set(40)
zeitAufwand_M4.set(2.5)
flexibilität_M4.set(7)
zeitEffizienz_M4.set(5)
innovativität_M4.set(5)
flächenVerbrauch_M4 = ...

" TO DO: Checks für Gültigkeit der Werte im Verhältnis zu den erlaubten Grenzen "

# Maschine 1



# Maschine 2



# Maschine 3
def abfallProzentsatz():
 min = IntVar()
 max = IntVar()
 nom_Wert3_M3 = IntVar()
 min.set(10)
 max.set(90)
  if abfallProzentsatz_M3 >= min and abfallProzentsatz_M3 <= max:
 nom_Wert3_M3 = (max.set(90)-abfallProzentsatz_M3)/(max.set(90)-min.set(10))
 elif abfallProzentsatz_M3 <= min.set(10):
 nom_Wert3_M3 = 0
if recyclingAbsolut_M3 >= 0 and recyclingAbsolut_M3 <= 1440:
  nom_Wert5_M3 = (recyclingAbsolut_M3-0)/(1440-0)

if recyclingRelativ_M3 >= 51.2 and recyclingRelativ_M3 <= 53.5:


if verbrauchEnergie_M3 >= 2524 and verbrauchEnergie_M3 <= 3051:


if verbrauchMaterial_M3 >= 1250 and verbrauchMaterial_M3 <= 1375:


if kostenEffizienz_M3 >= 0.28 and kostenEffizienz_M3 <= 2.56:


if kostenAufwand_M3 >= 1 and kostenAufwand_M3 <= 3.5:


if flexibilität_M3 >= 0 and flexibilität_M3 <= 8:


if zeitEffizienz_M3 >= 0 and zeitEffizienz_M3 <= 8:


if innovativität_M3 >= 0 and innovativität_M3 <= 8:


if flächenVerbrauch_M3 >= 25.5 and flächenVerbrauch_M3 <= 55.5:




# Maschine 4

if abfallProzentsatz_M4 >= 10 and abfallProzentsatz_M4 <= 90:


if recyclingAbsolut_M4 >= 0 and recyclingAbsolut_M4 <= 1440:


if recyclingRelativ_M4 >= 51.2 and recyclingRelativ_M4 <= 53.5:


if verbrauchEnergie_M4 >= 2524 and verbrauchEnergie_M4 <= 3051:

if verbrauchMaterial_M4 >= 1250 and verbrauchMaterial_M4 <= 1375:


if kostenEffizienz_M4 >= 0.28 and kostenEffizienz_M3 <= 2.56:


if kostenAufwand_M4 >= 1 and kostenAufwand_M4 <= 3.5:


if flexibilität_M4 >= 0 and flexibilität_M4 <= 8:


if zeitEffizienz_M4 >= 0 and zeitEffizienz_M4 <= 8:

if innovativität_M4 >= 0 and innovativität_M4 <= 8:


if flächenVerbrauch_M4 >= 25.5 and flächenVerbrauch_M4 <= 55.5:


 " TO DO: Ausrechnung der Nachhaltigkeitswerte "

# Maschine 1



# Maschine 2



# Maschine 3



# Maschine 4



" Ausgabe der Nachhaltigkeitswerte"

# Maschine 1



# Maschine 2



# Maschine 3



# Maschine 4


