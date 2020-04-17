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
#Parameter wurden an dieser Stelle deklariert.

abfallProzentsatz_M3 = DoubleVar()
recyclingAbsolut_M3 = IntVar()
recyclingRelativ_M3 = DoubleVar()
verbrauchEnergie_M3 = IntVar()
verbrauchMaterial_M3 = IntVar()
kostenEffizienz_M3 = DoubleVar()
kostenAufwand_M3 = IntVar()
zeitAufwand_M3 = DoubleVar()
flexibilität_M3 = IntVar()
zeitEffizienz_M3 = IntVar()
innovativität_M3 = IntVar()
flächenVerbrauch_M3 = DoubleVar()

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


abfallProzentsatz_M4 = DoubleVar()
recyclingAbsolut_M4 = IntVar()
recyclingRelativ_M4 = DoubleVar()
verbrauchEnergie_M4 = IntVar()
verbrauchMaterial_M4 = IntVar()
kostenEffizienz_M4 = DoubleVar()
kostenAufwand_M4 = IntVar()
zeitAufwand_M4 = DoubleVar()
flexibilität_M4 = IntVar()
zeitEffizienz_M4 = IntVar()
innovativität_M4 = IntVar()
flächenVerbrauch_M4 = DoubleVar()


abfallProzentsatz_M4.set(10)
recyclingAbsolut_M4.set(1440)
recyclingRelativ_M4.set(51.8)
# verbrauchEnergie_M4 = ... noch keine Angaben zu diesem BasisIndikator
verbrauchMaterial_M4.set(1337)
kostenEffizienz_M4.set(0.28)
kostenAufwand_M4.set(40)
zeitAufwand_M4.set(2.5)
flexibilität_M4.set(7)
zeitEffizienz_M4.set(5)
innovativität_M4.set(5)
# flächenVerbrauch_M4 = ... noch keine Angaben zu diesem Basisindikator

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



# Maschine 2



# Maschine 3

 abfallProzentsatz_M3_norm = DoubleVar()
 recyclingAbsolut_M3_norm = DoubleVar()
 recyclingRelativ_M3_norm = DoubleVar()
 verbrauchEnergie_M3_norm = DoubleVar()
 verbrauchMaterial_M3_norm = DoubleVar()
 kostenEffizienz_M3_norm = DoubleVar()
 kostenAufwand_M3_norm = DoubleVar()
 zeitAufwand_M3_norm = DoubleVar()
 flexibilität_M3_norm = DoubleVar()
 zeitEffizienz_M3_norm = DoubleVar()
 innovativität_M3_norm = DoubleVar()
 flächenVerbrauch_M3_norm = DoubleVar()

 abfallProzentsatz_M3_norm = norm_wert(abfallProzentsatz_M3.get(), 10, 90)
 recyclingAbsolut_M3_norm = norm_wert(recyclingAbsolut_M3.get(), 0, 1440)
 recyclingRelativ_M3_norm = norm_wert(recyclingRelativ_M3.get(), 51.2, 53.5)
 verbrauchEnergie_M3_norm = norm_wert(verbrauchEnergie_M3.get(), 2524, 3051)
 verbrauchMaterial_M3_norm = norm_wert(verbrauchMaterial_M3.get(), 1250, 1375)
 kostenEffizienz_M3_norm = norm_wert(kostenEffizienz_M3.get(), 0.28, 2.56)
 kostenAufwand_M3_norm = norm_wert(kostenAufwand_M3.get(), 40, 60)
 zeitAufwand_M3_norm = norm_wert(zeitAufwand_M3.get(), 1, 3.5)
 flexibilität_M3_norm = norm_wert(flexibilität_M3.get(), 0, 8)
 zeitEffizienz_M3_norm = norm_wert(zeitEffizienz_M3.get(), 0, 8)
 innovativität_M3_norm = norm_wert(innovativität_M3.get(), 0, 8)
 flächenVerbrauch_M3_norm = norm_wert(flächenVerbrauch_M3.get(), 25.5, 55.5)

# Maschine 4
 abfallProzentsatz_M4_norm = DoubleVar()
 recyclingAbsolut_M4_norm = DoubleVar()
 recyclingRelativ_M4_norm = DoubleVar()
 verbrauchEnergie_M4_norm = DoubleVar()
 verbrauchMaterial_M4_norm = DoubleVar()
 kostenEffizienz_M4_norm = DoubleVar()
 kostenAufwand_M4_norm = DoubleVar()
 zeitAufwand_M4_norm = DoubleVar()
 flexibilität_M4_norm = DoubleVar()
 zeitEffizienz_M4_norm = DoubleVar()
 innovativität_M4_norm = DoubleVar()
 flächenVerbrauch_M4_norm = DoubleVar()

 abfallProzentsatz_M4_norm = norm_wert(abfallProzentsatz_M4.get(), 10, 90)
 recyclingAbsolut_M4_norm = norm_wert(recyclingAbsolut_M4.get(), 0, 1440)
 recyclingRelativ_M4_norm = norm_wert(recyclingRelativ_M4.get(), 51.2, 53.5)
 verbrauchEnergie_M4_norm = norm_wert(verbrauchEnergie_M4.get(), 2524, 3051)
 verbrauchMaterial_M4_norm = norm_wert(verbrauchMaterial_M4.get(), 1250, 1375)
 kostenEffizienz_M4_norm = norm_wert(kostenEffizienz_M4.get(), 0.28, 2.56)
 kostenAufwand_M4_norm = norm_wert(kostenAufwand_M4.get(), 40, 60)
 zeitAufwand_M4_norm = norm_wert(zeitAufwand_M4.get(), 1, 3.5)
 flexibilität_M4_norm = norm_wert(flexibilität_M4.get(), 0, 8)
 zeitEffizienz_M4_norm = norm_wert(zeitEffizienz_M4.get(), 0, 8)
 innovativität_M4_norm = norm_wert(innovativität_M4.get(), 0, 8)
 flächenVerbrauch_M4_norm = norm_wert(flächenVerbrauch_M4.get(), 25.5, 55.5)


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


