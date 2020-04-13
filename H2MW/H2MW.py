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

" TO DO: Deklaration/Initialisierung der Parameter "

# Maschine 1

abfallProzentsatz_M1 = IntVar()
recyclingAbsolut_M1 = IntVar()
recyclingRelativ_M1 = DoubleVar()
verbrauchEnergie_M1 = IntVar()
verbrauchMaterial_M1 = IntVar()
kostenEffizienz_M1 = DoubleVar()
kostenAufwand_M1 = IntVar()
zeitAufwand_M1 = DoubleVar()
flexibilität_M1 = IntVar()
zeitEffizienz_M1 = IntVar()
innovativität_M1 = IntVar()
flächenVerbrauch_M1 = DoubleVar()


abfallProzentsatz_M1.set(64)
recyclingAbsolut_M1.set(1440)
recyclingRelativ_M1.set(51.2)
verbrauchEnergie_M1.set(2524)
verbrauchMaterial_M1.set(1375)
kostenEffizienz_M1.set(0.91)
kostenAufwand_M1.set(40)
zeitAufwand_M1.set(3.5)
flexibilität_M1.set(5)
zeitEffizienz_M1.set(3)
innovativität_M1.set(4)
flächenVerbrauch_M1.set(25.5)


# Maschine 2

abfallProzentsatz_M2 = IntVar()
recyclingAbsolut_M2 = IntVar()
recyclingRelativ_M2 = DoubleVar()
verbrauchEnergie_M2 = IntVar()
verbrauchMaterial_M2 = IntVar()
kostenEffizienz_M2 = DoubleVar()
kostenAufwand_M2 = IntVar()
zeitAufwand_M2 = DoubleVar()
flexibilität_M2 = IntVar()
zeitEffizienz_M2 = IntVar()
innovativität_M2 = IntVar()
flächenVerbrauch_M2 = DoubleVar()


abfallProzentsatz_M2.set(90)
recyclingAbsolut_M2.set(1440)
recyclingRelativ_M2.set(53.5)
verbrauchEnergie_M2.set(3051)
verbrauchMaterial_M2.set(1250)
kostenEffizienz_M2.set(2.56)
kostenAufwand_M2.set(60)
zeitAufwand_M2.set(1)
flexibilität_M2.set(6)
zeitEffizienz_M2.set(7)
innovativität_M2.set(7)
flächenVerbrauch_M2.set(36.5)


# Maschine 3



# Maschine 4



" TO DO: Checks für Gültigkeit der Werte im Verhältnis zu den erlaubten Grenzen "

def norm_wert( wert, min, max):
 if wert <= min:
  return 1
  print("Der Wert ist größer als das erlaubte Maximum!")
 elif wert >= max:
  return 0
  print("Der Wert ist kleiner als das erlaubte Minimum!")
 else:
  return max - wert / max - min

# Maschine 1

abfallProzentsatz_M1_norm = DoubleVar()
recyclingAbsolut_M1_norm = DoubleVar()
recyclingRelativ_M1_norm = DoubleVar()
verbrauchEnergie_M1_norm = DoubleVar()
verbrauchMaterial_M1_norm = DoubleVar()
kostenEffizienz_M1_norm = DoubleVar()
kostenAufwand_M1_norm = DoubleVar()
zeitAufwand_M1_norm = DoubleVar()
flexibilität_M1_norm = DoubleVar()
zeitEffizienz_M1_norm = DoubleVar()
innovativität_M1_norm = DoubleVar()
flächenVerbrauch_M1_norm = DoubleVar()


abfallProzentsatz_M1_norm = norm_wert(abfallProzentsatz_M1.get(), 10, 90)
recyclingAbsolut_M1_norm = norm_wert(recyclingAbsolut_M1.get(), 0, 1440)
recyclingRelativ_M1_norm = norm_wert(recyclingRelativ_M1.get(), 51.2, 53.5)
verbrauchEnergie_M1_norm = norm_wert(verbrauchEnergie_M1.get(), 2524 , 3051)
verbrauchMaterial_M1_norm = norm_wert(verbrauchMaterial_M1.get(), 1250, 1375)
kostenEffizienz_M1_norm = norm_wert(kostenEffizienz_M1.get(), 0.28, 2.56)
kostenAufwand_M1_norm = norm_wert(kostenAufwand_M1.get(), 40, 60)
zeitAufwand_M1_norm = norm_wert(zeitAufwand_M1.get(), 1, 3.5)
flexibilität_M1_norm = norm_wert(flexibilität_M1.get(), 5, 7)
zeitEffizienz_M1_norm = norm_wert(zeitEffizienz_M1.get(), 3, 7)
innovativität_M1_norm = norm_wert(innovativität_M1.get(), 4, 7)
flächenVerbrauch_M1_norm = norm_wert(flächenVerbrauch_M1.get(), 25.5, 55.5)

# Maschine 2



# Maschine 3



# Maschine 4



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


