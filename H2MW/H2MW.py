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

abfallProzentsatz = []                          # Deklaration der Werte Listen
for i in range(2):                              #<------ range zu 4 stellen !!!!!!!!!!!!!!!
    abfallProzentsatz.append(IntVar())
recyclingAbsolut = []
for i in range(2):
    recyclingAbsolut.append(IntVar())
recyclingRelativ = []
for i in range(2):
    recyclingRelativ.append(DoubleVar())
verbrauchEnergie = []
for i in range(2):
    verbrauchEnergie.append(IntVar())
verbrauchMaterial = []
for i in range(2):
    verbrauchMaterial.append(IntVar())
kostenEffizienz = []
for i in range(2):
    kostenEffizienz.append(DoubleVar())
kostenAufwand = []
for i in range(2):
    kostenAufwand.append(IntVar())
zeitAufwand = []
for i in range(2):
    zeitAufwand.append(DoubleVar())
flexibilität = []
for i in range(2):
    flexibilität.append(IntVar())
zeitEffizienz = []
for i in range(2):
    zeitEffizienz.append(IntVar())
innovativität = []
for i in range(2):
    innovativität.append(IntVar())
flächenVerbrauch = []
for i in range(2):
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



abfallProzentsatz[1].set(170)
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



# Maschine 3



" TO DO: Checks für Gültigkeit der Werte im Verhältnis zu den erlaubten Grenzen "



def norm_wert(wert, wertList, min, max, mode: bool):            #normierte Wert Funktion
 for x in range(2):                                             #Ausgaben zu den Fällen
  if wertList[x].get() <= min:
      if wertList[x].get() < 0:
        min = 0
      else:
          min = wertList[x].get()
  elif wertList[x].get() >= max:
   max = wertList[x].get()
 if mode == 0:
  return (max - wert) / (max - min)
 else:
  return ((wert - min)/(max - min))

abfallProzentsatz_norm = []
for i in range(2):
    abfallProzentsatz_norm.append(DoubleVar())
recyclingAbsolut_norm = []
for i in range(2):
    recyclingAbsolut_norm.append(DoubleVar())
recyclingRelativ_norm = []                                  #Deklaration der normierten Werte
for i in range(2):
    recyclingRelativ_norm.append(DoubleVar())
verbrauchEnergie_norm = []
for i in range(2):
    verbrauchEnergie_norm.append(DoubleVar())
verbrauchMaterial_norm = []
for i in range(2):
    verbrauchMaterial_norm.append(DoubleVar())
kostenEffizienz_norm = []
for i in range(2):
    kostenEffizienz_norm.append(DoubleVar())
kostenAufwand_norm = []
for i in range(2):
    kostenAufwand_norm.append(DoubleVar())
zeitAufwand_norm = []
for i in range(2):
    zeitAufwand_norm.append(DoubleVar())
flexibilität_norm = []
for i in range(2):
    flexibilität_norm.append(DoubleVar())
zeitEffizienz_norm = []
for i in range(2):
    zeitEffizienz_norm.append(DoubleVar())
innovativität_norm = []
for i in range(2):
    innovativität_norm.append(DoubleVar())
flächenVerbrauch_norm = []
for i in range(2):
    flächenVerbrauch_norm.append(DoubleVar())


print(norm_wert(abfallProzentsatz[0].get(), abfallProzentsatz, 10, 90, 0))              #Ausgabe-Block
print(norm_wert(recyclingAbsolut[0].get(), recyclingAbsolut, 0, 1440, 1))
print(norm_wert(recyclingRelativ[0].get(), recyclingRelativ, 51.2, 53.5, 1))
print(norm_wert(verbrauchEnergie[0].get(), verbrauchEnergie, 2524, 3051, 0))
print(norm_wert(verbrauchMaterial[0].get(), verbrauchMaterial, 1250, 1375, 1))
print(norm_wert(kostenEffizienz[0].get(), kostenEffizienz, 0.28, 2.56, 0))
print(norm_wert(kostenAufwand[0].get(), kostenAufwand, 40, 60, 0))
print(norm_wert(zeitAufwand[0].get(), zeitAufwand, 1, 3.5, 0))
print(norm_wert(flexibilität[0].get(), flexibilität, 0, 8, 1))
print(norm_wert(zeitEffizienz[0].get(), zeitEffizienz, 0, 8, 1))
print(norm_wert(innovativität[0].get(), innovativität, 0, 8, 1))
print(norm_wert(flächenVerbrauch[0].get(), flächenVerbrauch, 25.5, 55.5, 0))


print("---------------------------------------------")

print(norm_wert(abfallProzentsatz[1].get(), abfallProzentsatz, 10, 90, 0))
print(norm_wert(recyclingAbsolut[1].get(), recyclingAbsolut, 0, 1440, 1))
print(norm_wert(recyclingRelativ[1].get(), recyclingRelativ, 51.2, 53.5, 1))
print(norm_wert(verbrauchEnergie[1].get(), verbrauchEnergie, 2524, 3051, 0))
print(norm_wert(verbrauchMaterial[1].get(), verbrauchMaterial, 1250, 1375, 1))
print(norm_wert(kostenEffizienz[1].get(), kostenEffizienz, 0.28, 2.56, 0))
print(norm_wert(kostenAufwand[1].get(), kostenAufwand, 40, 60, 0))
print(norm_wert(zeitAufwand[1].get(), zeitAufwand, 1, 3.5, 0))
print(norm_wert(flexibilität[1].get(), flexibilität, 0, 8, 1))
print(norm_wert(zeitEffizienz[1].get(), zeitEffizienz, 0, 8, 1))
print(norm_wert(innovativität[1].get(), innovativität, 0, 8, 1))
print(norm_wert(flächenVerbrauch[1].get(), flächenVerbrauch, 25.5, 55.5, 0))

# Maschine 0

abfallProzentsatz_norm[0].set(norm_wert(abfallProzentsatz[0].get(), abfallProzentsatz, 10, 90, 0)) #Initialisierung der norm Werte
recyclingAbsolut_norm[0].set(norm_wert(recyclingAbsolut[0].get(), recyclingAbsolut, 0, 1440, 1))

# Maschine 1



# Maschine 2



# Maschine 3



" TO DO: Ausrechnung der Nachhaltigkeitswerte "

# Maschine 0



# Maschine 1



# Maschine 2



# Maschine 3



" Ausgabe der Nachhaltigkeitswerte"

# Maschine 0



# Maschine 1



# Maschine 2



# Maschine 3



"""