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
from tkinter import font



class H2MW(Tk):



    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageEnd):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()


        self.show_frame(StartPage, "Maschinen Auswahl")

    def show_frame(self, cont, name):
        for fme in self.frames:  # Remove all frames
            self.frames[fme].grid_remove()
        self.get_page(StartPage).werte_update()
        frame = self.frames[cont]
        frame.grid()
        self.title(name)

    def get_page(self, page_name):
        return self.frames[page_name]

    def resetter(self):
        self.get_page(StartPage).werte_reset()
        self.show_frame(StartPage, "Maschinen Auswahl")


def columnconfig(*argv):
    for arg in argv:
        arg.columnconfigure(0, minsize=280)
        arg.columnconfigure(1, minsize=280)


def enable(childList):
    for child in childList:
        child.configure(state='normal')


def disable(childList):
    for child in childList:
        child.configure(state='disabled')


class StartPage(Frame):

    def boot(self):
        self.emissionen = []
        for i in range(4):
            self.emissionen.append(IntVar())
        self.giftMaterial = []
        for i in range(4):
            self.giftMaterial.append(IntVar())
        self.abfallProzentsatz = []  # Deklaration der Werte Listen
        for i in range(4):
            self.abfallProzentsatz.append(IntVar())
        self.abfallSzenarien = []
        for i in range(4):
            self.abfallSzenarien.append(IntVar())
        self.recyclingAbsolut = []
        for i in range(4):
            self.recyclingAbsolut.append(IntVar())
        self.recyclingRelativ = []
        for i in range(4):
            self.recyclingRelativ.append(DoubleVar())
        self.verbrauchEnergie = []
        for i in range(4):
            self.verbrauchEnergie.append(IntVar())
        self.verbrauchMaterial = []
        for i in range(4):
            self.verbrauchMaterial.append(IntVar())
        self.kostenEffizienz = []
        for i in range(4):
            self.kostenEffizienz.append(DoubleVar())
        self.kostenAufwand = []
        for i in range(4):
            self.kostenAufwand.append(IntVar())
        self.zeitAufwand = []
        for i in range(4):
            self.zeitAufwand.append(DoubleVar())
        self.flexibilität = []
        for i in range(4):
            self.flexibilität.append(IntVar())
        self.zeitEffizienz = []
        for i in range(4):
            self.zeitEffizienz.append(IntVar())
        self.produktQualität = []
        for i in range(4):
            self.produktQualität.append(IntVar())
        self.innovativität = []
        for i in range(4):
            self.innovativität.append(IntVar())
        self.flächenVerbrauch = []
        for i in range(4):
            self.flächenVerbrauch.append(DoubleVar())

        self.werte_reset()

        " TO DO: Checks für Gültigkeit der Werte im Verhältnis zu den erlaubten Grenzen"

        def norm_wert(wert, wertList, min, max, mode: bool):  # normierte Wert Funktion
            """
            if wert < min:
                print("Der von Ihnen gewählte Wert ist kleiner als das Minimum")
            elif wert > max:
                print("Der von Ihnen gewählte Wert ist größer als das Maximum")
            """
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

        self.emissionen_norm = []
        for i in range(4):
            self.emissionen_norm.append(DoubleVar())
        self.giftMaterial_norm = []
        for i in range(4):
            self.giftMaterial_norm.append(DoubleVar())
        self.abfallProzentsatz_norm = []
        for i in range(4):
            self.abfallProzentsatz_norm.append(DoubleVar())
        self.abfallSzenarien_norm = []
        for i in range(4):
            self.abfallSzenarien_norm.append(DoubleVar())
        self.recyclingAbsolut_norm = []
        for i in range(4):
            self.recyclingAbsolut_norm.append(DoubleVar())
        self.recyclingRelativ_norm = []  # Deklaration der normierten Werte
        for i in range(4):
            self.recyclingRelativ_norm.append(DoubleVar())
        self.verbrauchEnergie_norm = []
        for i in range(4):
            self.verbrauchEnergie_norm.append(DoubleVar())
        self.verbrauchMaterial_norm = []
        for i in range(4):
            self.verbrauchMaterial_norm.append(DoubleVar())
        self.kostenEffizienz_norm = []
        for i in range(4):
            self.kostenEffizienz_norm.append(DoubleVar())
        self.kostenAufwand_norm = []
        for i in range(4):
            self.kostenAufwand_norm.append(DoubleVar())
        self.zeitAufwand_norm = []
        for i in range(4):
            self.zeitAufwand_norm.append(DoubleVar())
        self.flexibilität_norm = []
        for i in range(4):
            self.flexibilität_norm.append(DoubleVar())
        self.zeitEffizienz_norm = []
        for i in range(4):
            self.zeitEffizienz_norm.append(DoubleVar())
        self.produktQualität_norm = []
        for i in range(4):
            self.produktQualität_norm.append(DoubleVar())
        self.innovativität_norm = []
        for i in range(4):
            self.innovativität_norm.append(DoubleVar())
        self.flächenVerbrauch_norm = []
        for i in range(4):
            self.flächenVerbrauch_norm.append(DoubleVar())

        # Maschine 0-3

        " TO DO: Ausrechnung der Nachhaltigkeitswerte "

        for i in range(4):
            self.emissionen_norm[i].set(norm_wert(self.emissionen[i].get(), self.emissionen, 0, 100, 1))
            self.giftMaterial_norm[i].set(norm_wert(self.giftMaterial[i].get(), self.giftMaterial, 0, 100, 1))
            self.abfallProzentsatz_norm[i].set(
                norm_wert(self.abfallProzentsatz[i].get(), self.abfallProzentsatz, 10, 90, 0))
            self.abfallSzenarien_norm[i].set(norm_wert(self.abfallSzenarien[i].get(), self.abfallSzenarien, 0, 8, 0))
            self.recyclingAbsolut_norm[i].set(
                norm_wert(self.recyclingAbsolut[i].get(), self.recyclingAbsolut, 0, 1440, 1))
            self.recyclingRelativ_norm[i].set(
                norm_wert(self.recyclingRelativ[i].get(), self.recyclingRelativ, 51.2, 53.5, 1))
            self.verbrauchEnergie_norm[i].set(
                norm_wert(self.verbrauchEnergie[i].get(), self.verbrauchEnergie, 2524, 3051, 0))
            self.verbrauchMaterial_norm[i].set(
                norm_wert(self.verbrauchMaterial[i].get(), self.verbrauchMaterial, 1250, 1375, 1))
            self.kostenEffizienz_norm[i].set(
                norm_wert(self.kostenEffizienz[i].get(), self.kostenEffizienz, 0.28, 2.56, 0))
            self.kostenAufwand_norm[i].set(norm_wert(self.kostenAufwand[i].get(), self.kostenAufwand, 40, 60, 0))
            self.zeitAufwand_norm[i].set(norm_wert(self.zeitAufwand[i].get(), self.zeitAufwand, 1, 3.5, 0))
            self.flexibilität_norm[i].set(norm_wert(self.flexibilität[i].get(), self.flexibilität, 0, 8, 1))
            self.zeitEffizienz_norm[i].set(norm_wert(self.zeitEffizienz[i].get(), self.zeitEffizienz, 0, 8, 1))
            self.produktQualität_norm[i].set(norm_wert(self.produktQualität[i].get(), self.produktQualität, 0, 100, 0))
            self.innovativität_norm[i].set(norm_wert(self.innovativität[i].get(), self.innovativität, 0, 8, 1))
            self.flächenVerbrauch_norm[i].set(
                norm_wert(self.flächenVerbrauch[i].get(), self.flächenVerbrauch, 25.5, 55.5, 0))

        self.emissionen_zg = []
        for i in range(4):
            self.emissionen_zg.append(DoubleVar())
        self.giftMaterial_zg = []
        for i in range(4):
            self.giftMaterial_zg.append(DoubleVar())
        self.abfallProzentsatz_zg = []  # Deklaration der ZG Werte
        for i in range(4):
            self.abfallProzentsatz_zg.append(DoubleVar())
        self.abfallSzenarien_zg = []
        for i in range(4):
            self.abfallSzenarien_zg.append(DoubleVar())
        self.recyclingAbsolut_zg = []
        for i in range(4):
            self.recyclingAbsolut_zg.append(DoubleVar())
        self.recyclingRelativ_zg = []
        for i in range(4):
            self.recyclingRelativ_zg.append(DoubleVar())
        self.verbrauchEnergie_zg = []
        for i in range(4):
            self.verbrauchEnergie_zg.append(DoubleVar())
        self.verbrauchMaterial_zg = []
        for i in range(4):
            self.verbrauchMaterial_zg.append(DoubleVar())
        self.kostenEffizienz_zg = []
        for i in range(4):
            self.kostenEffizienz_zg.append(DoubleVar())
        self.kostenAufwand_zg = []
        for i in range(4):
            self.kostenAufwand_zg.append(DoubleVar())
        self.zeitAufwand_zg = []
        for i in range(4):
            self.zeitAufwand_zg.append(DoubleVar())
        self.flexibilität_zg = []
        for i in range(4):
            self.flexibilität_zg.append(DoubleVar())
        self.zeitEffizienz_zg = []
        for i in range(4):
            self.zeitEffizienz_zg.append(DoubleVar())
        self.produktQualität_zg = []
        for i in range(4):
            self.produktQualität_zg.append(DoubleVar())
        self.innovativität_zg = []
        for i in range(4):
            self.innovativität_zg.append(DoubleVar())
        self.flächenVerbrauch_zg = []
        for i in range(4):
            self.flächenVerbrauch_zg.append(DoubleVar())

        for i in range(4):
            self.emissionen_zg[i].set((self.emissionen_norm[i].get() % 0.5) * 2)
            self.giftMaterial_zg[i].set((self.giftMaterial_norm[i].get() % 0.5) * 2)
            self.abfallProzentsatz_zg[i].set((self.abfallProzentsatz_norm[i].get() % 0.5) * 2)
            self.abfallSzenarien_zg[i].set((self.abfallSzenarien_norm[i].get() % 0.5) * 2)
            self.recyclingAbsolut_zg[i].set((self.recyclingAbsolut_norm[i].get() % 0.5) * 2)
            self.recyclingRelativ_zg[i].set((self.recyclingRelativ_norm[i].get() % 0.5) * 2)
            self.verbrauchEnergie_zg[i].set((self.verbrauchEnergie_norm[i].get() % 0.5) * 2)
            self.verbrauchMaterial_zg[i].set((self.verbrauchMaterial_norm[i].get() % 0.5) * 2)
            self.kostenEffizienz_zg[i].set((self.kostenEffizienz_norm[i].get() % 0.5) * 2)
            self.kostenAufwand_zg[i].set((self.kostenAufwand_norm[i].get() % 0.5) * 2)
            self.zeitAufwand_zg[i].set((self.zeitAufwand_norm[i].get() % 0.5) * 2)
            self.flexibilität_zg[i].set((self.flexibilität_norm[i].get() % 0.5) * 2)
            self.zeitEffizienz_zg[i].set((self.zeitEffizienz_norm[i].get() % 0.5) * 2)
            self.produktQualität_zg[i].set((self.produktQualität_norm[i].get() % 0.5) * 2)
            self.innovativität_zg[i].set((self.innovativität_norm[i].get() % 0.5) * 2)
            self.flächenVerbrauch_zg[i].set((self.flächenVerbrauch_norm[i].get() % 0.5) * 2)

        self.sozial_oekologisch = []
        for i in range(4):
            self.sozial_oekologisch.append(DoubleVar())
        self.oekologisch = []
        for i in range(4):
            self.oekologisch.append(DoubleVar())
        self.oekologisch_oekonomisch = []
        for i in range(4):
            self.oekologisch_oekonomisch.append(DoubleVar())
        self.oekonomisch = []
        for i in range(4):
            self.oekonomisch.append(DoubleVar())
        self.sozial_oekonomisch = []
        for i in range(4):
            self.sozial_oekonomisch.append(DoubleVar())
        self.sozial_oekologisch_oekonomisch = []
        for i in range(4):
            self.sozial_oekologisch_oekonomisch.append(DoubleVar())
        self.gsi_wert = []
        for i in range(4):
            self.gsi_wert.append(DoubleVar())

        def dimension_rechnen(*argv):
            var = 1
            for arg in argv:
                var = var * (arg * arg + (1 - arg) * (1 - arg))
            return var

        for i in range(4):
            self.sozial_oekologisch[i].set(dimension_rechnen(self.emissionen_zg[i].get(), self.giftMaterial_zg[i].get()))
            self.oekologisch[i].set(
                dimension_rechnen(self.abfallProzentsatz_zg[i].get(), self.abfallSzenarien_zg[i].get(),
                                  self.recyclingAbsolut_zg[i].get(),
                                  self.recyclingRelativ_zg[i].get()))
            self.oekologisch_oekonomisch[i].set(
                dimension_rechnen(self.verbrauchEnergie_zg[i].get(), self.verbrauchMaterial_zg[i].get(),
                                  self.kostenEffizienz_zg[i].get(),
                                  self.kostenAufwand_zg[i].get()))
            self.oekonomisch[i].set(
                dimension_rechnen(self.zeitAufwand_zg[i].get(), self.flexibilität_zg[i].get(),
                                  self.zeitEffizienz_zg[i].get()))
            self.sozial_oekonomisch[i].set(dimension_rechnen(self.produktQualität_zg[i].get()))
            self.sozial_oekologisch_oekonomisch[i].set(
                dimension_rechnen(self.innovativität_zg[i].get(), self.flächenVerbrauch_zg[i].get()))
            self.gsi_wert[i].set(dimension_rechnen(self.sozial_oekologisch[i].get(), self.oekologisch[i].get(),  self.oekologisch_oekonomisch[i].get(), self.oekonomisch[i].get(),
                                                   self.sozial_oekonomisch[i].get(), self.sozial_oekologisch_oekonomisch[i].get()))


    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        first = Frame(self)
        buttons_first = Frame(first)

        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()
        self.var4 = BooleanVar()

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)

        button_1 = Button(buttons_first, text="Run with Default", command=lambda: self.default())
        button_2 = Button(buttons_first, text="Next", command=lambda: controller.show_frame(PageOne, "Sozial-Ökologische Indikatoren"))

        label_1 = Label(first, text="Flechtmaschine")
        label_2 = Label(first, text="Multifilamentwickelmaschine90")
        label_3 = Label(first, text="Multifilamentwickelmaschine48")
        label_4 = Label(first, text="Nasswickelmaschine")

        check_1 = Checkbutton(first, variable=self.var1, onvalue=1, offvalue=0)
        check_2 = Checkbutton(first, variable=self.var2, onvalue=1, offvalue=0)
        check_3 = Checkbutton(first, variable=self.var3, onvalue=1, offvalue=0)
        check_4 = Checkbutton(first, variable=self.var4, onvalue=1, offvalue=0)

        label_1.grid(row=0, column=0)
        label_2.grid(row=0, column=2)
        label_3.grid(row=1, column=0)
        label_4.grid(row=1, column=2)

        check_1.grid(row=0, column=1)
        check_2.grid(row=0, column=3)
        check_3.grid(row=1, column=1)
        check_4.grid(row=1, column=3)

        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)


        buttons_first.grid(row=2, column=2)

        first.grid(row=0, column=0)

        self.boot()

    def default(self):
        self.werte_reset()
        self.werte_update()
        self.controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick")
    """
    def ausgabe(self):
    
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


        for i in range(4):
            self.emissionen_norm[i].set(norm_wert(self.emissionen[i].get(), self.emissionen, 0, 100, 1))
            self.giftMaterial_norm[i].set(norm_wert(self.giftMaterial[i].get(), self.giftMaterial, 0, 100, 1))
            self.abfallProzentsatz_norm[i].set(
                norm_wert(self.abfallProzentsatz[i].get(), self.abfallProzentsatz, 10, 90, 0))
            self.abfallSzenarien_norm[i].set(norm_wert(self.abfallSzenarien[i].get(), self.abfallSzenarien, 0, 8, 0))
            self.recyclingAbsolut_norm[i].set(
                norm_wert(self.recyclingAbsolut[i].get(), self.recyclingAbsolut, 0, 1440, 1))
            self.recyclingRelativ_norm[i].set(
                norm_wert(self.recyclingRelativ[i].get(), self.recyclingRelativ, 51.2, 53.5, 1))
            self.verbrauchEnergie_norm[i].set(
                norm_wert(self.verbrauchEnergie[i].get(), self.verbrauchEnergie, 2524, 3051, 0))
            self.verbrauchMaterial_norm[i].set(
                norm_wert(self.verbrauchMaterial[i].get(), self.verbrauchMaterial, 1250, 1375, 1))
            self.kostenEffizienz_norm[i].set(
                norm_wert(self.kostenEffizienz[i].get(), self.kostenEffizienz, 0.28, 2.56, 0))
            self.kostenAufwand_norm[i].set(norm_wert(self.kostenAufwand[i].get(), self.kostenAufwand, 40, 60, 0))
            self.zeitAufwand_norm[i].set(norm_wert(self.zeitAufwand[i].get(), self.zeitAufwand, 1, 3.5, 0))
            self.flexibilität_norm[i].set(norm_wert(self.flexibilität[i].get(), self.flexibilität, 0, 8, 1))
            self.zeitEffizienz_norm[i].set(norm_wert(self.zeitEffizienz[i].get(), self.zeitEffizienz, 0, 8, 1))
            self.produktQualität_norm[i].set(norm_wert(self.produktQualität[i].get(), self.produktQualität, 0, 100, 0))
            self.innovativität_norm[i].set(norm_wert(self.innovativität[i].get(), self.innovativität, 0, 8, 1))
            self.flächenVerbrauch_norm[i].set(
                norm_wert(self.flächenVerbrauch[i].get(), self.flächenVerbrauch, 25.5, 55.5, 0))


        for i in range(4):
            self.emissionen_zg[i].set((self.emissionen_norm[i].get() % 0.5) * 2)
            self.giftMaterial_zg[i].set((self.giftMaterial_norm[i].get() % 0.5) * 2)
            self.abfallProzentsatz_zg[i].set((self.abfallProzentsatz_norm[i].get() % 0.5) * 2)
            self.abfallSzenarien_zg[i].set((self.abfallSzenarien_norm[i].get() % 0.5) * 2)
            self.recyclingAbsolut_zg[i].set((self.recyclingAbsolut_norm[i].get() % 0.5) * 2)
            self.recyclingRelativ_zg[i].set((self.recyclingRelativ_norm[i].get() % 0.5) * 2)
            self.verbrauchEnergie_zg[i].set((self.verbrauchEnergie_norm[i].get() % 0.5) * 2)
            self.verbrauchMaterial_zg[i].set((self.verbrauchMaterial_norm[i].get() % 0.5) * 2)
            self.kostenEffizienz_zg[i].set((self.kostenEffizienz_norm[i].get() % 0.5) * 2)
            self.kostenAufwand_zg[i].set((self.kostenAufwand_norm[i].get() % 0.5) * 2)
            self.zeitAufwand_zg[i].set((self.zeitAufwand_norm[i].get() % 0.5) * 2)
            self.flexibilität_zg[i].set((self.flexibilität_norm[i].get() % 0.5) * 2)
            self.zeitEffizienz_zg[i].set((self.zeitEffizienz_norm[i].get() % 0.5) * 2)
            self.produktQualität_zg[i].set((self.produktQualität_norm[i].get() % 0.5) * 2)
            self.innovativität_zg[i].set((self.innovativität_norm[i].get() % 0.5) * 2)
            self.flächenVerbrauch_zg[i].set((self.flächenVerbrauch_norm[i].get() % 0.5) * 2)


        def dimension_rechnen(*argv):
            var = 1
            for arg in argv:
                var = var * (arg * arg + (1 - arg) * (1 - arg))
            return var


        for i in range(4):
            self.sozial_oekologisch[i].set(
                dimension_rechnen(self.emissionen_zg[i].get(), self.giftMaterial_zg[i].get()))
            self.oekologisch[i].set(
                dimension_rechnen(self.abfallProzentsatz_zg[i].get(), self.abfallSzenarien_zg[i].get(),
                                  self.recyclingAbsolut_zg[i].get(),
                                  self.recyclingRelativ_zg[i].get()))
            self.oekologisch_oekonomisch[i].set(
                dimension_rechnen(self.verbrauchEnergie_zg[i].get(), self.verbrauchMaterial_zg[i].get(),
                                  self.kostenEffizienz_zg[i].get(),
                                  self.kostenAufwand_zg[i].get()))
            self.oekonomisch[i].set(
                dimension_rechnen(self.zeitAufwand_zg[i].get(), self.flexibilität_zg[i].get(),
                                  self.zeitEffizienz_zg[i].get()))
            self.sozial_oekonomisch[i].set(dimension_rechnen(self.produktQualität_zg[i].get()))
            self.sozial_oekologisch_oekonomisch[i].set(
                dimension_rechnen(self.innovativität_zg[i].get(), self.flächenVerbrauch_zg[i].get()))
            self.gsi_wert[i].set((self.sozial_oekologisch[i].get() + self.oekologisch_oekonomisch[i].get() + self.oekonomisch[i].get() +
                                  self.sozial_oekonomisch[i].get() + self.sozial_oekologisch_oekonomisch[i].get() + self.sozial_oekologisch_oekonomisch[i].get()) / 6)


        for i in range(4):
            print("----------------------------------------------------------------")
            print("sozial - oekologisch: ", self.sozial_oekologisch[i].get())
            print("oekologisch: ", self.oekologisch[i].get())
            print("oekologisch_oekonomisch :", self.oekologisch_oekonomisch[i].get())
            print("oekonomisch :", self.oekonomisch[i].get())
            print("sozial - oekonomisch :", self.sozial_oekonomisch[i].get())
            print("sozial_oekologisch_oekonomisch :", self.sozial_oekologisch_oekonomisch[i].get())

        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        
        """
    """
    """
    def werte_update(self):

        self.emissionen[0].set(self.controller.get_page(PageOne).entry_1_1.get())
        self.giftMaterial[0].set(self.controller.get_page(PageOne).entry_1_2.get())
        self.emissionen[1].set(self.controller.get_page(PageOne).entry_1.get())
        self.giftMaterial[1].set(self.controller.get_page(PageOne).entry_2.get())
        self.emissionen[2].set(self.controller.get_page(PageOne).entry_3_1.get())
        self.giftMaterial[2].set(self.controller.get_page(PageOne).entry_3_1.get())
        self.emissionen[3].set(self.controller.get_page(PageOne).entry_4_1.get())
        self.giftMaterial[3].set(self.controller.get_page(PageOne).entry_4_1.get())

        self.abfallProzentsatz[0].set(self.controller.get_page(PageTwo).entry_1_1.get())
        self.abfallSzenarien[0].set(self.controller.get_page(PageTwo).entry_1_2.get())
        self.recyclingAbsolut[0].set(self.controller.get_page(PageTwo).entry_1_3.get())
        self.recyclingRelativ[0].set(self.controller.get_page(PageTwo).entry_1_4.get())
        self.abfallProzentsatz[1].set(self.controller.get_page(PageTwo).entry_2_1.get())
        self.abfallSzenarien[1].set(self.controller.get_page(PageTwo).entry_2_2.get())
        self.recyclingAbsolut[1].set(self.controller.get_page(PageTwo).entry_2_3.get())
        self.recyclingRelativ[1].set(self.controller.get_page(PageTwo).entry_2_4.get())
        self.abfallProzentsatz[2].set(self.controller.get_page(PageTwo).entry_3_1.get())
        self.abfallSzenarien[2].set(self.controller.get_page(PageTwo).entry_3_2.get())
        self.recyclingAbsolut[2].set(self.controller.get_page(PageTwo).entry_3_3.get())
        self.recyclingRelativ[2].set(self.controller.get_page(PageTwo).entry_3_4.get())
        self.abfallProzentsatz[3].set(self.controller.get_page(PageTwo).entry_4_1.get())
        self.abfallSzenarien[3].set(self.controller.get_page(PageTwo).entry_4_2.get())
        self.recyclingAbsolut[3].set(self.controller.get_page(PageTwo).entry_4_3.get())
        self.recyclingRelativ[3].set(self.controller.get_page(PageTwo).entry_4_4.get())

        self.verbrauchEnergie[0].set(self.controller.get_page(PageThree).entry_1_1.get())
        self.verbrauchMaterial[0].set(self.controller.get_page(PageThree).entry_1_2.get())
        self.kostenEffizienz[0].set(self.controller.get_page(PageThree).entry_1_3.get())
        self.kostenAufwand[0].set(self.controller.get_page(PageThree).entry_1_4.get())
        self.verbrauchEnergie[1].set(self.controller.get_page(PageThree).entry_2_1.get())
        self.verbrauchMaterial[1].set(self.controller.get_page(PageThree).entry_2_2.get())
        self.kostenEffizienz[1].set(self.controller.get_page(PageThree).entry_2_3.get())
        self.kostenAufwand[1].set(self.controller.get_page(PageThree).entry_2_4.get())
        self.verbrauchEnergie[2].set(self.controller.get_page(PageThree).entry_3_1.get())
        self.verbrauchMaterial[2].set(self.controller.get_page(PageThree).entry_3_2.get())
        self.kostenEffizienz[2].set(self.controller.get_page(PageThree).entry_3_3.get())
        self.kostenAufwand[2].set(self.controller.get_page(PageThree).entry_3_4.get())
        self.verbrauchEnergie[3].set(self.controller.get_page(PageThree).entry_4_1.get())
        self.verbrauchMaterial[3].set(self.controller.get_page(PageThree).entry_4_2.get())
        self.kostenEffizienz[3].set(self.controller.get_page(PageThree).entry_4_3.get())
        self.kostenAufwand[3].set(self.controller.get_page(PageThree).entry_4_4.get())

        self.zeitAufwand[0].set(self.controller.get_page(PageFour).entry_1_1.get())
        self.flexibilität[0].set(self.controller.get_page(PageFour).entry_1_2.get())
        self.zeitEffizienz[0].set(self.controller.get_page(PageFour).entry_1_3.get())
        self.zeitAufwand[1].set(self.controller.get_page(PageFour).entry_2_1.get())
        self.flexibilität[1].set(self.controller.get_page(PageFour).entry_2_2.get())
        self.zeitEffizienz[1].set(self.controller.get_page(PageFour).entry_2_3.get())
        self.zeitAufwand[2].set(self.controller.get_page(PageFour).entry_3_1.get())
        self.flexibilität[2].set(self.controller.get_page(PageFour).entry_3_2.get())
        self.zeitEffizienz[2].set(self.controller.get_page(PageFour).entry_3_3.get())
        self.zeitAufwand[3].set(self.controller.get_page(PageFour).entry_4_1.get())
        self.flexibilität[3].set(self.controller.get_page(PageFour).entry_4_2.get())
        self.zeitEffizienz[3].set(self.controller.get_page(PageFour).entry_4_3.get())

        self.produktQualität[0].set(self.controller.get_page(PageFive).entry_1_1.get())
        self.produktQualität[1].set(self.controller.get_page(PageFive).entry_1_2.get())
        self.produktQualität[2].set(self.controller.get_page(PageFive).entry_1_3.get())
        self.produktQualität[3].set(self.controller.get_page(PageFive).entry_1_4.get())

        self.innovativität[0].set(self.controller.get_page(PageSix).entry_1_1.get())
        self.flächenVerbrauch[0].set(self.controller.get_page(PageSix).entry_1_2.get())
        self.innovativität[1].set(self.controller.get_page(PageSix).entry_2_1.get())
        self.flächenVerbrauch[1].set(self.controller.get_page(PageSix).entry_2_2.get())
        self.innovativität[2].set(self.controller.get_page(PageSix).entry_3_1.get())
        self.flächenVerbrauch[2].set(self.controller.get_page(PageSix).entry_3_1.get())
        self.innovativität[3].set(self.controller.get_page(PageSix).entry_4_1.get())
        self.flächenVerbrauch[3].set(self.controller.get_page(PageSix).entry_4_1.get())


        def norm_wert(wert, wertList, min, max, mode: bool):  # normierte Wert Funktion
            """
            if wert < min:
                print("Der von Ihnen gewählte Wert ist kleiner als das Minimum")
            elif wert > max:
                print("Der von Ihnen gewählte Wert ist größer als das Maximum")
            """
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


        for i in range(4):
            self.emissionen_norm[i].set(norm_wert(self.emissionen[i].get(), self.emissionen, 0, 100, 1))
            self.giftMaterial_norm[i].set(norm_wert(self.giftMaterial[i].get(), self.giftMaterial, 0, 100, 1))
            self.abfallProzentsatz_norm[i].set(
                norm_wert(self.abfallProzentsatz[i].get(), self.abfallProzentsatz, 10, 90, 0))
            self.abfallSzenarien_norm[i].set(norm_wert(self.abfallSzenarien[i].get(), self.abfallSzenarien, 0, 8, 0))
            self.recyclingAbsolut_norm[i].set(
                norm_wert(self.recyclingAbsolut[i].get(), self.recyclingAbsolut, 0, 1440, 1))
            self.recyclingRelativ_norm[i].set(
                norm_wert(self.recyclingRelativ[i].get(), self.recyclingRelativ, 51.2, 53.5, 1))
            self.verbrauchEnergie_norm[i].set(
                norm_wert(self.verbrauchEnergie[i].get(), self.verbrauchEnergie, 2524, 3051, 0))
            self.verbrauchMaterial_norm[i].set(
                norm_wert(self.verbrauchMaterial[i].get(), self.verbrauchMaterial, 1250, 1375, 1))
            self.kostenEffizienz_norm[i].set(
                norm_wert(self.kostenEffizienz[i].get(), self.kostenEffizienz, 0.28, 2.56, 0))
            self.kostenAufwand_norm[i].set(norm_wert(self.kostenAufwand[i].get(), self.kostenAufwand, 40, 60, 0))
            self.zeitAufwand_norm[i].set(norm_wert(self.zeitAufwand[i].get(), self.zeitAufwand, 1, 3.5, 0))
            self.flexibilität_norm[i].set(norm_wert(self.flexibilität[i].get(), self.flexibilität, 0, 8, 1))
            self.zeitEffizienz_norm[i].set(norm_wert(self.zeitEffizienz[i].get(), self.zeitEffizienz, 0, 8, 1))
            self.produktQualität_norm[i].set(norm_wert(self.produktQualität[i].get(), self.produktQualität, 0, 100, 0))
            self.innovativität_norm[i].set(norm_wert(self.innovativität[i].get(), self.innovativität, 0, 8, 1))
            self.flächenVerbrauch_norm[i].set(
                norm_wert(self.flächenVerbrauch[i].get(), self.flächenVerbrauch, 25.5, 55.5, 0))


        for i in range(4):
            self.emissionen_zg[i].set((self.emissionen_norm[i].get() % 0.5) * 2)
            self.giftMaterial_zg[i].set((self.giftMaterial_norm[i].get() % 0.5) * 2)
            self.abfallProzentsatz_zg[i].set((self.abfallProzentsatz_norm[i].get() % 0.5) * 2)
            self.abfallSzenarien_zg[i].set((self.abfallSzenarien_norm[i].get() % 0.5) * 2)
            self.recyclingAbsolut_zg[i].set((self.recyclingAbsolut_norm[i].get() % 0.5) * 2)
            self.recyclingRelativ_zg[i].set((self.recyclingRelativ_norm[i].get() % 0.5) * 2)
            self.verbrauchEnergie_zg[i].set((self.verbrauchEnergie_norm[i].get() % 0.5) * 2)
            self.verbrauchMaterial_zg[i].set((self.verbrauchMaterial_norm[i].get() % 0.5) * 2)
            self.kostenEffizienz_zg[i].set((self.kostenEffizienz_norm[i].get() % 0.5) * 2)
            self.kostenAufwand_zg[i].set((self.kostenAufwand_norm[i].get() % 0.5) * 2)
            self.zeitAufwand_zg[i].set((self.zeitAufwand_norm[i].get() % 0.5) * 2)
            self.flexibilität_zg[i].set((self.flexibilität_norm[i].get() % 0.5) * 2)
            self.zeitEffizienz_zg[i].set((self.zeitEffizienz_norm[i].get() % 0.5) * 2)
            self.produktQualität_zg[i].set((self.produktQualität_norm[i].get() % 0.5) * 2)
            self.innovativität_zg[i].set((self.innovativität_norm[i].get() % 0.5) * 2)
            self.flächenVerbrauch_zg[i].set((self.flächenVerbrauch_norm[i].get() % 0.5) * 2)


        def dimension_rechnen(*argv):
            var = 1
            for arg in argv:
                var = var * (arg * arg + (1 - arg) * (1 - arg))
            return var


        for i in range(4):
            self.sozial_oekologisch[i].set(
                dimension_rechnen(self.emissionen_zg[i].get(), self.giftMaterial_zg[i].get()))
            self.oekologisch[i].set(
                dimension_rechnen(self.abfallProzentsatz_zg[i].get(), self.abfallSzenarien_zg[i].get(),
                                  self.recyclingAbsolut_zg[i].get(),
                                  self.recyclingRelativ_zg[i].get()))
            self.oekologisch_oekonomisch[i].set(
                dimension_rechnen(self.verbrauchEnergie_zg[i].get(), self.verbrauchMaterial_zg[i].get(),
                                  self.kostenEffizienz_zg[i].get(),
                                  self.kostenAufwand_zg[i].get()))
            self.oekonomisch[i].set(
                dimension_rechnen(self.zeitAufwand_zg[i].get(), self.flexibilität_zg[i].get(),
                                  self.zeitEffizienz_zg[i].get()))
            self.sozial_oekonomisch[i].set(dimension_rechnen(self.produktQualität_zg[i].get()))
            self.sozial_oekologisch_oekonomisch[i].set(
                dimension_rechnen(self.innovativität_zg[i].get(), self.flächenVerbrauch_zg[i].get()))
            self.gsi_wert[i].set(dimension_rechnen(self.sozial_oekologisch[i].get(), self.oekologisch[i].get(),
                                                   self.oekologisch_oekonomisch[i].get(), self.oekonomisch[i].get(),
                                                   self.sozial_oekonomisch[i].get(),
                                                   self.sozial_oekologisch_oekonomisch[i].get()))

        self.controller.get_page(PageOne).auswertung_1.itemconfig(self.controller.get_page(PageOne).rect_1, fill=colourer(self.controller.get_page(StartPage).sozial_oekologisch[0]))
        self.controller.get_page(PageOne).auswertung_2.itemconfig(self.controller.get_page(PageOne).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekologisch[1]))
        self.controller.get_page(PageOne).auswertung_3.itemconfig(self.controller.get_page(PageOne).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekologisch[2]))
        self.controller.get_page(PageOne).auswertung_4.itemconfig(self.controller.get_page(PageOne).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekologisch[3]))

        self.controller.get_page(PageTwo).auswertung_1.itemconfig(self.controller.get_page(PageTwo).rect_1, fill=colourer(self.controller.get_page(StartPage).oekologisch[0]))
        self.controller.get_page(PageTwo).auswertung_2.itemconfig(self.controller.get_page(PageTwo).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekologisch[1]))
        self.controller.get_page(PageTwo).auswertung_3.itemconfig(self.controller.get_page(PageTwo).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekologisch[2]))
        self.controller.get_page(PageTwo).auswertung_4.itemconfig(self.controller.get_page(PageTwo).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekologisch[3]))

        self.controller.get_page(PageThree).auswertung_1.itemconfig(self.controller.get_page(PageThree).rect_1, fill=colourer(self.controller.get_page(StartPage).oekologisch_oekonomisch[0]))
        self.controller.get_page(PageThree).auswertung_2.itemconfig(self.controller.get_page(PageThree).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekologisch_oekonomisch[1]))
        self.controller.get_page(PageThree).auswertung_3.itemconfig(self.controller.get_page(PageThree).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekologisch_oekonomisch[2]))
        self.controller.get_page(PageThree).auswertung_4.itemconfig(self.controller.get_page(PageThree).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekologisch_oekonomisch[3]))

        self.controller.get_page(PageFour).auswertung_1.itemconfig(self.controller.get_page(PageFour).rect_1, fill=colourer(self.controller.get_page(StartPage).oekonomisch[0]))
        self.controller.get_page(PageFour).auswertung_2.itemconfig(self.controller.get_page(PageFour).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekonomisch[1]))
        self.controller.get_page(PageFour).auswertung_3.itemconfig(self.controller.get_page(PageFour).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekonomisch[2]))
        self.controller.get_page(PageFour).auswertung_4.itemconfig(self.controller.get_page(PageFour).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).oekonomisch[3]))

        self.controller.get_page(PageFive).auswertung_1.itemconfig(self.controller.get_page(PageFive).rect_1, fill=colourer(self.controller.get_page(StartPage).sozial_oekonomisch[0]))
        self.controller.get_page(PageFive).auswertung_2.itemconfig(self.controller.get_page(PageFive).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekonomisch[1]))
        self.controller.get_page(PageFive).auswertung_3.itemconfig(self.controller.get_page(PageFive).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekonomisch[2]))
        self.controller.get_page(PageFive).auswertung_4.itemconfig(self.controller.get_page(PageFive).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekonomisch[3]))

        self.controller.get_page(PageSix).auswertung_1.itemconfig(self.controller.get_page(PageSix).rect_1, fill=colourer(self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[0]))
        self.controller.get_page(PageSix).auswertung_2.itemconfig(self.controller.get_page(PageSix).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekologisch_oekonomisch[1]))
        self.controller.get_page(PageSix).auswertung_3.itemconfig(self.controller.get_page(PageSix).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekologisch_oekonomisch[2]))
        self.controller.get_page(PageSix).auswertung_4.itemconfig(self.controller.get_page(PageSix).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).sozial_oekologisch_oekonomisch[3]))
        """
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).rect_1, fill=colourer(self.controller.get_page(StartPage).gsi_wert[0]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).rect_2,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).gsi_wert[1]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).rect_3,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).gsi_wert[2]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).rect_4,
                                                                  fill=colourer(self.controller.get_page(
                                                                      StartPage).gsi_wert[3]))
        """
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_1,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch[0]))
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_2,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch[0]))
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_3,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch_oekonomisch[0]))
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_4,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekonomisch[0]))
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_5,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekonomisch[0]))
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_6,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[0]))
        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).shape_1_7,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).gsi_wert[0]))


        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_1,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch[1]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_2,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch[1]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_3,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch_oekonomisch[1]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_4,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekonomisch[1]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_5,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekonomisch[1]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_6,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[1]))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).shape_2_7,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).gsi_wert[1]))


        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_1,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch[2]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_2,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch[2]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_3,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch_oekonomisch[2]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_4,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekonomisch[2]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_5,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekonomisch[2]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_6,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[2]))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).shape_3_7,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).gsi_wert[2]))


        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_1,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch[3]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_2,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch[3]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_3,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekologisch_oekonomisch[3]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_4,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).oekonomisch[3]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_5,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekonomisch[3]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_6,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[3]))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).shape_4_7,
                                                                  fill=colourer(
                                                                      self.controller.get_page(StartPage).gsi_wert[3]))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_1_b, text = str(round(self.controller.get_page(StartPage).oekologisch[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_1_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekologisch[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_1_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekologisch[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_1_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekologisch[3].get(), 5)))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_2_b, text = str(round(self.controller.get_page(StartPage).oekonomisch[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_2_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekonomisch[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_2_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekonomisch[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_2_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekonomisch[3].get(), 5)))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_3_b, text = str(round(self.controller.get_page(StartPage).oekologisch_oekonomisch[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_3_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekologisch_oekonomisch[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_3_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekologisch_oekonomisch[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_3_b,
                                                                  text=str(round(self.controller.get_page(StartPage).oekologisch_oekonomisch[3].get(), 5)))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_4_b, text = str(round(self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_4_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_4_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_4_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekologisch_oekonomisch[3].get(), 5)))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_5_b, text = str(round(self.controller.get_page(StartPage).sozial_oekonomisch[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_5_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekonomisch[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_5_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekonomisch[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_5_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekonomisch[3].get(), 5)))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_6_b, text = str(round(self.controller.get_page(StartPage).sozial_oekologisch[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_6_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekologisch[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_6_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekologisch[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_6_b,
                                                                  text=str(round(self.controller.get_page(StartPage).sozial_oekologisch[3].get(), 5)))

        self.controller.get_page(PageEnd).auswertung_1.itemconfig(self.controller.get_page(PageEnd).text_1_7_b, text = str(round(self.controller.get_page(StartPage).gsi_wert[0].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_2.itemconfig(self.controller.get_page(PageEnd).text_2_7_b,
                                                                  text=str(round(self.controller.get_page(StartPage).gsi_wert[1].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_3.itemconfig(self.controller.get_page(PageEnd).text_3_7_b,
                                                                  text=str(round(self.controller.get_page(StartPage).gsi_wert[2].get(), 5)))
        self.controller.get_page(PageEnd).auswertung_4.itemconfig(self.controller.get_page(PageEnd).text_4_7_b,
                                                                  text=str(round(self.controller.get_page(StartPage).gsi_wert[3].get(), 5)))


    def werte_reset(self):

        # Maschine 0

        self.emissionen[0].set(0)
        self.giftMaterial[0].set(0)
        self.abfallProzentsatz[0].set(64)
        self.abfallSzenarien[0].set(0)
        self.recyclingAbsolut[0].set(1440)
        self.recyclingRelativ[0].set(51.2)
        self.verbrauchEnergie[0].set(2524)
        self.verbrauchMaterial[0].set(1375)
        self.kostenEffizienz[0].set(0.91)
        self.kostenAufwand[0].set(40)
        self.zeitAufwand[0].set(3.5)
        self.flexibilität[0].set(5)
        self.zeitEffizienz[0].set(3)
        self.produktQualität[0].set(100)
        self.innovativität[0].set(7)
        self.flächenVerbrauch[0].set(29.5)

        # Maschine 1

        self.emissionen[1].set(0)
        self.giftMaterial[1].set(0)
        self.abfallProzentsatz[1].set(90)
        self.abfallSzenarien[1].set(0)
        self.recyclingAbsolut[1].set(1440)
        self.recyclingRelativ[1].set(53.5)
        self.verbrauchEnergie[1].set(3051)
        self.verbrauchMaterial[1].set(1250)
        self.kostenEffizienz[1].set(2.56)
        self.kostenAufwand[1].set(60)
        self.zeitAufwand[1].set(1)
        self.flexibilität[1].set(6)
        self.zeitEffizienz[1].set(7)
        self.produktQualität[1].set(100)
        self.innovativität[1].set(7)
        self.flächenVerbrauch[1].set(55.5)

        # Maschine 2

        self.emissionen[2].set(0)
        self.giftMaterial[2].set(0)
        self.abfallProzentsatz[2].set(48)
        self.abfallSzenarien[2].set(0)
        self.recyclingAbsolut[2].set(1440)
        self.recyclingRelativ[2].set(52.3)
        self.verbrauchEnergie[2].set(3051)
        self.verbrauchMaterial[2].set(1312)
        self.kostenEffizienz[2].set(1.37)
        self.kostenAufwand[2].set(60)
        self.zeitAufwand[2].set(1.5)
        self.flexibilität[2].set(5)
        self.zeitEffizienz[2].set(6)
        self.produktQualität[2].set(100)
        self.innovativität[2].set(6)
        self.flächenVerbrauch[2].set(36.5)

        # Maschine 3

        self.emissionen[3].set(0)
        self.giftMaterial[3].set(0)
        self.abfallProzentsatz[3].set(10)
        self.abfallSzenarien[3].set(0)
        self.recyclingAbsolut[3].set(1440)
        self.recyclingRelativ[3].set(51.8)
        self.verbrauchEnergie[3].set(2524)
        self.verbrauchMaterial[3].set(1337)
        self.kostenEffizienz[3].set(0.28)
        self.kostenAufwand[3].set(40)
        self.zeitAufwand[3].set(2.5)
        self.flexibilität[3].set(7)
        self.zeitEffizienz[3].set(5)
        self.produktQualität[3].set(100)
        self.innovativität[3].set(5)
        self.flächenVerbrauch[3].set(25.5)


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, minsize=30)


        Buttons = Frame(self)
        button_2 = Button(Buttons, text="Next", command=lambda: controller.show_frame(PageTwo, "Ökologische Indikatoren"))
        button_3 = Button(Buttons, text="Accept", command=lambda: controller.show_frame(PageOne, "Sozial-Ökologische Indikatoren"))
        button_4 = Button(Buttons, text="Auswerten", command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick"))
        button_5 = Button(Buttons, text="Cancel", command=lambda: controller.resetter())
        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)

        self.Sozial_Ökologisch_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökologisch_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökologisch_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökologisch_4 = Frame(self, highlightbackground="black", highlightthickness=1)


        name_1 = Label(self.Sozial_Ökologisch_1, text="Flechtwickelmaschine")
        name_2 = Label(self.Sozial_Ökologisch_2, text="Multifilamentwickelmaschine90")
        name_3 = Label(self.Sozial_Ökologisch_3, text="Multifilamentwickelmaschine48")
        name_4 = Label(self.Sozial_Ökologisch_4, text="Nasswickelmaschine")

        label_1_1 = Label(self.Sozial_Ökologisch_1, text="Anteil giftige Emissionen/Abfälle   (tonne)")
        label_1_2 = Label(self.Sozial_Ökologisch_1, text="Einsatz giftiger/kritischer Materialien   (%)")
        label_2_1 = Label(self.Sozial_Ökologisch_2, text="Anteil giftige Emissionen/Abfälle   (tonne)")
        label_2_2 = Label(self.Sozial_Ökologisch_2, text="Einsatz giftiger/kritischer Materialien   (%)")
        label_3_1 = Label(self.Sozial_Ökologisch_3, text="Anteil giftige Emissionen/Abfälle   (tonne)")
        label_3_2 = Label(self.Sozial_Ökologisch_3, text="Einsatz giftiger/kritischer Materialien   (%)")
        label_4_1 = Label(self.Sozial_Ökologisch_4, text="Anteil giftige Emissionen/Abfälle   (tonne)")
        label_4_2 = Label(self.Sozial_Ökologisch_4, text="Einsatz giftiger/kritischer Materialien   (%)")

        self.entry_1_1 = Entry(self.Sozial_Ökologisch_1, textvariable = controller.get_page(StartPage).emissionen[0])
        self.entry_1_2 = Entry(self.Sozial_Ökologisch_1, textvariable = controller.get_page(StartPage).giftMaterial[0])
        self.entry_1 = Entry(self.Sozial_Ökologisch_2, textvariable = controller.get_page(StartPage).emissionen[1])
        self.entry_2 = Entry(self.Sozial_Ökologisch_2, textvariable = controller.get_page(StartPage).giftMaterial[1])
        self.entry_3_1 = Entry(self.Sozial_Ökologisch_3, textvariable = controller.get_page(StartPage).emissionen[2])
        self.entry_3_2 = Entry(self.Sozial_Ökologisch_3, textvariable = controller.get_page(StartPage).giftMaterial[2])
        self.entry_4_1 = Entry(self.Sozial_Ökologisch_4, textvariable = controller.get_page(StartPage).emissionen[3])
        self.entry_4_2 = Entry(self.Sozial_Ökologisch_4, textvariable = controller.get_page(StartPage).giftMaterial[3])

        self.auswertung_1 = Canvas(self.Sozial_Ökologisch_1, width=40, height=40)
        self.auswertung_2 = Canvas(self.Sozial_Ökologisch_2, width=40, height=40)
        self.auswertung_3 = Canvas(self.Sozial_Ökologisch_3, width=40, height=40)
        self.auswertung_4 = Canvas(self.Sozial_Ökologisch_4, width=40, height=40)

        self.rect_1 = self.auswertung_1.create_rectangle(0, 0, 40, 40, fill=colourer(controller.get_page(StartPage).sozial_oekologisch[0]))
        self.rect_2 = self.auswertung_2.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekologisch[1]))
        self.rect_3 = self.auswertung_3.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekologisch[2]))
        self.rect_4 = self.auswertung_4.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekologisch[3]))

        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=3)
        button_4.grid(row=0, column=5)
        button_5.grid(row=0, column=6)

        name_1.grid(row=0, column=0)
        name_2.grid(row=0, column=0)
        name_3.grid(row=0, column=0)
        name_4.grid(row=0, column=0)

        label_1_1.grid(row=1, column=0)
        label_1_2.grid(row=2, column=0)
        label_2_1.grid(row=1, column=0)
        label_2_2.grid(row=2, column=0)
        label_3_1.grid(row=1, column=0)
        label_3_2.grid(row=2, column=0)
        label_4_1.grid(row=1, column=0)
        label_4_2.grid(row=2, column=0)

        self.entry_1_1.grid(row=1, column=1)
        self.entry_1_2.grid(row=2, column=1)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)
        self.entry_3_1.grid(row=1, column=1)
        self.entry_3_2.grid(row=2, column=1)
        self.entry_4_1.grid(row=1, column=1)
        self.entry_4_2.grid(row=2, column=1)

        self.auswertung_1.grid(row=0, column=1)
        self.auswertung_2.grid(row=0, column=1)
        self.auswertung_3.grid(row=0, column=1)
        self.auswertung_4.grid(row=0, column=1)


        columnconfig(self.Sozial_Ökologisch_1, self.Sozial_Ökologisch_2, self.Sozial_Ökologisch_3, self.Sozial_Ökologisch_4)

        self.Sozial_Ökologisch_1.grid(row=0, column=0)
        self.Sozial_Ökologisch_2.grid(row=0, column=1)
        self.Sozial_Ökologisch_3.grid(row=1, column=0)
        self.Sozial_Ökologisch_4.grid(row=1, column=1)
        Buttons.grid(row=3, column=1)


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, minsize=30)

        Buttons = Frame(self)
        button_1 = Button(Buttons, text="Back",
                          command=lambda: controller.show_frame(PageOne, "Sozial-Ökologische Indikatoren"))
        button_2 = Button(Buttons, text="Next",
                          command=lambda: controller.show_frame(PageThree, "Ökologisch-Ökonomische Indikatoren"))
        button_3 = Button(Buttons, text="Accept", command=lambda: controller.show_frame(PageTwo, "Ökologische Indikatoren"))
        button_4 = Button(Buttons, text="Auswerten", command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick"))
        button_5 = Button(Buttons, text="Cancel", command=lambda: controller.resetter())

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)

        self.Ökologisch_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökologisch_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökologisch_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökologisch_4 = Frame(self, highlightbackground="black", highlightthickness=1)

        name_1 = Label(self.Ökologisch_1, text="Flechtwickelmaschine")
        name_2 = Label(self.Ökologisch_2, text="Multifilamentwickelmaschine90")
        name_3 = Label(self.Ökologisch_3, text="Multifilamentwickelmaschine48")
        name_4 = Label(self.Ökologisch_4, text="Nasswickelmaschine")

        label_1_1 = Label(self.Ökologisch_1, text="Abfall   (%)")
        label_1_2 = Label(self.Ökologisch_1, text="Abfallszenarien    (Skala:     0 = niedrig / 8 = hoch)")
        label_1_3 = Label(self.Ökologisch_1, text="Anteil verwendetes Recyclingmaterial(Asolut)   (g)")
        label_1_4 = Label(self.Ökologisch_1, text="Anteil verwendetes Recyclingmaterial(Relativ)   (%)")
        label_2_1 = Label(self.Ökologisch_2, text="Abfall   (%)")
        label_2_2 = Label(self.Ökologisch_2, text="Abfallszenarien    (Skala:     0 = niedrig / 8 = hoch)")
        label_2_3 = Label(self.Ökologisch_2, text="Anteil verwendetes Recyclingmaterial(Asolut)   (g)")
        label_2_4 = Label(self.Ökologisch_2, text="Anteil verwendetes Recyclingmaterial(Relativ   (%))")
        label_3_1 = Label(self.Ökologisch_3, text="Abfall   (%)")
        label_3_2 = Label(self.Ökologisch_3, text="Abfallszenarien    (Skala:     0 = niedrig / 8 = hoch)")
        label_3_3 = Label(self.Ökologisch_3, text="Anteil verwendetes Recyclingmaterial(Asolut)   (g)")
        label_3_4 = Label(self.Ökologisch_3, text="Anteil verwendetes Recyclingmaterial(Relativ)   (%)")
        label_4_1 = Label(self.Ökologisch_4, text="Abfall   (%)")
        label_4_2 = Label(self.Ökologisch_4, text="Abfallszenarien    (Skala:     0 = niedrig / 8 = hoch)")
        label_4_3 = Label(self.Ökologisch_4, text="Anteil verwendetes Recyclingmaterial(Asolut)   (g)")
        label_4_4 = Label(self.Ökologisch_4, text="Anteil verwendetes Recyclingmaterial(Relativ)   (%)")

        self.entry_1_1 = Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).abfallProzentsatz[0])
        self.entry_1_2 = Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).abfallSzenarien[0])
        self.entry_1_3 = Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).recyclingAbsolut[0])
        self.entry_1_4 = Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).recyclingRelativ[0])
        self.entry_2_1 = Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).abfallProzentsatz[1])
        self.entry_2_2 = Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).abfallSzenarien[1])
        self.entry_2_3 = Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).recyclingAbsolut[1])
        self.entry_2_4 = Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).recyclingRelativ[1])
        self.entry_3_1 = Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).abfallProzentsatz[2])
        self.entry_3_2 = Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).abfallSzenarien[2])
        self.entry_3_3 = Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).recyclingAbsolut[2])
        self.entry_3_4 = Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).recyclingRelativ[2])
        self.entry_4_1 = Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).abfallProzentsatz[3])
        self.entry_4_2 = Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).abfallSzenarien[3])
        self.entry_4_3 = Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).recyclingAbsolut[3])
        self.entry_4_4 = Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).recyclingRelativ[3])

        self.auswertung_1 = Canvas(self.Ökologisch_1, width=40, height=40)
        self.auswertung_2 = Canvas(self.Ökologisch_2, width=40, height=40)
        self.auswertung_3 = Canvas(self.Ökologisch_3, width=40, height=40)
        self.auswertung_4 = Canvas(self.Ökologisch_4, width=40, height=40)

        self.rect_1 = self.auswertung_1.create_rectangle(0, 0, 40, 40, fill=colourer(controller.get_page(StartPage).oekologisch[0]))
        self.rect_2 = self.auswertung_2.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekologisch[1]))
        self.rect_3 = self.auswertung_3.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekologisch[2]))
        self.rect_4 = self.auswertung_4.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekologisch[3]))

        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=3)
        button_4.grid(row=0, column=5)
        button_5.grid(row=0, column=6)

        name_1.grid(row=0, column=0)
        name_2.grid(row=0, column=0)
        name_3.grid(row=0, column=0)
        name_4.grid(row=0, column=0)

        label_1_1.grid(row=1, column=0)
        label_1_2.grid(row=2, column=0)
        label_1_3.grid(row=3, column=0)
        label_1_4.grid(row=4, column=0)
        label_2_1.grid(row=1, column=0)
        label_2_2.grid(row=2, column=0)
        label_2_3.grid(row=3, column=0)
        label_2_4.grid(row=4, column=0)
        label_3_1.grid(row=1, column=0)
        label_3_2.grid(row=2, column=0)
        label_3_3.grid(row=3, column=0)
        label_3_4.grid(row=4, column=0)
        label_4_1.grid(row=1, column=0)
        label_4_2.grid(row=2, column=0)
        label_4_3.grid(row=3, column=0)
        label_4_4.grid(row=4, column=0)

        self.entry_1_1.grid(row=1, column=1)
        self.entry_1_2.grid(row=2, column=1)
        self.entry_1_3.grid(row=3, column=1)
        self.entry_1_4.grid(row=4, column=1)
        self.entry_2_1.grid(row=1, column=1)
        self.entry_2_2.grid(row=2, column=1)
        self.entry_2_3.grid(row=3, column=1)
        self.entry_2_4.grid(row=4, column=1)
        self.entry_3_1.grid(row=1, column=1)
        self.entry_3_2.grid(row=2, column=1)
        self.entry_3_3.grid(row=3, column=1)
        self.entry_3_4.grid(row=4, column=1)
        self.entry_4_1.grid(row=1, column=1)
        self.entry_4_2.grid(row=2, column=1)
        self.entry_4_3.grid(row=3, column=1)
        self.entry_4_4.grid(row=4, column=1)

        self.auswertung_1.grid(row=0, column=1)
        self.auswertung_2.grid(row=0, column=1)
        self.auswertung_3.grid(row=0, column=1)
        self.auswertung_4.grid(row=0, column=1)

        columnconfig(self.Ökologisch_1, self.Ökologisch_2, self.Ökologisch_3, self.Ökologisch_4)

        self.Ökologisch_1.grid(row=0, column=0)
        self.Ökologisch_2.grid(row=0, column=1)
        self.Ökologisch_3.grid(row=1, column=0)
        self.Ökologisch_4.grid(row=1, column=1)
        Buttons.grid(row=3, column=1)


class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, minsize=30)

        Buttons = Frame(self)
        button_1 = Button(Buttons, text="Back",
                          command=lambda: controller.show_frame(PageTwo, "Ökologische Indikatoren"))
        button_2 = Button(Buttons, text="Next",
                          command=lambda: controller.show_frame(PageFour, "Ökonomische Indikatoren"))
        button_3 = Button(Buttons, text="Accept", command=lambda: controller.show_frame(PageThree, "Ökologisch-Ökonomische Indikatoren"))
        button_4 = Button(Buttons, text="Auswerten", command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick"))
        button_5 = Button(Buttons, text="Cancel", command=lambda: controller.resetter())

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)

        self.Ökologisch_Ökonomisch_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökologisch_Ökonomisch_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökologisch_Ökonomisch_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökologisch_Ökonomisch_4 = Frame(self, highlightbackground="black", highlightthickness=1)

        name_1_1 = Label(self.Ökologisch_Ökonomisch_1, text="Flechtwickelmaschine")
        name_1_2 = Label(self.Ökologisch_Ökonomisch_2, text="Multifilamentwickelmaschine90")
        name_1_3 = Label(self.Ökologisch_Ökonomisch_3, text="Multifilamentwickelmaschine48")
        name_1_4 = Label(self.Ökologisch_Ökonomisch_4, text="Nasswickelmaschine")

        label_1_1 = Label(self.Ökologisch_Ökonomisch_1, text="Energieverbrauch   (W)")
        label_1_2 = Label(self.Ökologisch_Ökonomisch_1, text="Materialverbrauch   (g)")
        label_1_3 = Label(self.Ökologisch_Ökonomisch_1, text="Kosteneffizient   (Euro/s)")
        label_1_4 = Label(self.Ökologisch_Ökonomisch_1, text="Kostenaufwand   (Euro/kg)")
        label_2_1 = Label(self.Ökologisch_Ökonomisch_2, text="Energieverbrauch   (W)")
        label_2_2 = Label(self.Ökologisch_Ökonomisch_2, text="Materialverbrauch   (g)")
        label_2_3 = Label(self.Ökologisch_Ökonomisch_2, text="Kosteneffizient   (Euro/s)")
        label_2_4 = Label(self.Ökologisch_Ökonomisch_2, text="Kostenaufwand   (Euro/kg)")
        label_3_1 = Label(self.Ökologisch_Ökonomisch_3, text="Energieverbrauch   (W)")
        label_3_2 = Label(self.Ökologisch_Ökonomisch_3, text="Materialverbrauch   (g)")
        label_3_3 = Label(self.Ökologisch_Ökonomisch_3, text="Kosteneffizient   (Euro/s)")
        label_3_4 = Label(self.Ökologisch_Ökonomisch_3, text="Kostenaufwand   (Euro/kg)")
        label_4_1 = Label(self.Ökologisch_Ökonomisch_4, text="Energieverbrauch   (W)")
        label_4_2 = Label(self.Ökologisch_Ökonomisch_4, text="Materialverbrauch   (g)")
        label_4_3 = Label(self.Ökologisch_Ökonomisch_4, text="Kosteneffizient   (Euro/s)")
        label_4_4 = Label(self.Ökologisch_Ökonomisch_4, text="Kostenaufwand   (Euro/kg)")

        self.entry_1_1 = Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).verbrauchEnergie[0])
        self.entry_1_2 = Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).verbrauchMaterial[0])
        self.entry_1_3 = Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).kostenEffizienz[0])
        self.entry_1_4 = Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).kostenAufwand[0])
        self.entry_2_1 = Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).verbrauchEnergie[1])
        self.entry_2_2 = Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).verbrauchMaterial[1])
        self.entry_2_3 = Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).kostenEffizienz[1])
        self.entry_2_4 = Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).kostenAufwand[1])
        self.entry_3_1 = Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).verbrauchEnergie[2])
        self.entry_3_2 = Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).verbrauchMaterial[2])
        self.entry_3_3 = Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).kostenEffizienz[2])
        self.entry_3_4 = Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).kostenAufwand[2])
        self.entry_4_1 = Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).verbrauchEnergie[3])
        self.entry_4_2 = Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).verbrauchMaterial[3])
        self.entry_4_3 = Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).kostenEffizienz[3])
        self.entry_4_4 = Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).kostenAufwand[3])

        self.auswertung_1 = Canvas(self.Ökologisch_Ökonomisch_1, width=40, height=40)
        self.auswertung_2 = Canvas(self.Ökologisch_Ökonomisch_2, width=40, height=40)
        self.auswertung_3 = Canvas(self.Ökologisch_Ökonomisch_3, width=40, height=40)
        self.auswertung_4 = Canvas(self.Ökologisch_Ökonomisch_4, width=40, height=40)

        self.rect_1 = self.auswertung_1.create_rectangle(0, 0, 40, 40, fill=colourer(controller.get_page(StartPage).oekologisch_oekonomisch[0]))
        self.rect_2 = self.auswertung_2.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekologisch_oekonomisch[1]))
        self.rect_3 = self.auswertung_3.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekologisch_oekonomisch[2]))
        self.rect_4 = self.auswertung_4.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekologisch_oekonomisch[3]))

        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=3)
        button_4.grid(row=0, column=5)
        button_5.grid(row=0, column=6)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_1.grid(row=1, column=0)
        label_1_2.grid(row=2, column=0)
        label_1_3.grid(row=3, column=0)
        label_1_4.grid(row=4, column=0)
        label_2_1.grid(row=1, column=0)
        label_2_2.grid(row=2, column=0)
        label_2_3.grid(row=3, column=0)
        label_2_4.grid(row=4, column=0)
        label_3_1.grid(row=1, column=0)
        label_3_2.grid(row=2, column=0)
        label_3_3.grid(row=3, column=0)
        label_3_4.grid(row=4, column=0)
        label_4_1.grid(row=1, column=0)
        label_4_2.grid(row=2, column=0)
        label_4_3.grid(row=3, column=0)
        label_4_4.grid(row=4, column=0)

        self.entry_1_1.grid(row=1, column=1)
        self.entry_1_2.grid(row=2, column=1)
        self.entry_1_3.grid(row=3, column=1)
        self.entry_1_4.grid(row=4, column=1)
        self.entry_2_1.grid(row=1, column=1)
        self.entry_2_2.grid(row=2, column=1)
        self.entry_2_3.grid(row=3, column=1)
        self.entry_2_4.grid(row=4, column=1)
        self.entry_3_1.grid(row=1, column=1)
        self.entry_3_2.grid(row=2, column=1)
        self.entry_3_3.grid(row=3, column=1)
        self.entry_3_4.grid(row=4, column=1)
        self.entry_4_1.grid(row=1, column=1)
        self.entry_4_2.grid(row=2, column=1)
        self.entry_4_3.grid(row=3, column=1)
        self.entry_4_4.grid(row=4, column=1)

        self.auswertung_1.grid(row=0, column=1)
        self.auswertung_2.grid(row=0, column=1)
        self.auswertung_3.grid(row=0, column=1)
        self.auswertung_4.grid(row=0, column=1)

        columnconfig(self.Ökologisch_Ökonomisch_1, self.Ökologisch_Ökonomisch_2, self.Ökologisch_Ökonomisch_3, self.Ökologisch_Ökonomisch_4)

        self.Ökologisch_Ökonomisch_1.grid(row=0, column=0)
        self.Ökologisch_Ökonomisch_2.grid(row=0, column=1)
        self.Ökologisch_Ökonomisch_3.grid(row=1, column=0)
        self.Ökologisch_Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=3, column=1)


class PageFour(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, minsize=30)

        Buttons = Frame(self)
        button_1 = Button(Buttons, text="Back",
                          command=lambda: controller.show_frame(PageThree, "Ökologisch-Ökonomische Indikatoren"))
        button_2 = Button(Buttons, text="Next",
                          command=lambda: controller.show_frame(PageFive, "Sozial-Ökonomische Indikatoren"))
        button_3 = Button(Buttons, text="Accept", command=lambda: controller.show_frame(PageFour, "Ökonomische Indikatoren"))
        button_4 = Button(Buttons, text="Auswerten", command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick"))
        button_5 = Button(Buttons, text="Cancel", command=lambda: controller.resetter())

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)

        self.Ökonomisch_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökonomisch_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökonomisch_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Ökonomisch_4 = Frame(self, highlightbackground="black", highlightthickness=1)

        name_1_1 = Label(self.Ökonomisch_1, text="Flechtwickelmaschine")
        name_1_2 = Label(self.Ökonomisch_2, text="Multifilamentwickelmaschine90")
        name_1_3 = Label(self.Ökonomisch_3, text="Multifilamentwickelmaschine48")
        name_1_4 = Label(self.Ökonomisch_4, text="Nasswickelmaschine")

        label_1_1 = Label(self.Ökonomisch_1, text="Zeitlicher Aufwand   (min/Tank)")
        label_1_2 = Label(self.Ökonomisch_1, text="Flexibilität   (Skala:     0 = niedrig / 8 = hoch)")
        label_1_3 = Label(self.Ökonomisch_1, text="Zeitliche Effizienz   (Skala:     0 = niedrig / 8 = hoch)")
        label_2_1 = Label(self.Ökonomisch_2, text="Zeitlicher Aufwand   (min/Tank)")
        label_2_2 = Label(self.Ökonomisch_2, text="Flexibilität   (Skala:     0 = niedrig / 8 = hoch)")
        label_2_3 = Label(self.Ökonomisch_2, text="Zeitliche Effizienz   (Skala:     0 = niedrig / 8 = hoch)")
        label_3_1 = Label(self.Ökonomisch_3, text="Zeitlicher Aufwand   (min/Tank)")
        label_3_2 = Label(self.Ökonomisch_3, text="Flexibilität   (Skala:     0 = niedrig / 8 = hoch)")
        label_3_3 = Label(self.Ökonomisch_3, text="Zeitliche Effizienz   (Skala:     0 = niedrig / 8 = hoch)")
        label_4_1 = Label(self.Ökonomisch_4, text="Zeitlicher Aufwand   (min/Tank)")
        label_4_2 = Label(self.Ökonomisch_4, text="Flexibilität   (Skala:     0 = niedrig / 8 = hoch)")
        label_4_3 = Label(self.Ökonomisch_4, text="Zeitliche Effizienz   (Skala:     0 = niedrig / 8 = hoch)")

        self.entry_1_1 = Entry(self.Ökonomisch_1, textvariable = controller.get_page(StartPage).zeitAufwand[0])
        self.entry_1_2 = Entry(self.Ökonomisch_1, textvariable = controller.get_page(StartPage).flexibilität[0])
        self.entry_1_3 = Entry(self.Ökonomisch_1, textvariable = controller.get_page(StartPage).zeitEffizienz[0])
        self.entry_2_1 = Entry(self.Ökonomisch_2, textvariable = controller.get_page(StartPage).zeitAufwand[1])
        self.entry_2_2 = Entry(self.Ökonomisch_2, textvariable = controller.get_page(StartPage).flexibilität[1])
        self.entry_2_3 = Entry(self.Ökonomisch_2, textvariable = controller.get_page(StartPage).zeitEffizienz[1])
        self.entry_3_1 = Entry(self.Ökonomisch_3, textvariable = controller.get_page(StartPage).zeitAufwand[2])
        self.entry_3_2 = Entry(self.Ökonomisch_3, textvariable = controller.get_page(StartPage).flexibilität[2])
        self.entry_3_3 = Entry(self.Ökonomisch_3, textvariable = controller.get_page(StartPage).zeitEffizienz[2])
        self.entry_4_1 = Entry(self.Ökonomisch_4, textvariable = controller.get_page(StartPage).zeitAufwand[3])
        self.entry_4_2 = Entry(self.Ökonomisch_4, textvariable = controller.get_page(StartPage).flexibilität[3])
        self.entry_4_3 = Entry(self.Ökonomisch_4, textvariable = controller.get_page(StartPage).zeitEffizienz[3])

        self.auswertung_1 = Canvas(self.Ökonomisch_1, width=40, height=40)
        self.auswertung_2 = Canvas(self.Ökonomisch_2, width=40, height=40)
        self.auswertung_3 = Canvas(self.Ökonomisch_3, width=40, height=40)
        self.auswertung_4 = Canvas(self.Ökonomisch_4, width=40, height=40)

        self.rect_1 = self.auswertung_1.create_rectangle(0, 0, 40, 40, fill=colourer(controller.get_page(StartPage).oekonomisch[0]))
        self.rect_2 = self.auswertung_2.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekonomisch[1]))
        self.rect_3 = self.auswertung_3.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekonomisch[2]))
        self.rect_4 = self.auswertung_4.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).oekonomisch[3]))

        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=3)
        button_4.grid(row=0, column=5)
        button_5.grid(row=0, column=6)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_1.grid(row=1, column=0)
        label_1_2.grid(row=2, column=0)
        label_1_3.grid(row=3, column=0)
        label_2_1.grid(row=1, column=0)
        label_2_2.grid(row=2, column=0)
        label_2_3.grid(row=3, column=0)
        label_3_1.grid(row=1, column=0)
        label_3_2.grid(row=2, column=0)
        label_3_3.grid(row=3, column=0)
        label_4_1.grid(row=1, column=0)
        label_4_2.grid(row=2, column=0)
        label_4_3.grid(row=3, column=0)

        self.entry_1_1.grid(row=1, column=1)
        self.entry_1_2.grid(row=2, column=1)
        self.entry_1_3.grid(row=3, column=1)
        self.entry_2_1.grid(row=1, column=1)
        self.entry_2_2.grid(row=2, column=1)
        self.entry_2_3.grid(row=3, column=1)
        self.entry_3_1.grid(row=1, column=1)
        self.entry_3_2.grid(row=2, column=1)
        self.entry_3_3.grid(row=3, column=1)
        self.entry_4_1.grid(row=1, column=1)
        self.entry_4_2.grid(row=2, column=1)
        self.entry_4_3.grid(row=3, column=1)

        self.auswertung_1.grid(row=0, column=1)
        self.auswertung_2.grid(row=0, column=1)
        self.auswertung_3.grid(row=0, column=1)
        self.auswertung_4.grid(row=0, column=1)

        columnconfig(self.Ökonomisch_1, self.Ökonomisch_2, self.Ökonomisch_3, self.Ökonomisch_4)

        self.Ökonomisch_1.grid(row=0, column=0)
        self.Ökonomisch_2.grid(row=0, column=1)
        self.Ökonomisch_3.grid(row=1, column=0)
        self.Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=3, column=1)


class PageFive(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, minsize=30)

        Buttons = Frame(self)
        button_1 = Button(Buttons, text="Back",
                          command=lambda: controller.show_frame(PageFour, "Ökonomische Indikatoren"))
        button_2 = Button(Buttons, text="Next",
                          command=lambda: controller.show_frame(PageSix, "Sozial-Ökonomisch_Ökologische Indikatoren"))
        button_3 = Button(Buttons, text="Accept", command=lambda: controller.show_frame(PageFive, "Sozial-Ökonomische Indikatoren"))
        button_4 = Button(Buttons, text="Auswerten", command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick"))
        button_5 = Button(Buttons, text="Cancel", command=lambda: controller.resetter())

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)

        self.Sozial_Ökonomisch_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökonomisch_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökonomisch_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökonomisch_4 = Frame(self, highlightbackground="black", highlightthickness=1)

        name_1_1 = Label(self.Sozial_Ökonomisch_1, text="Flechtwickelmaschine")
        name_1_2 = Label(self.Sozial_Ökonomisch_2, text="Multifilamentwickelmaschine90")
        name_1_3 = Label(self.Sozial_Ökonomisch_3, text="Multifilamentwickelmaschine48")
        name_1_4 = Label(self.Sozial_Ökonomisch_4, text="Nasswickelmaschine")

        label_1_1 = Label(self.Sozial_Ökonomisch_1, text="Produktqualität   (%)")
        label_1_2 = Label(self.Sozial_Ökonomisch_2, text="Produktqualität   (%)")
        label_1_3 = Label(self.Sozial_Ökonomisch_3, text="Produktqualität   (%)")
        label_1_4 = Label(self.Sozial_Ökonomisch_4, text="Produktqualität   (%)")

        self.entry_1_1 = Entry(self.Sozial_Ökonomisch_1, textvariable = controller.get_page(StartPage).produktQualität[0])
        self.entry_1_2 = Entry(self.Sozial_Ökonomisch_2, textvariable = controller.get_page(StartPage).produktQualität[1])
        self.entry_1_3 = Entry(self.Sozial_Ökonomisch_3, textvariable = controller.get_page(StartPage).produktQualität[2])
        self.entry_1_4 = Entry(self.Sozial_Ökonomisch_4, textvariable = controller.get_page(StartPage).produktQualität[3])

        self.auswertung_1 = Canvas(self.Sozial_Ökonomisch_1, width=40, height=40)
        self.auswertung_2 = Canvas(self.Sozial_Ökonomisch_2, width=40, height=40)
        self.auswertung_3 = Canvas(self.Sozial_Ökonomisch_3, width=40, height=40)
        self.auswertung_4 = Canvas(self.Sozial_Ökonomisch_4, width=40, height=40)

        self.rect_1 = self.auswertung_1.create_rectangle(0, 0, 40, 40, fill=colourer(controller.get_page(StartPage).sozial_oekonomisch[0]))
        self.rect_2 = self.auswertung_2.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekonomisch[1]))
        self.rect_3 = self.auswertung_3.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekonomisch[2]))
        self.rect_4 = self.auswertung_4.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekonomisch[3]))

        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=3)
        button_4.grid(row=0, column=5)
        button_5.grid(row=0, column=6)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_1.grid(row=1, column=0)
        label_1_2.grid(row=1, column=0)
        label_1_3.grid(row=1, column=0)
        label_1_4.grid(row=1, column=0)

        self.entry_1_1.grid(row=1, column=1)
        self.entry_1_2.grid(row=1, column=1)
        self.entry_1_3.grid(row=1, column=1)
        self.entry_1_4.grid(row=1, column=1)

        self.auswertung_1.grid(row=0, column=1)
        self.auswertung_2.grid(row=0, column=1)
        self.auswertung_3.grid(row=0, column=1)
        self.auswertung_4.grid(row=0, column=1)

        columnconfig(self.Sozial_Ökonomisch_1, self.Sozial_Ökonomisch_2, self.Sozial_Ökonomisch_3, self.Sozial_Ökonomisch_4)

        self.Sozial_Ökonomisch_1.grid(row=0, column=0)
        self.Sozial_Ökonomisch_2.grid(row=0, column=1)
        self.Sozial_Ökonomisch_3.grid(row=1, column=0)
        self.Sozial_Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=3, column=1)


class PageSix(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, minsize=30)

        Buttons = Frame(self)
        button_1 = Button(Buttons, text="Back",
                          command=lambda: controller.show_frame(PageFive, "Sozial-Ökonomische Indikatoren"))
        button_3 = Button(Buttons, text="Accept", command=lambda: controller.show_frame(PageSix, "Sozial-Ökonomisch_Ökologische Indikatoren"))
        button_4 = Button(Buttons, text="Auswerten", command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreick"))
        button_5 = Button(Buttons, text="Cancel", command=lambda: controller.resetter())

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)

        self.Sozial_Ökologisch_Ökonomisch_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökologisch_Ökonomisch_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökologisch_Ökonomisch_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.Sozial_Ökologisch_Ökonomisch_4 = Frame(self, highlightbackground="black", highlightthickness=1)

        name_1_1 = Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Flechtwickelmaschine")
        name_1_2 = Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Multifilamentwickelmaschine90")
        name_1_3 = Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Multifilamentwickelmaschine48")
        name_1_4 = Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Nasswickelmaschine")

        label_1_1 = Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Innovativität   (Skala:     0 = niedrig / 8 = hoch)")
        label_1_2 = Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Flächenverbrauch   (m^2)")
        label_2_1 = Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Innovativität   (Skala:     0 = niedrig / 8 = hoch)")
        label_2_2 = Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Flächenverbrauch   (m^2)")
        label_3_1 = Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Innovativität   (Skala:     0 = niedrig / 8 = hoch)")
        label_3_2 = Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Flächenverbrauch   (m^2)")
        label_4_1 = Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Innovativität   (Skala:     0 = niedrig / 8 = hoch)")
        label_4_2 = Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Fächenverbrauch   (m^2)")

        self.entry_1_1 = Entry(self.Sozial_Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).innovativität[0])
        self.entry_1_2 = Entry(self.Sozial_Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).flächenVerbrauch[0])
        self.entry_2_1 = Entry(self.Sozial_Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).innovativität[1])
        self.entry_2_2 = Entry(self.Sozial_Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).flächenVerbrauch[1])
        self.entry_3_1 = Entry(self.Sozial_Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).innovativität[2])
        self.entry_3_2 = Entry(self.Sozial_Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).flächenVerbrauch[2])
        self.entry_4_1 = Entry(self.Sozial_Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).innovativität[3])
        self.entry_4_2 = Entry(self.Sozial_Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).flächenVerbrauch[3])

        self.auswertung_1 = Canvas(self.Sozial_Ökologisch_Ökonomisch_1, width=40, height=40)
        self.auswertung_2 = Canvas(self.Sozial_Ökologisch_Ökonomisch_2, width=40, height=40)
        self.auswertung_3 = Canvas(self.Sozial_Ökologisch_Ökonomisch_3, width=40, height=40)
        self.auswertung_4 = Canvas(self.Sozial_Ökologisch_Ökonomisch_4, width=40, height=40)

        self.rect_1 = self.auswertung_1.create_rectangle(0, 0, 40, 40, fill=colourer(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[0]))
        self.rect_2 = self.auswertung_2.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekologisch_oekonomisch[1]))
        self.rect_3 = self.auswertung_3.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekologisch_oekonomisch[2]))
        self.rect_4 = self.auswertung_4.create_rectangle(0, 0, 40, 40, fill=colourer(
            controller.get_page(StartPage).sozial_oekologisch_oekonomisch[3]))

        button_1.grid(row=0, column=0)

        button_3.grid(row=0, column=3)
        button_4.grid(row=0, column=5)
        button_5.grid(row=0, column=6)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_1.grid(row=1, column=0)
        label_1_2.grid(row=2, column=0)
        label_2_1.grid(row=1, column=0)
        label_2_2.grid(row=2, column=0)
        label_3_1.grid(row=1, column=0)
        label_3_2.grid(row=2, column=0)
        label_4_1.grid(row=1, column=0)
        label_4_2.grid(row=2, column=0)

        self.entry_1_1.grid(row=1, column=1)
        self.entry_1_2.grid(row=2, column=1)
        self.entry_2_1.grid(row=1, column=1)
        self.entry_2_2.grid(row=2, column=1)
        self.entry_3_1.grid(row=1, column=1)
        self.entry_3_2.grid(row=2, column=1)
        self.entry_4_1.grid(row=1, column=1)
        self.entry_4_2.grid(row=2, column=1)

        self.auswertung_1.grid(row=0, column=1)
        self.auswertung_2.grid(row=0, column=1)
        self.auswertung_3.grid(row=0, column=1)
        self.auswertung_4.grid(row=0, column=1)

        columnconfig(self.Sozial_Ökologisch_Ökonomisch_1, self.Sozial_Ökologisch_Ökonomisch_2, self.Sozial_Ökologisch_Ökonomisch_3,
                     self.Sozial_Ökologisch_Ökonomisch_4)

        self.Sozial_Ökologisch_Ökonomisch_1.grid(row=0, column=0)
        self.Sozial_Ökologisch_Ökonomisch_2.grid(row=0, column=1)
        self.Sozial_Ökologisch_Ökonomisch_3.grid(row=1, column=0)
        self.Sozial_Ökologisch_Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=3, column=1)


class PageEnd(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        Buttons = Frame(self)
        button_1 = Button(Buttons, text="Back",
                          command=lambda: controller.show_frame(StartPage, "Maschinen Auswahl"))
        button_2 = Button(Buttons, text="Reset",
                          command=lambda: controller.resetter())


        self.End_1 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.End_2 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.End_3 = Frame(self, highlightbackground="black", highlightthickness=1)
        self.End_4 = Frame(self, highlightbackground="black", highlightthickness=1)

        name_1_1 = Label(self.End_1, text="Flechtwickelmaschine")
        name_1_2 = Label(self.End_2, text="Multifilamentwickelmaschine90")
        name_1_3 = Label(self.End_3, text="Multifilamentwickelmaschine48")
        name_1_4 = Label(self.End_4, text="Nasswickelmaschine")

        self.auswertung_1 = Canvas(self.End_1, width=300, height=360)
        self.auswertung_2 = Canvas(self.End_2, width=300, height=360)
        self.auswertung_3 = Canvas(self.End_3, width=300, height=360)
        self.auswertung_4 = Canvas(self.End_4, width=300, height=360)
        """
        points = [20, 360, 130, 360, 80, 240, 60, 240]
        points2 = [170, 360, 280, 360, 240, 240, 220, 240]
        points3 = [60, 240, 150, 240, 100, 120]
        points4 = [150, 240, 240, 240, 200, 120]
        points5 = [100, 120, 150, 240, 200, 120, 150, 0]
        points6 = [80, 240, 130, 360, 170, 360, 220, 240]
        """
        points = [60, 240, 100, 240, 150, 120, 150, 0]
        points2 = [20, 360, 130, 360, 80, 240, 60, 240]
        points3 = [80, 240, 130, 360, 170, 360, 220, 240]
        points4 = [170, 360, 280, 360, 240, 240, 220, 240]
        points5 = [180, 240, 240, 240, 150, 0, 150, 120]
        points6 = [98, 240, 150, 110, 202, 240]

        self.f = font.Font(size=8, weight='bold')
        self.f_alt = font.Font(size=8, weight='bold', slant = 'italic')



        self.shape_1_1 = self.auswertung_1.create_polygon(points, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch[0]))
        self.shape_1_2 = self.auswertung_1.create_polygon(points2, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch[0]))
        self.shape_1_3 = self.auswertung_1.create_polygon(points3, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch_oekonomisch[0]))
        self.shape_1_4 = self.auswertung_1.create_polygon(points4, outline='white', fill=colourer(controller.get_page(StartPage).oekonomisch[0]))
        self.shape_1_5 = self.auswertung_1.create_polygon(points5, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekonomisch[0]))
        self.shape_1_6 = self.auswertung_1.create_polygon(points6, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[0]))
        self.shape_1_7 = self.auswertung_1.create_oval(10, 10, 100, 100, outline='white', fill=colourer(controller.get_page(StartPage).gsi_wert[0]))

        self.text_1_1_a = self.auswertung_1.create_text(40, 330, text = "  Ökologisch:", anchor = 'w', width = 80, font = self.f)
        self.text_1_1_b = self.auswertung_1.create_text(70, 345, text=str(round(controller.get_page(StartPage).oekologisch[0].get(), 5)), width=80, font = self.f)
        self.text_1_2_a = self.auswertung_1.create_text(190, 330, text = "Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_1_2_b = self.auswertung_1.create_text(220, 345, text=str(round(controller.get_page(StartPage).oekonomisch[0].get(), 5)), width=80, font = self.f)
        self.text_1_3_a = self.auswertung_1.create_text(115, 270, text = "Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_1_3_b = self.auswertung_1.create_text(145, 295, text=str(round(controller.get_page(StartPage).oekologisch_oekonomisch[0].get(), 5)), width=80, font = self.f)
        self.text_1_4_a = self.auswertung_1.create_text(118, 200, text = "     Sozial- Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_1_4_b = self.auswertung_1.create_text(148, 230, text=str(round(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[0].get(), 5)), width=80, font = self.f)
        self.text_1_5_a = self.auswertung_1.create_text(170, 80, text = "Sozial - Ökonomisch:", anchor = 'w', angle = -69, font = self.f_alt)
        self.text_1_5_b = self.auswertung_1.create_text(172, 130, text=str(round(controller.get_page(StartPage).sozial_oekonomisch[0].get(), 5)), width=80, angle = -69, font = self.f_alt)
        self.text_1_6_a = self.auswertung_1.create_text(95, 180, text = "Sozial - Ökologisch:", anchor = 'w', angle = 70, font = self.f_alt)
        self.text_1_6_b = self.auswertung_1.create_text(125, 135, text=str(round(controller.get_page(StartPage).sozial_oekologisch[0].get(), 5)), width=80, angle = 70, font = self.f_alt)
        self.text_1_7_a = self.auswertung_1.create_text(45, 45, text = "GSI:", anchor = 'w', width = 80, font = self.f)
        self.text_1_7_b = self.auswertung_1.create_text(55, 60, text=str(round(controller.get_page(StartPage).gsi_wert[0].get(), 5)), width=80, font = self.f)

        self.shape_2_1 = self.auswertung_2.create_polygon(points, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch[1]))
        self.shape_2_2 = self.auswertung_2.create_polygon(points2, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch[1]))
        self.shape_2_3 = self.auswertung_2.create_polygon(points3, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch_oekonomisch[1]))
        self.shape_2_4 = self.auswertung_2.create_polygon(points4, outline='white', fill=colourer(controller.get_page(StartPage).oekonomisch[1]))
        self.shape_2_5 = self.auswertung_2.create_polygon(points5, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekonomisch[1]))
        self.shape_2_6 = self.auswertung_2.create_polygon(points6, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[1]))
        self.shape_2_7 = self.auswertung_2.create_oval(10, 10, 100, 100, outline='white',
                                                       fill=colourer(controller.get_page(StartPage).gsi_wert[1]))

        self.text_2_1_a = self.auswertung_2.create_text(40, 330, text =  "  Ökologisch:", anchor = 'w', width = 80, font = self.f)
        self.text_2_1_b = self.auswertung_2.create_text(70, 345, text=str(round(controller.get_page(StartPage).oekologisch[1].get(), 5)), width=80, font = self.f)
        self.text_2_2_a = self.auswertung_2.create_text(190, 330, text = "Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_2_2_b = self.auswertung_2.create_text(220, 345, text=str(round(controller.get_page(StartPage).oekonomisch[1].get(), 5)), width=80, font = self.f)
        self.text_2_3_a = self.auswertung_2.create_text(115, 270, text = "Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_2_3_b = self.auswertung_2.create_text(145, 295, text=str(round(controller.get_page(StartPage).oekologisch_oekonomisch[1].get(), 5)), width=80, font = self.f)
        self.text_2_4_a = self.auswertung_2.create_text(118, 200, text = "     Sozial- Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_2_4_b = self.auswertung_2.create_text(148, 230, text=str(round(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[1].get(), 5)), width=80, font = self.f)
        self.text_2_5_a = self.auswertung_2.create_text(170, 80, text = "Sozial - Ökonomisch:", anchor = 'w', angle = -69, font = self.f_alt)
        self.text_2_5_b = self.auswertung_2.create_text(172, 130, text=str(round(controller.get_page(StartPage).sozial_oekonomisch[1].get(), 5)), width=80, angle = -69, font = self.f_alt)
        self.text_2_6_a = self.auswertung_2.create_text(95, 180, text = "Sozial - Ökologisch:", anchor = 'w', angle = 70, font = self.f_alt)
        self.text_2_6_b = self.auswertung_2.create_text(125, 135, text=str(round(controller.get_page(StartPage).sozial_oekologisch[1].get(), 5)), width=80, angle = 70, font = self.f_alt)
        self.text_2_7_a = self.auswertung_2.create_text(45, 45, text = "GSI:", anchor = 'w', width = 80, font = self.f)
        self.text_2_7_b = self.auswertung_2.create_text(55, 60, text=str(round(controller.get_page(StartPage).gsi_wert[1].get(), 5)), width=80, font = self.f)



        self.shape_3_1 = self.auswertung_3.create_polygon(points, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch[2]))
        self.shape_3_2 = self.auswertung_3.create_polygon(points2, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch[2]))
        self.shape_3_3 = self.auswertung_3.create_polygon(points3, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch_oekonomisch[2]))
        self.shape_3_4 = self.auswertung_3.create_polygon(points4, outline='white', fill=colourer(controller.get_page(StartPage).oekonomisch[2]))
        self.shape_3_5 = self.auswertung_3.create_polygon(points5, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekonomisch[2]))
        self.shape_3_6 = self.auswertung_3.create_polygon(points6, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[2]))
        self.shape_3_7 = self.auswertung_3.create_oval(10, 10, 100, 100, outline='white',
                                                       fill=colourer(controller.get_page(StartPage).gsi_wert[2]))

        self.text_3_1_a = self.auswertung_3.create_text(40, 330, text =  "  Ökologisch:", anchor = 'w', width = 80, font = self.f)
        self.text_3_1_b = self.auswertung_3.create_text(70, 345, text=str(round(controller.get_page(StartPage).oekologisch[2].get(), 5)), width=80, font = self.f)
        self.text_3_2_a = self.auswertung_3.create_text(190, 330, text = "Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_3_2_b = self.auswertung_3.create_text(220, 345, text=str(round(controller.get_page(StartPage).oekonomisch[2].get(), 5)), width=80, font = self.f)
        self.text_3_3_a = self.auswertung_3.create_text(115, 270, text = "Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_3_3_b = self.auswertung_3.create_text(145, 295, text=str(round(controller.get_page(StartPage).oekologisch_oekonomisch[2].get(), 5)), width=80, font = self.f)
        self.text_3_4_a = self.auswertung_3.create_text(118, 200, text = "     Sozial- Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_3_4_b = self.auswertung_3.create_text(148, 230, text=str(round(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[2].get(), 5)), width=80, font = self.f)
        self.text_3_5_a = self.auswertung_3.create_text(170, 80, text = "Sozial - Ökonomisch:", anchor = 'w', angle = -69, font = self.f_alt)
        self.text_3_5_b = self.auswertung_3.create_text(172, 130, text=str(round(controller.get_page(StartPage).sozial_oekonomisch[2].get(), 5)), width=80, angle = -69, font = self.f_alt)
        self.text_3_6_a = self.auswertung_3.create_text(95, 180, text = "Sozial - Ökologisch:", anchor = 'w', angle = 70, font = self.f_alt)
        self.text_3_6_b = self.auswertung_3.create_text(125, 135, text=str(round(controller.get_page(StartPage).sozial_oekologisch[2].get(), 5)), width=80, angle = 70, font = self.f_alt)
        self.text_3_7_a = self.auswertung_3.create_text(45, 45, text = "GSI:", anchor = 'w', width = 80, font = self.f)
        self.text_3_7_b = self.auswertung_3.create_text(55, 60, text=str(round(controller.get_page(StartPage).gsi_wert[2].get(), 5)), width=80, font = self.f)


        self.shape_4_1 = self.auswertung_4.create_polygon(points, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch[3]))
        self.shape_4_2 = self.auswertung_4.create_polygon(points2, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch[3]))
        self.shape_4_3 = self.auswertung_4.create_polygon(points3, outline='white', fill=colourer(controller.get_page(StartPage).oekologisch_oekonomisch[3]))
        self.shape_4_4 = self.auswertung_4.create_polygon(points4, outline='white', fill=colourer(controller.get_page(StartPage).oekonomisch[3]))
        self.shape_4_5 = self.auswertung_4.create_polygon(points5, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekonomisch[3]))
        self.shape_4_6 = self.auswertung_4.create_polygon(points6, outline='white', fill=colourer(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[3]))
        self.shape_4_7 = self.auswertung_4.create_oval(10, 10, 100, 100, outline='white',
                                                       fill=colourer(controller.get_page(StartPage).gsi_wert[3]))

        self.text_4_1_a = self.auswertung_4.create_text(40, 330, text =  "  Ökologisch:", anchor = 'w', width = 80, font = self.f)
        self.text_4_1_b = self.auswertung_4.create_text(70, 345, text=str(round(controller.get_page(StartPage).oekologisch[3].get(), 5)), width=80, font = self.f)
        self.text_4_2_a = self.auswertung_4.create_text(190, 330, text = "Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_4_2_b = self.auswertung_4.create_text(220, 345, text=str(round(controller.get_page(StartPage).oekonomisch[3].get(), 5)), width=80, font = self.f)
        self.text_4_3_a = self.auswertung_4.create_text(115, 270, text = "Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_4_3_b = self.auswertung_4.create_text(145, 295, text=str(round(controller.get_page(StartPage).oekologisch_oekonomisch[3].get(), 5)), width=80, font = self.f)
        self.text_4_4_a = self.auswertung_4.create_text(118, 200, text = "     Sozial- Ökologisch-  Ökonomisch:", anchor = 'w', width = 80, font = self.f)
        self.text_4_4_b = self.auswertung_4.create_text(148, 230, text=str(round(controller.get_page(StartPage).sozial_oekologisch_oekonomisch[3].get(), 5)), width=80, font = self.f)
        self.text_4_5_a = self.auswertung_4.create_text(170, 80, text = "Sozial - Ökonomisch:", anchor = 'w', angle = -69, font = self.f_alt)
        self.text_4_5_b = self.auswertung_4.create_text(172, 130, text=str(round(controller.get_page(StartPage).sozial_oekonomisch[3].get(), 5)), width=80, angle = -69, font = self.f_alt)
        self.text_4_6_a = self.auswertung_4.create_text(95, 180, text = "Sozial - Ökologisch:", anchor = 'w', angle = 70, font = self.f_alt)
        self.text_4_6_b = self.auswertung_4.create_text(125, 135, text=str(round(controller.get_page(StartPage).sozial_oekologisch[3].get(), 5)), width=80, angle = 70, font = self.f_alt)
        self.text_4_7_a = self.auswertung_4.create_text(45, 45, text = "GSI:", anchor = 'w', width = 80, font = self.f)
        self.text_4_7_b = self.auswertung_4.create_text(55, 60, text=str(round(controller.get_page(StartPage).gsi_wert[3].get(), 5)), width=80, font = self.f)


        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        self.auswertung_1.grid(row=1, column=0)
        self.auswertung_2.grid(row=1, column=0)
        self.auswertung_3.grid(row=1, column=0)
        self.auswertung_4.grid(row=1, column=0)



        self.End_1.grid(row=0, column=0)
        self.End_2.grid(row=0, column=1)
        self.End_3.grid(row=0, column=2)
        self.End_4.grid(row=0, column=3)
        Buttons.grid(row=2, column=3)


def enabler():
    if app.frames[StartPage].var1.get() == 1:
        enable(app.get_page(PageOne).Sozial_Ökologisch_1.winfo_children())
        enable(app.get_page(PageTwo).Ökologisch_1.winfo_children())
        enable(app.get_page(PageThree).Ökologisch_Ökonomisch_1.winfo_children())
        enable(app.get_page(PageFour).Ökonomisch_1.winfo_children())
        enable(app.get_page(PageFive).Sozial_Ökonomisch_1.winfo_children())
        enable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_1.winfo_children())
    else:
        disable(app.get_page(PageOne).Sozial_Ökologisch_1.winfo_children())
        disable(app.get_page(PageTwo).Ökologisch_1.winfo_children())
        disable(app.get_page(PageThree).Ökologisch_Ökonomisch_1.winfo_children())
        disable(app.get_page(PageFour).Ökonomisch_1.winfo_children())
        disable(app.get_page(PageFive).Sozial_Ökonomisch_1.winfo_children())
        disable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_1.winfo_children())

    if app.frames[StartPage].var2.get() == 1:
        enable(app.get_page(PageOne).Sozial_Ökologisch_2.winfo_children())
        enable(app.get_page(PageTwo).Ökologisch_2.winfo_children())
        enable(app.get_page(PageThree).Ökologisch_Ökonomisch_2.winfo_children())
        enable(app.get_page(PageFour).Ökonomisch_2.winfo_children())
        enable(app.get_page(PageFive).Sozial_Ökonomisch_2.winfo_children())
        enable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_2.winfo_children())
    else:
        disable(app.get_page(PageOne).Sozial_Ökologisch_2.winfo_children())
        disable(app.get_page(PageTwo).Ökologisch_2.winfo_children())
        disable(app.get_page(PageThree).Ökologisch_Ökonomisch_2.winfo_children())
        disable(app.get_page(PageFour).Ökonomisch_2.winfo_children())
        disable(app.get_page(PageFive).Sozial_Ökonomisch_2.winfo_children())
        disable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_2.winfo_children())

    if app.frames[StartPage].var3.get() == 1:
        enable(app.get_page(PageOne).Sozial_Ökologisch_3.winfo_children())
        enable(app.get_page(PageTwo).Ökologisch_3.winfo_children())
        enable(app.get_page(PageThree).Ökologisch_Ökonomisch_3.winfo_children())
        enable(app.get_page(PageFour).Ökonomisch_3.winfo_children())
        enable(app.get_page(PageFive).Sozial_Ökonomisch_3.winfo_children())
        enable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_3.winfo_children())
    else:
        disable(app.get_page(PageOne).Sozial_Ökologisch_3.winfo_children())
        disable(app.get_page(PageTwo).Ökologisch_3.winfo_children())
        disable(app.get_page(PageThree).Ökologisch_Ökonomisch_3.winfo_children())
        disable(app.get_page(PageFour).Ökonomisch_3.winfo_children())
        disable(app.get_page(PageFive).Sozial_Ökonomisch_3.winfo_children())
        disable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_3.winfo_children())

    if app.frames[StartPage].var4.get() == 1:
        enable(app.get_page(PageOne).Sozial_Ökologisch_4.winfo_children())
        enable(app.get_page(PageTwo).Ökologisch_4.winfo_children())
        enable(app.get_page(PageThree).Ökologisch_Ökonomisch_4.winfo_children())
        enable(app.get_page(PageFour).Ökonomisch_4.winfo_children())
        enable(app.get_page(PageFive).Sozial_Ökonomisch_4.winfo_children())
        enable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_4.winfo_children())
    else:
        disable(app.get_page(PageOne).Sozial_Ökologisch_4.winfo_children())
        disable(app.get_page(PageTwo).Ökologisch_4.winfo_children())
        disable(app.get_page(PageThree).Ökologisch_Ökonomisch_4.winfo_children())
        disable(app.get_page(PageFour).Ökonomisch_4.winfo_children())
        disable(app.get_page(PageFive).Sozial_Ökonomisch_4.winfo_children())
        disable(app.get_page(PageSix).Sozial_Ökologisch_Ökonomisch_4.winfo_children())

    #app.frames[StartPage].abfallProzentsatz[0].set(app.frames[PageTwo].entry_1_1.get())

    app.after(100, enabler)

def colourer(wert):

    if wert.get() <= 0.5:

        hex_1 = hex(int(wert.get() * 255))

        if int(wert.get() * 255) > 15:
            return ('#ff' + hex_1[2:4] + '00')
        else:
            return ('#ff0' + hex_1[2:4] + '00')

    else:

        hex_1 = hex(int(255 - ((wert.get() - 0.5) * 255)))

        return ('#' + hex_1[2:4] + 'ff00')

app = H2MW()

app.after(100, enabler)
app.mainloop()
