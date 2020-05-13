from tkinter import *
master = Tk()
master.geometry('1200x300')










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