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
import tkinter.font as tkFont
import sys
import os
import os.path
import Pmw
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

#ttk.Button(app)

def resource_path(relative_path):
    """ Returns absolute path of file, used for dev and Pyinstaller"""
    bundle_dir =  os.path.dirname(sys.argv[0])
    path_to_dat = bundle_dir + relative_path
    return path_to_dat

class H2MW(ThemedTk):
    """ Main class for the application, houses all overreaching methods"""


    def __init__(self, *args, **kwargs):
        """ Initializes the app using ThemedTk, sets up a list with all Pages and shows the Starting Page"""
        ThemedTk.__init__(self, *args, **kwargs)
        container = ttk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageEnd, MaschineWerte1, MaschineWerte2, MaschineWerte3, MaschineWerte4,
                  PageTutorial1, PageTutorial2, PageTutorial3, PageTutorial4, PageTutorial5, PageTutorial6, PageTutorial7, PageTutorial8, PageTutorial9, PageTutorial10, PageTutorial11
                  , StartTutorial1, StartTutorial2, StartTutorial3, StartTutorial4, StartTutorial5, StartTutorial6, StartTutorial7, StartTutorial8
                  , StartTutorial9, StartTutorial10, StartTutorial11, StartTutorial12, StartTutorial13, StartTutorial14):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()


        self.show_frame(StartPage, "Maschinenauswahl")

    def show_frame(self, cont, name):
        """ clears all frames from the screen and draws the requested page as set in @cont with the window-name as set in @name"""
        for fme in self.frames:  # Remove all frames
            self.frames[fme].grid_remove()
        self.get_page(StartPage).werte_update()
        frame = self.frames[cont]
        frame.grid()
        self.title(name)

    def show_first(self):
        """ shows first page, also enables only selected machines"""
        self.show_frame(PageOne, "Sozial-Ökologische Indikatoren")
        enabler()


    def get_page(self, page_name):
        """ returns pointer for page (@page_name)"""
        return self.frames[page_name]

    def resetter(self):
        """ Function that returns to Selection screen and resets values to default. To be called from End Page"""
        self.get_page(StartPage).werte_reset()
        self.show_frame(StartPage, "Maschinenauswahl")

    def acceptwerte(self, page, name):
        """ Used by the Akzeptieren Buttons in the program, recalculates values and redraws page"""
        self.get_page(StartPage).werte_update()
        self.show_frame(page, name)

def enabler():
    """ Handles the enabling/disabling of pages corresponding to selected checkboxes in Start Page"""
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


    app.update_idletasks()


def colourer(wert):
    """ Returns a colour from red to green based on a normalised 0-1 float"""
    if round(wert.get(),5) <= 0.5:

        hex_1 = hex(int(wert.get() * 255))

        if int(round(wert.get(),5) * 255) > 15:
            return ('#ff' + hex_1[2:4] + '00')
        else:
            return ('#ff0' + hex_1[2:4] + '00')

    else:

        hex_1 = hex(int(255 - ((round(wert.get(),5) - 0.5) * 255)))

        if int(255 - ((round(wert.get(),5) - 0.5) * 255)) > 15:
            return ('#' + hex_1[2:4] + 'ff00')
        else:
            return ('#0' + hex_1[3:4] + 'ff00')

def correctfloat(inp):
    """ Checks input and allows digits, nothing and a single point (must be proceeded by at least one digit)"""
    if inp.isdigit() and inp.count(".") <= 1:
        return True
    elif inp.count(".") <= 1:
        if inp.isdigit() or inp == "":
            return True
        elif isfloat(inp):
            return True
        else:
            return False
    elif inp == "":
        return True
    else:
        return False


def correct(inp):
    """ checks for digits and blank space only"""
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False

def isfloat(value):
  """ Checks if value is float, used for input checking"""
  try:
    float(value)
    return True
  except ValueError:
    return False


def columnconfig(*argv):
    """ Maintains uniformity in pages with input masks"""
    for arg in argv:
        arg.columnconfigure(0, minsize=300)
        arg.columnconfigure(1, minsize=300)


def enable(childList):
    """ Enables all widgets in a frame"""
    for child in childList:
        child.configure(state='normal')


def disable(childList):
    """ Disables all widgets in a frame"""
    for child in childList:
        child.configure(state='disabled')

def mf_v2(wert, mode):
    """Calculates MF2 Value as in Excel Sheet from normalised value"""
    if mode == 1:
        if wert < 0.5:
            v = wert * 2
            return v
        else:
            v = (wert - 0.5) * 2
            return v
    else:
        return (wert % 0.25) * 4

def mf_v1(wert, mode):
    """Calculates MF1 Value as in Excel Sheet from normalised value"""
    return (1 - mf_v2(wert, mode))

def bereiten_1(wert, modus):
    """Calculates Multiplicator Value for MF1 Values as in Excel Sheet from normalised value. @modus set for at 1 for all dimensions except GSI"""
    if modus == 1:
        if wert >= 0.5:
            return 0.5
        else:
            return 0
    else:
        if wert >= 0.75:
            return 0.75
        elif wert >= 0.5:
            return 0.5
        elif wert >= 0.25:
            return 0.25
        else:
            return 0

def bereiten_2(wert, modus):
    """Calculates Multiplicator Value for MF2 Values as in Excel Sheet from normalised value. @modus set for at 1 for all dimensions except GSI"""
    if modus == 1:
        if wert >= 0.5:
            return 1
        else:
            return 0.5
    else:
        if wert >= 0.75:
            return 1
        elif wert >= 0.5:
            return 0.75
        elif wert >= 0.25:
            return 0.5
        else:
            return 0.25

def biaskoef(wert1, wert2, wert3, wert4, wert5, wert6, length):
    """Calculates Value corresponding to S Values in Excel Sheet"""
    v = ((wert1 + wert2 + wert3 + wert4 + wert5 + wert6) / 6) * (6 / length) #ensures working formula for all dimensions
    if v > 0.875:
        return 1
    elif v > 0.625:
        return 0.75
    elif v > 0.3749:
        return 0.5
    elif v > 0.1249:
        return 0.25
    else:
        return 0

class StartPage(Frame):
    """Page where enabled machines are chosen. Default execution is also possible"""
    def dimensionrechnen(self, *argv):
        """Calculates dimension based on the formulas from the Excel Sheet"""
        mf_1 = []
        mf_2 = []
        mf_1_zw = []
        mf_2_zw = []
        bias = []
        end = []

        if len(argv) == 6:
            modus = 0
        else:
            modus = 1

        for i in range(6):
            try:
                mf_1.append(mf_v1(argv[i], modus))
            except:
                mf_1.append(0.5)    #dead value for smaller dimensions
            try:
                mf_2.append(mf_v2(argv[i], modus))
            except:
                mf_2.append(0.5)    #dead value for smaller dimensions

            try:
                mf_1_zw.append(bereiten_1(argv[i], modus))
            except:
                mf_1_zw.append(0)    #dead value for smaller dimensions
            try:
                mf_2_zw.append(bereiten_2(argv[i], modus))
            except:
                mf_2_zw.append(0)    #dead value for smaller dimensions

        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 )) #creates coefficient list
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_1_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_1_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_1_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_1_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_1_zw[4], mf_2_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_1_zw[5], len(argv)) ,5 ))
        bias.append(round(biaskoef(mf_2_zw[0], mf_2_zw[1], mf_2_zw[2], mf_2_zw[3], mf_2_zw[4], mf_2_zw[5], len(argv)) ,5 ))

        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[0], 5)) #creates values list to be added for dimension, most are 0
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[1], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[2], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[3], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[4], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[5], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[6], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[7], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[8], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[9], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[10], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[11], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[12], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[13], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[14], 5))
        end.append(round(mf_1[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[15], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[16], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[17], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[18], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[19], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[20], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[21], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[22], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[23], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[24], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[25], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[26], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[27], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[28], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[29], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[30], 5))
        end.append(round(mf_1[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[31], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[32], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[33], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[34], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[35], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[36], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[37], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[38], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[39], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[40], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[41], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[42], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[43], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[44], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[45], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[46], 5))
        end.append(round(mf_2[0] * mf_1[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[47], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[48], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[49], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[50], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[51], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[52], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[53], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[54], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_1[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[55], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_1[5] * bias[56], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_1[4] * mf_2[5] * bias[57], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_1[5] * bias[58], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_1[3] * mf_2[4] * mf_2[5] * bias[59], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_1[5] * bias[60], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_1[4] * mf_2[5] * bias[61], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_1[5] * bias[62], 5))
        end.append(round(mf_2[0] * mf_2[1] * mf_2[2] * mf_2[3] * mf_2[4] * mf_2[5] * bias[63], 5))

        return sum(end)


    def boot(self):
        """Creates default values and variables to be used in the program"""
        self.emissionen = []
        for i in range(4):
            self.emissionen.append(DoubleVar())
        self.giftMaterial = []
        for i in range(4):
            self.giftMaterial.append(IntVar())
        self.abfallProzentsatz = []  # Deklaration der Werte Listen
        for i in range(4):
            self.abfallProzentsatz.append(DoubleVar())
        self.abfallSzenarien = []
        for i in range(4):
            self.abfallSzenarien.append(IntVar())
        self.recyclingAbsolut = []
        for i in range(4):
            self.recyclingAbsolut.append(DoubleVar())
        self.recyclingRelativ = []
        for i in range(4):
            self.recyclingRelativ.append(DoubleVar())
        self.verbrauchEnergie = []
        for i in range(4):
            self.verbrauchEnergie.append(DoubleVar())
        self.verbrauchMaterial = []
        for i in range(4):
            self.verbrauchMaterial.append(DoubleVar())
        self.kostenEffizienz = []
        for i in range(4):
            self.kostenEffizienz.append(DoubleVar())
        self.kostenAufwand = []
        for i in range(4):
            self.kostenAufwand.append(DoubleVar())
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
            self.produktQualität.append(DoubleVar())
        self.innovativität = []
        for i in range(4):
            self.innovativität.append(IntVar())
        self.flächenVerbrauch = []
        for i in range(4):
            self.flächenVerbrauch.append(DoubleVar())

        self.werte_reset()


        def norm_wert(wert, wertList, min, max, mode: bool):  # normalised value function

            if min == max:
                return 1

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

        for i in range(4):
            self.emissionen_norm[i].set(norm_wert(self.emissionen[i].get(), self.emissionen, 300.75, 501.41, 0))
            self.giftMaterial_norm[i].set(norm_wert(self.giftMaterial[i].get(), self.giftMaterial, 1, 5, 0))
            self.abfallProzentsatz_norm[i].set(
                norm_wert(self.abfallProzentsatz[i].get(), self.abfallProzentsatz, 10, 90, 0))
            self.abfallSzenarien_norm[i].set(norm_wert(self.abfallSzenarien[i].get(), self.abfallSzenarien, 1, 1, 1))
            self.recyclingAbsolut_norm[i].set(
                norm_wert(self.recyclingAbsolut[i].get(), self.recyclingAbsolut, 1440, 1440, 1))
            self.recyclingRelativ_norm[i].set(
                norm_wert(self.recyclingRelativ[i].get(), self.recyclingRelativ, 51.2, 53.5, 1))
            self.verbrauchEnergie_norm[i].set(
                norm_wert(self.verbrauchEnergie[i].get(), self.verbrauchEnergie, 750, 1250.41, 0))
            self.verbrauchMaterial_norm[i].set(
                norm_wert(self.verbrauchMaterial[i].get(), self.verbrauchMaterial, 1250, 1375, 0))
            self.kostenEffizienz_norm[i].set(
                norm_wert(self.kostenEffizienz[i].get(), self.kostenEffizienz, 0.28, 2.56, 0))
            self.kostenAufwand_norm[i].set(norm_wert(self.kostenAufwand[i].get(), self.kostenAufwand, 40, 60, 0))
            self.zeitAufwand_norm[i].set(norm_wert(self.zeitAufwand[i].get(), self.zeitAufwand, 1, 3.5, 0))
            self.flexibilität_norm[i].set(norm_wert(self.flexibilität[i].get(), self.flexibilität, 5, 7, 1))
            self.zeitEffizienz_norm[i].set(norm_wert(self.zeitEffizienz[i].get(), self.zeitEffizienz, 3, 7, 1))
            self.produktQualität_norm[i].set(norm_wert(self.produktQualität[i].get(), self.produktQualität, 1, 3.5, 0))
            self.innovativität_norm[i].set(norm_wert(self.innovativität[i].get(), self.innovativität, 4, 7, 1))
            self.flächenVerbrauch_norm[i].set(
                norm_wert(self.flächenVerbrauch[i].get(), self.flächenVerbrauch, 25.5, 55.5, 0))


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


        for i in range(4):
            self.sozial_oekologisch[i].set(self.dimensionrechnen(self.emissionen_norm[i].get(), self.giftMaterial_norm[i].get()))
            self.oekologisch[i].set(
                self.dimensionrechnen(self.abfallProzentsatz_norm[i].get(),self.abfallSzenarien_norm[i].get(),self.recyclingAbsolut_norm[i].get(), self.recyclingRelativ_norm[i].get()))
            self.oekologisch_oekonomisch[i].set(
                self.dimensionrechnen(self.verbrauchEnergie_norm[i].get(), self.verbrauchMaterial_norm[i].get(),self.kostenEffizienz_norm[i].get(),self.kostenAufwand_norm[i].get()))
            self.oekonomisch[i].set(
                self.dimensionrechnen(self.zeitAufwand_norm[i].get(), self.flexibilität_norm[i].get(),
                                  self.zeitEffizienz_norm[i].get()))
            self.sozial_oekonomisch[i].set(self.dimensionrechnen(self.produktQualität_norm[i].get()))
            self.sozial_oekologisch_oekonomisch[i].set(
                self.dimensionrechnen(self.innovativität_norm[i].get(),self.flächenVerbrauch_norm[i].get()))
            self.gsi_wert[i].set(self.dimensionrechnen(self.sozial_oekologisch[i].get(), self.oekologisch[i].get(), self.oekologisch_oekonomisch[i].get(), self.oekonomisch[i].get(),
                                                       self.sozial_oekonomisch[i].get(), self.sozial_oekologisch_oekonomisch[i].get()))


    def __init__(self, parent, controller):
        """Initializes Starting Page."""
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(1, minsize=30) #Vertical spacing
        self.columnconfigure(3, minsize=10)


        first = ttk.Frame(self)
        buttons_first = ttk.Frame(first)
        first.rowconfigure(5, minsize=50)   #Horizontal spacing
        first.rowconfigure(0, minsize=20)

        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()
        self.var4 = BooleanVar()

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)

        button_1 = ttk.Button(buttons_first, text="Standardparameter verwenden", command=lambda: self.default())
        button_2 = ttk.Button(buttons_first, text="Parameter ändern", command=lambda: controller.show_first())
        button_3 = ttk.Button(buttons_first, text="Tutorial",
                              command=lambda: controller.show_frame(StartTutorial1, "Tutorial (1/14)"))

        label_1 = ttk.Label(first, text="Flechtmaschine", font = tkFont.Font(family = "helvetica", size=12))
        label_2 = ttk.Label(first, text="Multifilamentwickelmaschine 90", font = tkFont.Font(family = "helvetica", size=12))
        label_3 = ttk.Label(first, text="Multifilamentwickelmaschine 48", font = tkFont.Font(family = "helvetica", size=12))
        label_4 = ttk.Label(first, text="Nasswickelmaschine", font = tkFont.Font(family = "helvetica", size=12))

        check_1 = ttk.Checkbutton(first, variable=self.var1, onvalue=1, offvalue=0)
        check_2 = ttk.Checkbutton(first, variable=self.var2, onvalue=1, offvalue=0)
        check_3 = ttk.Checkbutton(first, variable=self.var3, onvalue=1, offvalue=0)
        check_4 = ttk.Checkbutton(first, variable=self.var4, onvalue=1, offvalue=0)

        load = Image.open(resource_path('/IMAGES/H2MW_LOGO.png'))
        load = load.resize((550, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render

        label_1.grid(row=1, column=0)
        label_3.grid(row=2, column=0)
        label_2.grid(row=3, column=0)
        label_4.grid(row=4, column=0)

        check_1.grid(row=1, column=1)
        check_3.grid(row=2, column=1)
        check_2.grid(row=3, column=1)
        check_4.grid(row=4, column=1)

        button_1.grid(row=0, column=0)
        button_2.grid(row=0, column=1)
        button_3.grid(row=0, column=2)


        buttons_first.grid(row=6, column=0)
        img.grid(row=0, column=0)
        first.grid(row=0, column=2)

        self.boot()

    def default(self):
        """Runs default values and goes to End Page"""
        self.werte_reset()
        self.werte_update()
        self.controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck")

    def setter(self, subject, value, default):
        """Sets blank spaces to default values when pages are switched"""
        if value == "":
            subject.set(default)
        else:
            subject.set(value)


    def errorstring(self, value, checkvalue, errormsg, msg, checkint, mode):
        """Checks if @value is smaller or greater (@mode) than @checkvalue and add corresponding lines to error message"""
        if mode == 0:
            if value.get() > checkvalue:
                errormsg.set(errormsg.get() + msg)
                checkint.set(1)
                value.set(checkvalue)
        else:
            if value.get() < checkvalue:
                errormsg.set(errormsg.get() + msg)
                checkint.set(1)
                value.set(checkvalue)

    def werte_update(self):
        """Recalculates all values"""
        self.setter(self.emissionen[0], self.controller.get_page(PageOne).entry_1_1.get(), 398.47)
        self.setter(self.giftMaterial[0], self.controller.get_page(PageOne).entry_1_2.get(), 1)
        self.setter(self.emissionen[1], self.controller.get_page(PageOne).entry_1.get(), 501.41)
        self.setter(self.giftMaterial[1], self.controller.get_page(PageOne).entry_2.get(), 3)
        self.setter(self.emissionen[2], self.controller.get_page(PageOne).entry_3_1.get(), 491.35)
        self.setter(self.giftMaterial[2], self.controller.get_page(PageOne).entry_3_2.get(), 3)
        self.setter(self.emissionen[3], self.controller.get_page(PageOne).entry_4_1.get(), 300.75)
        self.setter(self.giftMaterial[3], self.controller.get_page(PageOne).entry_4_2.get(), 5)

        self.setter(self.abfallProzentsatz[0], self.controller.get_page(PageTwo).entry_1_1.get(), 64)
        self.setter(self.abfallSzenarien[0], self.controller.get_page(PageTwo).entry_1_2.get(), 1)
        self.setter(self.recyclingAbsolut[0], self.controller.get_page(PageTwo).entry_1_3.get(), 1440)
        self.setter(self.recyclingRelativ[0], self.controller.get_page(PageTwo).entry_1_4.get(), 51.2)
        self.setter(self.abfallProzentsatz[1], self.controller.get_page(PageTwo).entry_2_1.get(), 90)
        self.setter(self.abfallSzenarien[1], self.controller.get_page(PageTwo).entry_2_2.get(), 1)
        self.setter(self.recyclingAbsolut[1], self.controller.get_page(PageTwo).entry_2_3.get(), 1440)
        self.setter(self.recyclingRelativ[1], self.controller.get_page(PageTwo).entry_2_4.get(), 53.5)
        self.setter(self.abfallProzentsatz[2], self.controller.get_page(PageTwo).entry_3_1.get(), 48)
        self.setter(self.abfallSzenarien[2], self.controller.get_page(PageTwo).entry_3_2.get(), 1)
        self.setter(self.recyclingAbsolut[2], self.controller.get_page(PageTwo).entry_3_3.get(), 1440)
        self.setter(self.recyclingRelativ[2], self.controller.get_page(PageTwo).entry_3_4.get(), 52.3)
        self.setter(self.abfallProzentsatz[3], self.controller.get_page(PageTwo).entry_4_1.get(), 10)
        self.setter(self.abfallSzenarien[3], self.controller.get_page(PageTwo).entry_4_2.get(), 1)
        self.setter(self.recyclingAbsolut[3], self.controller.get_page(PageTwo).entry_4_3.get(), 1440)
        self.setter(self.recyclingRelativ[3], self.controller.get_page(PageTwo).entry_4_4.get(), 51.8)

        self.setter(self.verbrauchEnergie[0], self.controller.get_page(PageThree).entry_1_1.get(), 993.7)
        self.setter(self.verbrauchMaterial[0], self.controller.get_page(PageThree).entry_1_2.get(), 1375)
        self.setter(self.kostenEffizienz[0], self.controller.get_page(PageThree).entry_1_3.get(), 0.91)
        self.setter(self.kostenAufwand[0], self.controller.get_page(PageThree).entry_1_4.get(), 40)
        self.setter(self.verbrauchEnergie[1], self.controller.get_page(PageThree).entry_2_1.get(), 1250.41)
        self.setter(self.verbrauchMaterial[1], self.controller.get_page(PageThree).entry_2_2.get(), 1250)
        self.setter(self.kostenEffizienz[1], self.controller.get_page(PageThree).entry_2_3.get(), 2.56)
        self.setter(self.kostenAufwand[1], self.controller.get_page(PageThree).entry_2_4.get(), 60)
        self.setter(self.verbrauchEnergie[2], self.controller.get_page(PageThree).entry_3_1.get(), 1225.3)
        self.setter(self.verbrauchMaterial[2], self.controller.get_page(PageThree).entry_3_2.get(), 1312)
        self.setter(self.kostenEffizienz[2], self.controller.get_page(PageThree).entry_3_3.get(), 1.37)
        self.setter(self.kostenAufwand[2], self.controller.get_page(PageThree).entry_3_4.get(), 60)
        self.setter(self.verbrauchEnergie[3], self.controller.get_page(PageThree).entry_4_1.get(), 750)
        self.setter(self.verbrauchMaterial[3], self.controller.get_page(PageThree).entry_4_2.get(), 1337)
        self.setter(self.kostenEffizienz[3], self.controller.get_page(PageThree).entry_4_3.get(), 0.28)
        self.setter(self.kostenAufwand[3], self.controller.get_page(PageThree).entry_4_4.get(), 40)

        self.setter(self.zeitAufwand[0], self.controller.get_page(PageFour).entry_1_1.get(), 3.5)
        self.setter(self.flexibilität[0], self.controller.get_page(PageFour).entry_1_2.get(), 5)
        self.setter(self.zeitEffizienz[0], self.controller.get_page(PageFour).entry_1_3.get(), 3)
        self.setter(self.zeitAufwand[1], self.controller.get_page(PageFour).entry_2_1.get(), 1)
        self.setter(self.flexibilität[1], self.controller.get_page(PageFour).entry_2_2.get(), 6)
        self.setter(self.zeitEffizienz[1], self.controller.get_page(PageFour).entry_2_3.get(), 7)
        self.setter(self.zeitAufwand[2], self.controller.get_page(PageFour).entry_3_1.get(), 1.5)
        self.setter(self.flexibilität[2], self.controller.get_page(PageFour).entry_3_2.get(), 5)
        self.setter(self.zeitEffizienz[2], self.controller.get_page(PageFour).entry_3_3.get(), 6)
        self.setter(self.zeitAufwand[3], self.controller.get_page(PageFour).entry_4_1.get(), 2.5)
        self.setter(self.flexibilität[3], self.controller.get_page(PageFour).entry_4_2.get(), 7)
        self.setter(self.zeitEffizienz[3], self.controller.get_page(PageFour).entry_4_3.get(), 5)

        self.setter(self.produktQualität[0], self.controller.get_page(PageFive).entry_1_1.get(), 1)
        self.setter(self.produktQualität[1], self.controller.get_page(PageFive).entry_1_2.get(), 3.5)
        self.setter(self.produktQualität[2], self.controller.get_page(PageFive).entry_1_3.get(), 3.5)
        self.setter(self.produktQualität[3], self.controller.get_page(PageFive).entry_1_4.get(), 2)

        self.setter(self.innovativität[0], self.controller.get_page(PageSix).entry_1_1.get(), 4)
        self.setter(self.flächenVerbrauch[0], self.controller.get_page(PageSix).entry_1_2.get(), 25.5)
        self.setter(self.innovativität[1], self.controller.get_page(PageSix).entry_2_1.get(), 7)
        self.setter(self.flächenVerbrauch[1], self.controller.get_page(PageSix).entry_2_2.get(), 55.5)
        self.setter(self.innovativität[2], self.controller.get_page(PageSix).entry_3_1.get(), 6)
        self.setter(self.flächenVerbrauch[2], self.controller.get_page(PageSix).entry_3_2.get(), 36.5)
        self.setter(self.innovativität[3], self.controller.get_page(PageSix).entry_4_1.get(), 5)
        self.setter(self.flächenVerbrauch[3], self.controller.get_page(PageSix).entry_4_2.get(), 28.5)

        self.check = IntVar()
        self.check.set(0)

        self.errormsg = StringVar()
        self.errormsg.set("Die eingegebene Werte für folgende Indikatoren sind größer als erlaubt:\n")

        self.errorstring(self.giftMaterial[0], 5, self.errormsg, "\n-Flechtmaschine (Sozio-ökologische Kritikalität des Materials): Skalawert überschreitet 5.", self.check, 0)
        self.errorstring(self.abfallSzenarien[0], 1, self.errormsg, "\n-Flechtmaschine (Abfallszenarien): Skalawert überschreitet 1.", self.check, 0)
        self.errorstring(self.recyclingRelativ[0], 100, self.errormsg, "\n-Flechtmaschine (Anteil verwendetes Recyclingmaterial (Relativ)): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.flexibilität[0], 7, self.errormsg, "\n-Flechtmaschine (Flexibilität): Skalawert überschreitet 7.", self.check, 0)
        self.errorstring(self.zeitEffizienz[0], 7, self.errormsg, "\n-Flechtmaschine (Zeitliche Effizienz): Skalawert überschreitet 7.", self.check, 0)
        self.errorstring(self.produktQualität[0], 100, self.errormsg, "\n-Flechtmaschine (Produktqualität): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.innovativität[0], 7, self.errormsg, "\n-Flechtmaschine (Innovativität): Skalawert überschreitet 7.", self.check, 0)
        self.errorstring(self.giftMaterial[0], 1, self.errormsg, "\n-Flechtmaschine (Sozio-ökologische Kritikalität des Materials): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.abfallSzenarien[0], 1, self.errormsg, "\n-Flechtmaschine (Abfallszenarien): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.flexibilität[0], 5, self.errormsg, "\n-Flechtmaschine (Flexibilität): Skalawert unterschreitet 5.", self.check, 1)
        self.errorstring(self.zeitEffizienz[0], 3, self.errormsg, "\n-Flechtmaschine (Zeitliche Effizienz): Skalawert unterschreitet 3.", self.check, 1)
        self.errorstring(self.innovativität[0], 4, self.errormsg, "\n-Flechtmaschine (Innovativität): Skalawert unterschreitet 4.", self.check, 1)

        self.errorstring(self.giftMaterial[1], 5, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Sozio-ökologische Kritikalität des Materials): Skalawert überschreitet 5.", self.check, 0)
        self.errorstring(self.abfallSzenarien[1], 1, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Abfallszenarien): Skalawert überschreitet 1.", self.check, 0)
        self.errorstring(self.recyclingRelativ[1], 100, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Anteil verwendetes Recyclingmaterial (Relativ)): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.flexibilität[1], 7, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Flexibilität): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.zeitEffizienz[1], 7, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Zeitliche Effizienz): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.produktQualität[1], 100, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Produktqualität): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.innovativität[1], 7, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Innovativität): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.giftMaterial[1], 1, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Sozio-ökologische Kritikalität des Materials): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.abfallSzenarien[1], 1, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Abfallszenarien): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.flexibilität[1], 5, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Flexibilität): Skalawert unterschreitet 5.", self.check, 1)
        self.errorstring(self.zeitEffizienz[1], 3, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Zeitliche Effizienz): Skalawert unterschreitet 3.", self.check, 1)
        self.errorstring(self.innovativität[1], 4, self.errormsg, "\n-Multifilamentwickelmaschine 90 (Innovativität): Skalawert unterschreitet 4.", self.check, 1)

        self.errorstring(self.giftMaterial[2], 5, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Sozio-ökologische Kritikalität des Materials): Skalawert überschreitet 5.", self.check, 0)
        self.errorstring(self.abfallSzenarien[2], 1, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Abfallszenarien): Skalawert überschreitet 1.", self.check, 0)
        self.errorstring(self.recyclingRelativ[2], 100, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Anteil verwendetes Recyclingmaterial (Relativ)): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.flexibilität[2], 7, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Flexibilität): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.zeitEffizienz[2], 7, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Zeitliche Effizienz): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.produktQualität[2], 100, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Produktqualität): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.innovativität[2], 7, self.errormsg, "\n-Mulftifilamentwickelmaschine 48 (Innovativität): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.giftMaterial[2], 1, self.errormsg, "\n-Multifilamentwickelmaschine 48 (Sozio-ökologische Kritikalität des Materials): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.abfallSzenarien[2], 1, self.errormsg, "\n-Multifilamentwickelmaschine 48 (Abfallszenarien): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.flexibilität[2], 5, self.errormsg, "\n-Multifilamentwickelmaschine 48 (Flexibilität): Skalawert unterschreitet 5.", self.check, 1)
        self.errorstring(self.zeitEffizienz[2], 3, self.errormsg, "\n-Multifilamentwickelmaschine 48 (Zeitliche Effizienz): Skalawert unterschreitet 3.", self.check, 1)
        self.errorstring(self.innovativität[2], 4, self.errormsg, "\n-Multifilamentwickelmaschine 48 (Innovativität): Skalawert unterschreitet 4.", self.check, 1)

        self.errorstring(self.giftMaterial[3], 5, self.errormsg, "\n-Nasswickelmaschine (Sozio-ökologische Kritikalität des Materials): Skalawert überschreitet 5.", self.check, 0)
        self.errorstring(self.abfallSzenarien[3], 1, self.errormsg, "\n-Nasswickelmaschine (Abfallszenarien): Skalawert überschreitet 1.", self.check, 0)
        self.errorstring(self.recyclingRelativ[3], 100, self.errormsg, "\n-Nasswickelmaschine (Anteil verwendetes Recyclingmaterial (Relativ)): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.flexibilität[3], 7, self.errormsg, "\n-Nasswickelmaschine (Flexibilität): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.zeitEffizienz[3], 7, self.errormsg, "\n-Nasswickelmaschine (Zeitliche Effizienz): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.produktQualität[3], 100, self.errormsg, "\n-Nasswickelmaschine (Produktqualität): Prozentzatz überschreitet 100%.", self.check, 0)
        self.errorstring(self.innovativität[3], 7, self.errormsg, "\n-Nasswickelmaschine (Innovativität): Skalawert überschreitet 8.", self.check, 0)
        self.errorstring(self.giftMaterial[3], 1, self.errormsg, "\n-Nasswickelmaschine (Sozio-ökologische Kritikalität des Materials): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.abfallSzenarien[3], 1, self.errormsg, "\n-Nasswickelmaschine (Abfallszenarien): Skalawert unterschreitet 1.", self.check, 1)
        self.errorstring(self.flexibilität[3], 5, self.errormsg, "\n-Nasswickelmaschine (Flexibilität): Skalawert unterschreitet 5.", self.check, 1)
        self.errorstring(self.zeitEffizienz[3], 3, self.errormsg, "\n-Nasswickelmaschine (Zeitliche Effizienz): Skalawert unterschreitet 3.", self.check, 1)
        self.errorstring(self.innovativität[3], 4, self.errormsg, "\n-Nasswickelmaschine (Innovativität): Skalawert unterschreitet 4.", self.check, 1)


        if self.check.get() == 1:
            messagebox.showerror("Fehler!", self.errormsg.get() + "\n\nDie Indikatoren wurden zu ihren (maximal/minimalen) erlaubten Werten gesetzt.")


        self.check.set(0)


        def norm_wert(wert, wertList, min, max, mode: bool):  # normierte Wert Funktion

            if min == max:
                return 1

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
            self.emissionen_norm[i].set(norm_wert(self.emissionen[i].get(), self.emissionen, 300.75, 501.41, 0))
            self.giftMaterial_norm[i].set(norm_wert(self.giftMaterial[i].get(), self.giftMaterial, 1, 5, 0))
            self.abfallProzentsatz_norm[i].set(
                norm_wert(self.abfallProzentsatz[i].get(), self.abfallProzentsatz, 10, 90, 0))
            self.abfallSzenarien_norm[i].set(norm_wert(self.abfallSzenarien[i].get(), self.abfallSzenarien, 1, 1, 1))
            self.recyclingAbsolut_norm[i].set(
                norm_wert(self.recyclingAbsolut[i].get(), self.recyclingAbsolut, 1440, 1440, 1))
            self.recyclingRelativ_norm[i].set(
                norm_wert(self.recyclingRelativ[i].get(), self.recyclingRelativ, 51.2, 53.5, 1))
            self.verbrauchEnergie_norm[i].set(
                norm_wert(self.verbrauchEnergie[i].get(), self.verbrauchEnergie, 750, 1250.41, 0))
            self.verbrauchMaterial_norm[i].set(
                norm_wert(self.verbrauchMaterial[i].get(), self.verbrauchMaterial, 1250, 1375, 0))
            self.kostenEffizienz_norm[i].set(
                norm_wert(self.kostenEffizienz[i].get(), self.kostenEffizienz, 0.28, 2.56, 0))
            self.kostenAufwand_norm[i].set(norm_wert(self.kostenAufwand[i].get(), self.kostenAufwand, 40, 60, 0))
            self.zeitAufwand_norm[i].set(norm_wert(self.zeitAufwand[i].get(), self.zeitAufwand, 1, 3.5, 0))
            self.flexibilität_norm[i].set(norm_wert(self.flexibilität[i].get(), self.flexibilität, 5, 7, 1))
            self.zeitEffizienz_norm[i].set(norm_wert(self.zeitEffizienz[i].get(), self.zeitEffizienz, 3, 7, 1))
            self.produktQualität_norm[i].set(norm_wert(self.produktQualität[i].get(), self.produktQualität, 1, 3.5, 0))
            self.innovativität_norm[i].set(norm_wert(self.innovativität[i].get(), self.innovativität, 4, 7, 1))
            self.flächenVerbrauch_norm[i].set(
                norm_wert(self.flächenVerbrauch[i].get(), self.flächenVerbrauch, 25.5, 55.5, 0))




        for i in range(4):
            self.sozial_oekologisch[i].set(self.dimensionrechnen(self.emissionen_norm[i].get(), self.giftMaterial_norm[i].get()))
            self.oekologisch[i].set(
                self.dimensionrechnen(self.abfallProzentsatz_norm[i].get(),self.abfallSzenarien_norm[i].get(),self.recyclingAbsolut_norm[i].get(), self.recyclingRelativ_norm[i].get()))
            self.oekologisch_oekonomisch[i].set(
                self.dimensionrechnen(self.verbrauchEnergie_norm[i].get(), self.verbrauchMaterial_norm[i].get(),self.kostenEffizienz_norm[i].get(),self.kostenAufwand_norm[i].get()))
            self.oekonomisch[i].set(
                self.dimensionrechnen(self.zeitAufwand_norm[i].get(), self.flexibilität_norm[i].get(),
                                  self.zeitEffizienz_norm[i].get()))
            self.sozial_oekonomisch[i].set(self.dimensionrechnen(self.produktQualität_norm[i].get()))
            self.sozial_oekologisch_oekonomisch[i].set(
                self.dimensionrechnen(self.innovativität_norm[i].get(),self.flächenVerbrauch_norm[i].get()))
            self.gsi_wert[i].set(self.dimensionrechnen(self.sozial_oekologisch[i].get(), self.oekologisch[i].get(), self.oekologisch_oekonomisch[i].get(), self.oekonomisch[i].get(),
                                                       self.sozial_oekonomisch[i].get(), self.sozial_oekologisch_oekonomisch[i].get()))



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

        self.controller.get_page(MaschineWerte1).wert_1_1.config(text= round(self.controller.get_page(StartPage).emissionen_norm[0].get(), 5), bg = colourer(self.controller.get_page(StartPage).emissionen_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_1_2.config(
            text=round(self.controller.get_page(StartPage).giftMaterial_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).giftMaterial_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_2_1.config(
            text=round(self.controller.get_page(StartPage).abfallProzentsatz_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallProzentsatz_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_2_2.config(
            text=round(self.controller.get_page(StartPage).abfallSzenarien_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallSzenarien_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_2_3.config(
            text=round(self.controller.get_page(StartPage).recyclingAbsolut_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingAbsolut_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_2_4.config(
            text=round(self.controller.get_page(StartPage).recyclingRelativ_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingRelativ_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_3_1.config(
            text=round(self.controller.get_page(StartPage).verbrauchEnergie_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchEnergie_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_3_2.config(
            text=round(self.controller.get_page(StartPage).verbrauchMaterial_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchMaterial_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_3_3.config(
            text=round(self.controller.get_page(StartPage).kostenEffizienz_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenEffizienz_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_3_4.config(
            text=round(self.controller.get_page(StartPage).kostenAufwand_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenAufwand_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_4_1.config(
            text=round(self.controller.get_page(StartPage).zeitAufwand_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitAufwand_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_4_2.config(
            text=round(self.controller.get_page(StartPage).flexibilität_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flexibilität_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_4_3.config(
            text=round(self.controller.get_page(StartPage).zeitEffizienz_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitEffizienz_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_5_1.config(
            text=round(self.controller.get_page(StartPage).produktQualität_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).produktQualität_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_6_1.config(
            text=round(self.controller.get_page(StartPage).innovativität_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).innovativität_norm[0]))
        self.controller.get_page(MaschineWerte1).wert_6_2.config(
            text=round(self.controller.get_page(StartPage).flächenVerbrauch_norm[0].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flächenVerbrauch_norm[0]))

        self.controller.get_page(MaschineWerte2).wert_1_1.config(
            text=round(self.controller.get_page(StartPage).emissionen_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).emissionen_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_1_2.config(
            text=round(self.controller.get_page(StartPage).giftMaterial_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).giftMaterial_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_2_1.config(
            text=round(self.controller.get_page(StartPage).abfallProzentsatz_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallProzentsatz_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_2_2.config(
            text=round(self.controller.get_page(StartPage).abfallSzenarien_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallSzenarien_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_2_3.config(
            text=round(self.controller.get_page(StartPage).recyclingAbsolut_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingAbsolut_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_2_4.config(
            text=round(self.controller.get_page(StartPage).recyclingRelativ_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingRelativ_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_3_1.config(
            text=round(self.controller.get_page(StartPage).verbrauchEnergie_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchEnergie_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_3_2.config(
            text=round(self.controller.get_page(StartPage).verbrauchMaterial_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchMaterial_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_3_3.config(
            text=round(self.controller.get_page(StartPage).kostenEffizienz_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenEffizienz_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_3_4.config(
            text=round(self.controller.get_page(StartPage).kostenAufwand_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenAufwand_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_4_1.config(
            text=round(self.controller.get_page(StartPage).zeitAufwand_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitAufwand_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_4_2.config(
            text=round(self.controller.get_page(StartPage).flexibilität_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flexibilität_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_4_3.config(
            text=round(self.controller.get_page(StartPage).zeitEffizienz_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitEffizienz_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_5_1.config(
            text=round(self.controller.get_page(StartPage).produktQualität_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).produktQualität_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_6_1.config(
            text=round(self.controller.get_page(StartPage).innovativität_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).innovativität_norm[1]))
        self.controller.get_page(MaschineWerte2).wert_6_2.config(
            text=round(self.controller.get_page(StartPage).flächenVerbrauch_norm[1].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flächenVerbrauch_norm[1]))

        self.controller.get_page(MaschineWerte3).wert_1_1.config(
            text=round(self.controller.get_page(StartPage).emissionen_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).emissionen_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_1_2.config(
            text=round(self.controller.get_page(StartPage).giftMaterial_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).giftMaterial_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_2_1.config(
            text=round(self.controller.get_page(StartPage).abfallProzentsatz_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallProzentsatz_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_2_2.config(
            text=round(self.controller.get_page(StartPage).abfallSzenarien_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallSzenarien_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_2_3.config(
            text=round(self.controller.get_page(StartPage).recyclingAbsolut_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingAbsolut_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_2_4.config(
            text=round(self.controller.get_page(StartPage).recyclingRelativ_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingRelativ_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_3_1.config(
            text=round(self.controller.get_page(StartPage).verbrauchEnergie_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchEnergie_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_3_2.config(
            text=round(self.controller.get_page(StartPage).verbrauchMaterial_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchMaterial_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_3_3.config(
            text=round(self.controller.get_page(StartPage).kostenEffizienz_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenEffizienz_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_3_4.config(
            text=round(self.controller.get_page(StartPage).kostenAufwand_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenAufwand_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_4_1.config(
            text=round(self.controller.get_page(StartPage).zeitAufwand_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitAufwand_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_4_2.config(
            text=round(self.controller.get_page(StartPage).flexibilität_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flexibilität_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_4_3.config(
            text=round(self.controller.get_page(StartPage).zeitEffizienz_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitEffizienz_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_5_1.config(
            text=round(self.controller.get_page(StartPage).produktQualität_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).produktQualität_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_6_1.config(
            text=round(self.controller.get_page(StartPage).innovativität_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).innovativität_norm[2]))
        self.controller.get_page(MaschineWerte3).wert_6_2.config(
            text=round(self.controller.get_page(StartPage).flächenVerbrauch_norm[2].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flächenVerbrauch_norm[2]))

        self.controller.get_page(MaschineWerte4).wert_1_1.config(
            text=round(self.controller.get_page(StartPage).emissionen_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).emissionen_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_1_2.config(
            text=round(self.controller.get_page(StartPage).giftMaterial_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).giftMaterial_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_2_1.config(
            text=round(self.controller.get_page(StartPage).abfallProzentsatz_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallProzentsatz_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_2_2.config(
            text=round(self.controller.get_page(StartPage).abfallSzenarien_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).abfallSzenarien_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_2_3.config(
            text=round(self.controller.get_page(StartPage).recyclingAbsolut_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingAbsolut_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_2_4.config(
            text=round(self.controller.get_page(StartPage).recyclingRelativ_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).recyclingRelativ_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_3_1.config(
            text=round(self.controller.get_page(StartPage).verbrauchEnergie_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchEnergie_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_3_2.config(
            text=round(self.controller.get_page(StartPage).verbrauchMaterial_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).verbrauchMaterial_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_3_3.config(
            text=round(self.controller.get_page(StartPage).kostenEffizienz_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenEffizienz_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_3_4.config(
            text=round(self.controller.get_page(StartPage).kostenAufwand_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).kostenAufwand_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_4_1.config(
            text=round(self.controller.get_page(StartPage).zeitAufwand_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitAufwand_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_4_2.config(
            text=round(self.controller.get_page(StartPage).flexibilität_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flexibilität_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_4_3.config(
            text=round(self.controller.get_page(StartPage).zeitEffizienz_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).zeitEffizienz_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_5_1.config(
            text=round(self.controller.get_page(StartPage).produktQualität_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).produktQualität_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_6_1.config(
            text=round(self.controller.get_page(StartPage).innovativität_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).innovativität_norm[3]))
        self.controller.get_page(MaschineWerte4).wert_6_2.config(
            text=round(self.controller.get_page(StartPage).flächenVerbrauch_norm[3].get(), 5),
            bg=colourer(self.controller.get_page(StartPage).flächenVerbrauch_norm[3]))


    def werte_reset(self):
        """Resets all values"""
        # Maschine 0

        self.emissionen[0].set(398.47)
        self.giftMaterial[0].set(1)
        self.abfallProzentsatz[0].set(64)
        self.abfallSzenarien[0].set(1)
        self.recyclingAbsolut[0].set(1440)
        self.recyclingRelativ[0].set(51.2)
        self.verbrauchEnergie[0].set(993.7)
        self.verbrauchMaterial[0].set(1375)
        self.kostenEffizienz[0].set(0.91)
        self.kostenAufwand[0].set(40)
        self.zeitAufwand[0].set(3.5)
        self.flexibilität[0].set(5)
        self.zeitEffizienz[0].set(3)
        self.produktQualität[0].set(1)
        self.innovativität[0].set(4)
        self.flächenVerbrauch[0].set(25.5)

        # Maschine 1

        self.emissionen[1].set(501.41)
        self.giftMaterial[1].set(3)
        self.abfallProzentsatz[1].set(90)
        self.abfallSzenarien[1].set(1)
        self.recyclingAbsolut[1].set(1440)
        self.recyclingRelativ[1].set(53.5)
        self.verbrauchEnergie[1].set(1250.41)
        self.verbrauchMaterial[1].set(1250)
        self.kostenEffizienz[1].set(2.56)
        self.kostenAufwand[1].set(60)
        self.zeitAufwand[1].set(1)
        self.flexibilität[1].set(6)
        self.zeitEffizienz[1].set(7)
        self.produktQualität[1].set(3.5)
        self.innovativität[1].set(7)
        self.flächenVerbrauch[1].set(55.5)

        # Maschine 2

        self.emissionen[2].set(491.35)
        self.giftMaterial[2].set(3)
        self.abfallProzentsatz[2].set(48)
        self.abfallSzenarien[2].set(1)
        self.recyclingAbsolut[2].set(1440)
        self.recyclingRelativ[2].set(52.3)
        self.verbrauchEnergie[2].set(1225.3)
        self.verbrauchMaterial[2].set(1312)
        self.kostenEffizienz[2].set(1.37)
        self.kostenAufwand[2].set(60)
        self.zeitAufwand[2].set(1.5)
        self.flexibilität[2].set(5)
        self.zeitEffizienz[2].set(6)
        self.produktQualität[2].set(3.5)
        self.innovativität[2].set(6)
        self.flächenVerbrauch[2].set(36.5)

        # Maschine 3

        self.emissionen[3].set(300.75)
        self.giftMaterial[3].set(5)
        self.abfallProzentsatz[3].set(10)
        self.abfallSzenarien[3].set(1)
        self.recyclingAbsolut[3].set(1440)
        self.recyclingRelativ[3].set(51.8)
        self.verbrauchEnergie[3].set(750)
        self.verbrauchMaterial[3].set(1337)
        self.kostenEffizienz[3].set(0.28)
        self.kostenAufwand[3].set(40)
        self.zeitAufwand[3].set(2.5)
        self.flexibilität[3].set(7)
        self.zeitEffizienz[3].set(5)
        self.produktQualität[3].set(2)
        self.innovativität[3].set(5)
        self.flächenVerbrauch[3].set(28.5)


class PageOne(ttk.Frame):
    """Page for Social-Ecologic dimension"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.balloon = Pmw.Balloon(parent)

        regint = controller.register(correct)
        regfloat = controller.register(correctfloat)


        Buttons = ttk.Frame(self)
        button_2 = ttk.Button(Buttons, text="Nächste Seite", command=lambda: controller.acceptwerte(PageTwo, "Ökologische Indikatoren"))
        button_3 = ttk.Button(Buttons, text="Akzeptieren", command=lambda: controller.acceptwerte(PageOne, "Sozial-Ökologische Indikatoren"))
        button_4 = ttk.Button(Buttons, text="Auswerten", command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_5 = ttk.Button(Buttons, text="Abbrechen", command=lambda: controller.resetter())

        button_6 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial1, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)
        Buttons.columnconfigure(7, minsize=50)

        self.Sozial_Ökologisch_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökologisch_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökologisch_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökologisch_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)


        name_1 = ttk.Label(self.Sozial_Ökologisch_1, text="Flechtmaschine", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_2 = ttk.Label(self.Sozial_Ökologisch_2, text="Multifilamentwickelmaschine 90", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_3 = ttk.Label(self.Sozial_Ökologisch_3, text="Multifilamentwickelmaschine 48", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_4 = ttk.Label(self.Sozial_Ökologisch_4, text="Nasswickelmaschine", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))

        label_1_0 = ttk.Label(self.Sozial_Ökologisch_1, text="Sozial-Ökologische Auswertung --->", font = tkFont.Font(family = "helvetica", size=11, weight='bold'))
        label_1_1 = ttk.Label(self.Sozial_Ökologisch_1, text="Treibhausgasemissionen   (g/kg)", font = tkFont.Font(family = "helvetica", size=10))
        label_1_2 = ttk.Label(self.Sozial_Ökologisch_1, text="Kritikalität des Materials   (Skala: 1 = hoch / 5 = niedrig)", font = tkFont.Font(family = "helvetica", size=10))
        label_2_0 = ttk.Label(self.Sozial_Ökologisch_2, text="Sozial-Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_2_1 = ttk.Label(self.Sozial_Ökologisch_2, text="Treibhausgasemissionen   (g/kg)", font = tkFont.Font(family = "helvetica", size=10))
        label_2_2 = ttk.Label(self.Sozial_Ökologisch_2, text="Kritikalität des Materials   (Skala: 1 = hoch / 5 = niedrig)", font = tkFont.Font(family = "helvetica", size=10))
        label_3_0 = ttk.Label(self.Sozial_Ökologisch_3, text="Sozial-Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_3_1 = ttk.Label(self.Sozial_Ökologisch_3, text="Treibhausgasemissionen   (g/kg)", font = tkFont.Font(family = "helvetica", size=10))
        label_3_2 = ttk.Label(self.Sozial_Ökologisch_3, text="Kritikalität des Materials   (Skala: 1 = hoch / 5 = niedrig)", font = tkFont.Font(family = "helvetica", size=10))
        label_4_0 = ttk.Label(self.Sozial_Ökologisch_4, text="Sozial-Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_4_1 = ttk.Label(self.Sozial_Ökologisch_4, text="Treibhausgasemissionen   (g/kg)", font = tkFont.Font(family = "helvetica", size=10))
        label_4_2 = ttk.Label(self.Sozial_Ökologisch_4, text="Kritikalität des Materials   (Skala: 1 = hoch / 5 = niedrig)", font = tkFont.Font(family = "helvetica", size=10))

        self.entry_1_1 = ttk.Entry(self.Sozial_Ökologisch_1, textvariable = controller.get_page(StartPage).emissionen[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_2 = ttk.Entry(self.Sozial_Ökologisch_1, textvariable = controller.get_page(StartPage).giftMaterial[0], validate = "key", validatecommand =(regint, '%P'))
        self.entry_1 = ttk.Entry(self.Sozial_Ökologisch_2, textvariable = controller.get_page(StartPage).emissionen[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2 = ttk.Entry(self.Sozial_Ökologisch_2, textvariable = controller.get_page(StartPage).giftMaterial[1], validate = "key", validatecommand =(regint, '%P'))
        self.entry_3_1 = ttk.Entry(self.Sozial_Ökologisch_3, textvariable = controller.get_page(StartPage).emissionen[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_2 = ttk.Entry(self.Sozial_Ökologisch_3, textvariable = controller.get_page(StartPage).giftMaterial[2], validate = "key", validatecommand =(regint, '%P'))
        self.entry_4_1 = ttk.Entry(self.Sozial_Ökologisch_4, textvariable = controller.get_page(StartPage).emissionen[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_2 = ttk.Entry(self.Sozial_Ökologisch_4, textvariable = controller.get_page(StartPage).giftMaterial[3], validate = "key", validatecommand =(regint, '%P'))

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
        button_6.grid(row=0, column=8)


        name_1.grid(row=0, column=0)
        name_2.grid(row=0, column=0)
        name_3.grid(row=0, column=0)
        name_4.grid(row=0, column=0)

        label_1_0.grid(row=1, column=0)
        label_1_1.grid(row=2, column=0)
        label_1_2.grid(row=3, column=0)
        label_2_0.grid(row=1, column=0)
        label_2_1.grid(row=2, column=0)
        label_2_2.grid(row=3, column=0)
        label_3_0.grid(row=1, column=0)
        label_3_1.grid(row=2, column=0)
        label_3_2.grid(row=3, column=0)
        label_4_0.grid(row=1, column=0)
        label_4_1.grid(row=2, column=0)
        label_4_2.grid(row=3, column=0)

        self.entry_1_1.grid(row=2, column=1)
        self.entry_1_2.grid(row=3, column=1)
        self.entry_1.grid(row=2, column=1)
        self.entry_2.grid(row=3, column=1)
        self.entry_3_1.grid(row=2, column=1)
        self.entry_3_2.grid(row=3, column=1)
        self.entry_4_1.grid(row=2, column=1)
        self.entry_4_2.grid(row=3, column=1)

        self.auswertung_1.grid(row=1, column=1)
        self.auswertung_2.grid(row=1, column=1)
        self.auswertung_3.grid(row=1, column=1)
        self.auswertung_4.grid(row=1, column=1)


        columnconfig(self.Sozial_Ökologisch_1, self.Sozial_Ökologisch_2, self.Sozial_Ökologisch_3, self.Sozial_Ökologisch_4)

        self.Sozial_Ökologisch_1.grid(row=0, column=0)
        self.Sozial_Ökologisch_3.grid(row=0, column=1)
        self.Sozial_Ökologisch_2.grid(row=1, column=0)
        self.Sozial_Ökologisch_4.grid(row=1, column=1)
        Buttons.grid(row=2, column=1)

        self.balloon.bind(label_1_1, 'Die Menge an Treibhausgasen, die pro kg Abluft freigesetzt werden. \nBerechnung auf Basis vom Energieverbrauch und dem German Energy Mix (401g/kWh).')
        self.balloon.bind(label_1_2, 'Der Gesamtausmaß der negativen umweltbeeinflussenden Faktoren, die das ausgewählte Herstellungsverfahren mit sich bringt \n(z.B. Einsatz giftiger Materialien, Entflammbarkeit, karzinogene Effekte usw.).')
        self.balloon.bind(label_2_1, 'Die Menge an Treibhausgasen, die pro kg Abluft freigesetzt werden. \nBerechnung auf Basis vom Energieverbrauch und dem German Energy Mix (401g/kWh).')
        self.balloon.bind(label_2_2, 'Der Gesamtausmaß der negativen umweltbeeinflussenden Faktoren, die das ausgewählte Herstellungsverfahren mit sich bringt \n(z.B. Einsatz giftiger Materialien, Entflammbarkeit, karzinogene Effekte usw.).')
        self.balloon.bind(label_3_1, 'Die Menge an Treibhausgasen, die pro kg Abluft freigesetzt werden. \nBerechnung auf Basis vom Energieverbrauch und dem German Energy Mix (401g/kWh).')
        self.balloon.bind(label_3_2, 'Der Gesamtausmaß der negativen umweltbeeinflussenden Faktoren, die das ausgewählte Herstellungsverfahren mit sich bringt \n(z.B. Einsatz giftiger Materialien, Entflammbarkeit, karzinogene Effekte usw.).')
        self.balloon.bind(label_4_1, 'Die Menge an Treibhausgasen, die pro kg Abluft freigesetzt werden. \nBerechnung auf Basis vom Energieverbrauch und dem German Energy Mix (401g/kWh).')
        self.balloon.bind(label_4_2, 'Der Gesamtausmaß der negativen umweltbeeinflussenden Faktoren, die das ausgewählte Herstellungsverfahren mit sich bringt \n(z.B. Einsatz giftiger Materialien, Entflammbarkeit, karzinogene Effekte usw.).')


class PageTwo(ttk.Frame):
    """Page for Ecologic dimension"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.balloon = Pmw.Balloon(parent)


        regint = controller.register(correct)
        regfloat = controller.register(correctfloat)

        Buttons = ttk.Frame(self)
        button_1 = ttk.Button(Buttons, text="Zurück",
                          command=lambda: controller.acceptwerte(PageOne, "Sozial-Ökologische Indikatoren"))
        button_2 = ttk.Button(Buttons, text="Nächste Seite",
                          command=lambda: controller.acceptwerte(PageThree, "Ökologisch-Ökonomische Indikatoren"))
        button_3 = ttk.Button(Buttons, text="Akzeptieren", command=lambda: controller.acceptwerte(PageTwo, "Ökologische Indikatoren"))
        button_4 = ttk.Button(Buttons, text="Auswerten", command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_5 = ttk.Button(Buttons, text="Abbrechen", command=lambda: controller.resetter())
        button_6 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial2, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)
        Buttons.columnconfigure(7, minsize=50)


        self.Ökologisch_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökologisch_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökologisch_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökologisch_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)

        name_1 = ttk.Label(self.Ökologisch_1, text="Flechtmaschine", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_2 = ttk.Label(self.Ökologisch_2, text="Multifilamentwickelmaschine 90", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_3 = ttk.Label(self.Ökologisch_3, text="Multifilamentwickelmaschine 48", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_4 = ttk.Label(self.Ökologisch_4, text="Nasswickelmaschine", relief = 'ridge', font = tkFont.Font(family = "helvetica", size=14, weight='bold'))

        label_1_0 = ttk.Label(self.Ökologisch_1, text="Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_1_1 = ttk.Label(self.Ökologisch_1, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_2 = ttk.Label(self.Ökologisch_1, text="Abfallszenarien    (Skala:     nur 1 akzeptiert)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_3 = ttk.Label(self.Ökologisch_1, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_4 = ttk.Label(self.Ökologisch_1, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_0 = ttk.Label(self.Ökologisch_2, text="Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_2_1 = ttk.Label(self.Ökologisch_2, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_2 = ttk.Label(self.Ökologisch_2, text="Abfallszenarien    (Skala:     nur 1 akzeptiert)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_3 = ttk.Label(self.Ökologisch_2, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_4 = ttk.Label(self.Ökologisch_2, text="Anteil verwendetes Recyclingmaterial (Relativ   (%)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_0 = ttk.Label(self.Ökologisch_3, text="Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_3_1 = ttk.Label(self.Ökologisch_3, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_2 = ttk.Label(self.Ökologisch_3, text="Abfallszenarien    (Skala:     nur 1 akzeptiert)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_3 = ttk.Label(self.Ökologisch_3, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_4 = ttk.Label(self.Ökologisch_3, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_0 = ttk.Label(self.Ökologisch_4, text="Ökologische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_4_1 = ttk.Label(self.Ökologisch_4, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_2 = ttk.Label(self.Ökologisch_4, text="Abfallszenarien    (Skala:     nur 1 akzeptiert)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_3 = ttk.Label(self.Ökologisch_4, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_4 = ttk.Label(self.Ökologisch_4, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))

        self.entry_1_1 = ttk.Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).abfallProzentsatz[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_2 = ttk.Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).abfallSzenarien[0], validate = "key", validatecommand =(regint, '%P'))
        self.entry_1_3 = ttk.Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).recyclingAbsolut[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_4 = ttk.Entry(self.Ökologisch_1, textvariable = controller.get_page(StartPage).recyclingRelativ[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_1 = ttk.Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).abfallProzentsatz[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_2 = ttk.Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).abfallSzenarien[1], validate = "key", validatecommand =(regint, '%P'))
        self.entry_2_3 = ttk.Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).recyclingAbsolut[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_4 = ttk.Entry(self.Ökologisch_2, textvariable = controller.get_page(StartPage).recyclingRelativ[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_1 = ttk.Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).abfallProzentsatz[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_2 = ttk.Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).abfallSzenarien[2], validate = "key", validatecommand =(regint, '%P'))
        self.entry_3_3 = ttk.Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).recyclingAbsolut[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_4 = ttk.Entry(self.Ökologisch_3, textvariable = controller.get_page(StartPage).recyclingRelativ[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_1 = ttk.Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).abfallProzentsatz[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_2 = ttk.Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).abfallSzenarien[3], validate = "key", validatecommand =(regint, '%P'))
        self.entry_4_3 = ttk.Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).recyclingAbsolut[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_4 = ttk.Entry(self.Ökologisch_4, textvariable = controller.get_page(StartPage).recyclingRelativ[3], validate = "key", validatecommand =(regfloat, '%P'))

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
        button_6.grid(row=0, column=8)

        name_1.grid(row=0, column=0)
        name_2.grid(row=0, column=0)
        name_3.grid(row=0, column=0)
        name_4.grid(row=0, column=0)

        label_1_0.grid(row=1, column=0)
        label_1_1.grid(row=2, column=0)
        label_1_2.grid(row=3, column=0)
        label_1_3.grid(row=4, column=0)
        label_1_4.grid(row=5, column=0)
        label_2_0.grid(row=1, column=0)
        label_2_1.grid(row=2, column=0)
        label_2_2.grid(row=3, column=0)
        label_2_3.grid(row=4, column=0)
        label_2_4.grid(row=5, column=0)
        label_3_0.grid(row=1, column=0)
        label_3_1.grid(row=2, column=0)
        label_3_2.grid(row=3, column=0)
        label_3_3.grid(row=4, column=0)
        label_3_4.grid(row=5, column=0)
        label_4_0.grid(row=1, column=0)
        label_4_1.grid(row=2, column=0)
        label_4_2.grid(row=3, column=0)
        label_4_3.grid(row=4, column=0)
        label_4_4.grid(row=5, column=0)

        self.entry_1_1.grid(row=2, column=1)
        self.entry_1_2.grid(row=3, column=1)
        self.entry_1_3.grid(row=4, column=1)
        self.entry_1_4.grid(row=5, column=1)
        self.entry_2_1.grid(row=2, column=1)
        self.entry_2_2.grid(row=3, column=1)
        self.entry_2_3.grid(row=4, column=1)
        self.entry_2_4.grid(row=5, column=1)
        self.entry_3_1.grid(row=2, column=1)
        self.entry_3_2.grid(row=3, column=1)
        self.entry_3_3.grid(row=4, column=1)
        self.entry_3_4.grid(row=5, column=1)
        self.entry_4_1.grid(row=2, column=1)
        self.entry_4_2.grid(row=3, column=1)
        self.entry_4_3.grid(row=4, column=1)
        self.entry_4_4.grid(row=5, column=1)

        self.auswertung_1.grid(row=1, column=1)
        self.auswertung_2.grid(row=1, column=1)
        self.auswertung_3.grid(row=1, column=1)
        self.auswertung_4.grid(row=1, column=1)

        columnconfig(self.Ökologisch_1, self.Ökologisch_2, self.Ökologisch_3, self.Ökologisch_4)

        self.Ökologisch_1.grid(row=0, column=0)
        self.Ökologisch_3.grid(row=0, column=1)
        self.Ökologisch_2.grid(row=1, column=0)
        self.Ökologisch_4.grid(row=1, column=1)
        Buttons.grid(row=2, column=1)

        self.balloon.bind(label_1_1, 'Die Länge des Abfallmaterials (in m), die bei der Herstellung \neines Tanks entsteht bzw. verloren geht.')
        self.balloon.bind(label_1_2, 'Indikatorbeschreibung hier.')
        self.balloon.bind(label_1_3, 'Die Menge des recycelten Materials, die für die Herstellung \neines Tanks verwendet wird.')
        self.balloon.bind(label_1_4, 'Der Anteil an recyceltem Material in einem fertigen Tank \n(relativ zur Gesamtmenge).')
        self.balloon.bind(label_2_1, 'Die Länge des Abfallmaterials (in m), die bei der Herstellung \neines Tanks entsteht bzw. verloren geht.')
        self.balloon.bind(label_2_2, 'Indikatorbeschreibung hier.')
        self.balloon.bind(label_2_3, 'Die Menge des recycelten Materials, die für die Herstellung \neines Tanks verwendet wird.')
        self.balloon.bind(label_2_4, 'Der Anteil an recyceltem Material in einem fertigen Tank \n(relativ zur Gesamtmenge).')
        self.balloon.bind(label_3_1, 'Die Länge des Abfallmaterials (in m), die bei der Herstellung \neines Tanks entsteht bzw. verloren geht.')
        self.balloon.bind(label_3_2, 'Indikatorbeschreibung hier.')
        self.balloon.bind(label_3_3, 'Die Menge des recycelten Materials, die für die Herstellung \neines Tanks verwendet wird.')
        self.balloon.bind(label_3_4, 'Der Anteil an recyceltem Material in einem fertigen Tank \n(relativ zur Gesamtmenge).')
        self.balloon.bind(label_4_1, 'Die Länge des Abfallmaterials (in m), die bei der Herstellung \neines Tanks entsteht bzw. verloren geht.')
        self.balloon.bind(label_4_2, 'Indikatorbeschreibung hier.')
        self.balloon.bind(label_4_3, 'Die Menge des recycelten Materials, die für die Herstellung \neines Tanks verwendet wird.')
        self.balloon.bind(label_4_4, 'Der Anteil an recyceltem Material in einem fertigen Tank \n(relativ zur Gesamtmenge).')


class PageThree(ttk.Frame):
    """Page for Ecologic-Economic dimension"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.balloon = Pmw.Balloon(parent)


        regint = controller.register(correct)
        regfloat = controller.register(correctfloat)

        Buttons = ttk.Frame(self)
        button_1 = ttk.Button(Buttons, text="Zurück",
                          command=lambda: controller.acceptwerte(PageTwo, "Ökologische Indikatoren"))
        button_2 = ttk.Button(Buttons, text="Nächste Seite",
                          command=lambda: controller.acceptwerte(PageFour, "Ökonomische Indikatoren"))
        button_3 = ttk.Button(Buttons, text="Akzeptieren", command=lambda: controller.acceptwerte(PageThree, "Ökologisch-Ökonomische Indikatoren"))
        button_4 = ttk.Button(Buttons, text="Auswerten", command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_5 = ttk.Button(Buttons, text="Abbrechen", command=lambda: controller.resetter())
        button_6 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial3, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)
        Buttons.columnconfigure(7, minsize=50)


        self.Ökologisch_Ökonomisch_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökologisch_Ökonomisch_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökologisch_Ökonomisch_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökologisch_Ökonomisch_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)

        name_1_1 = ttk.Label(self.Ökologisch_Ökonomisch_1, text="Flechtmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_2 = ttk.Label(self.Ökologisch_Ökonomisch_2, text="Multifilamentwickelmaschine 90", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_3 = ttk.Label(self.Ökologisch_Ökonomisch_3, text="Multifilamentwickelmaschine 48", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_4 = ttk.Label(self.Ökologisch_Ökonomisch_4, text="Nasswickelmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))

        label_1_0 = ttk.Label(self.Ökologisch_Ökonomisch_1, text="Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_1_1 = ttk.Label(self.Ökologisch_Ökonomisch_1, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_2 = ttk.Label(self.Ökologisch_Ökonomisch_1, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_3 = ttk.Label(self.Ökologisch_Ökonomisch_1, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_4 = ttk.Label(self.Ökologisch_Ökonomisch_1, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_0 = ttk.Label(self.Ökologisch_Ökonomisch_2, text="Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_2_1 = ttk.Label(self.Ökologisch_Ökonomisch_2, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_2 = ttk.Label(self.Ökologisch_Ökonomisch_2, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_3 = ttk.Label(self.Ökologisch_Ökonomisch_2, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_4 = ttk.Label(self.Ökologisch_Ökonomisch_2, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_0 = ttk.Label(self.Ökologisch_Ökonomisch_3, text="Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_3_1 = ttk.Label(self.Ökologisch_Ökonomisch_3, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_2 = ttk.Label(self.Ökologisch_Ökonomisch_3, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_3 = ttk.Label(self.Ökologisch_Ökonomisch_3, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_4 = ttk.Label(self.Ökologisch_Ökonomisch_3, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_0 = ttk.Label(self.Ökologisch_Ökonomisch_4, text="Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_4_1 = ttk.Label(self.Ökologisch_Ökonomisch_4, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_2 = ttk.Label(self.Ökologisch_Ökonomisch_4, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_3 = ttk.Label(self.Ökologisch_Ökonomisch_4, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_4 = ttk.Label(self.Ökologisch_Ökonomisch_4, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))

        self.entry_1_1 = ttk.Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).verbrauchEnergie[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_2 = ttk.Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).verbrauchMaterial[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_3 = ttk.Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).kostenEffizienz[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_4 = ttk.Entry(self.Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).kostenAufwand[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_1 = ttk.Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).verbrauchEnergie[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_2 = ttk.Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).verbrauchMaterial[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_3 = ttk.Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).kostenEffizienz[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_4 = ttk.Entry(self.Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).kostenAufwand[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_1 = ttk.Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).verbrauchEnergie[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_2 = ttk.Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).verbrauchMaterial[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_3 = ttk.Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).kostenEffizienz[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_4 = ttk.Entry(self.Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).kostenAufwand[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_1 = ttk.Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).verbrauchEnergie[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_2 = ttk.Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).verbrauchMaterial[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_3 = ttk.Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).kostenEffizienz[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_4 = ttk.Entry(self.Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).kostenAufwand[3], validate = "key", validatecommand =(regfloat, '%P'))

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
        button_6.grid(row=0, column=8)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_0.grid(row=1, column=0)
        label_1_1.grid(row=2, column=0)
        label_1_2.grid(row=3, column=0)
        label_1_3.grid(row=4, column=0)
        label_1_4.grid(row=5, column=0)
        label_2_0.grid(row=1, column=0)
        label_2_1.grid(row=2, column=0)
        label_2_2.grid(row=3, column=0)
        label_2_3.grid(row=4, column=0)
        label_2_4.grid(row=5, column=0)
        label_3_0.grid(row=1, column=0)
        label_3_1.grid(row=2, column=0)
        label_3_2.grid(row=3, column=0)
        label_3_3.grid(row=4, column=0)
        label_3_4.grid(row=5, column=0)
        label_4_0.grid(row=1, column=0)
        label_4_1.grid(row=2, column=0)
        label_4_2.grid(row=3, column=0)
        label_4_3.grid(row=4, column=0)
        label_4_4.grid(row=5, column=0)

        self.entry_1_1.grid(row=2, column=1)
        self.entry_1_2.grid(row=3, column=1)
        self.entry_1_3.grid(row=4, column=1)
        self.entry_1_4.grid(row=5, column=1)
        self.entry_2_1.grid(row=2, column=1)
        self.entry_2_2.grid(row=3, column=1)
        self.entry_2_3.grid(row=4, column=1)
        self.entry_2_4.grid(row=5, column=1)
        self.entry_3_1.grid(row=2, column=1)
        self.entry_3_2.grid(row=3, column=1)
        self.entry_3_3.grid(row=4, column=1)
        self.entry_3_4.grid(row=5, column=1)
        self.entry_4_1.grid(row=2, column=1)
        self.entry_4_2.grid(row=3, column=1)
        self.entry_4_3.grid(row=4, column=1)
        self.entry_4_4.grid(row=5, column=1)

        self.auswertung_1.grid(row=1, column=1)
        self.auswertung_2.grid(row=1, column=1)
        self.auswertung_3.grid(row=1, column=1)
        self.auswertung_4.grid(row=1, column=1)

        columnconfig(self.Ökologisch_Ökonomisch_1, self.Ökologisch_Ökonomisch_2, self.Ökologisch_Ökonomisch_3, self.Ökologisch_Ökonomisch_4)

        self.Ökologisch_Ökonomisch_1.grid(row=0, column=0)
        self.Ökologisch_Ökonomisch_3.grid(row=0, column=1)
        self.Ökologisch_Ökonomisch_2.grid(row=1, column=0)
        self.Ökologisch_Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=2, column=1)

        self.balloon.bind(label_1_1, 'Die Menge elektrischer Energie, die bei der Herstellung pro kg \nFasermaterial verbraucht wird.')
        self.balloon.bind(label_1_2, 'Die Gesamtmenge an Material (in g), die für die Herstellung \neines Tanks benötigt wird.')
        self.balloon.bind(label_1_3, 'Die geschätzten Kosten des Herstellungsverfahrens pro Sekunde \n(während die Maschine in Betrieb ist).')
        self.balloon.bind(label_1_4, 'Die geschätzten Kosten der für die Herstellung benötigten Materialien pro kg.')
        self.balloon.bind(label_2_1, 'Die Menge elektrischer Energie, die bei der Herstellung pro kg \nFasermaterial verbraucht wird.')
        self.balloon.bind(label_2_2, 'Die Gesamtmenge an Material (in g), die für die Herstellung \neines Tanks benötigt wird.')
        self.balloon.bind(label_2_3, 'Die geschätzten Kosten des Herstellungsverfahrens pro Sekunde \n(während die Maschine in Betrieb ist).')
        self.balloon.bind(label_2_4, 'Die geschätzten Kosten der für die Herstellung benötigten Materialien pro kg.')
        self.balloon.bind(label_3_1, 'Die Menge elektrischer Energie, die bei der Herstellung pro kg \nFasermaterial verbraucht wird.')
        self.balloon.bind(label_3_2, 'Die Gesamtmenge an Material (in g), die für die Herstellung \neines Tanks benötigt wird.')
        self.balloon.bind(label_3_3, 'Die geschätzten Kosten des Herstellungsverfahrens pro Sekunde \n(während die Maschine in Betrieb ist).')
        self.balloon.bind(label_3_4, 'Die geschätzten Kosten der für die Herstellung benötigten Materialien pro kg.')
        self.balloon.bind(label_4_1, 'Die Menge elektrischer Energie, die bei der Herstellung pro kg \nFasermaterial verbraucht wird.')
        self.balloon.bind(label_4_2, 'Die Gesamtmenge an Material (in g), die für die Herstellung \neines Tanks benötigt wird.')
        self.balloon.bind(label_4_3, 'Die geschätzten Kosten des Herstellungsverfahrens pro Sekunde \n(während die Maschine in Betrieb ist).')
        self.balloon.bind(label_4_4, 'Die geschätzten Kosten der für die Herstellung benötigten Materialien pro kg.')


class PageFour(ttk.Frame):
    """Page for Economic dimension"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.balloon = Pmw.Balloon(parent)


        regint = controller.register(correct)
        regfloat = controller.register(correctfloat)

        Buttons = ttk.Frame(self)
        button_1 = ttk.Button(Buttons, text="Zurück",
                          command=lambda: controller.acceptwerte(PageThree, "Ökologisch-Ökonomische Indikatoren"))
        button_2 = ttk.Button(Buttons, text="Nächste Seite",
                          command=lambda: controller.acceptwerte(PageFive, "Sozial-Ökonomische Indikatoren"))
        button_3 = ttk.Button(Buttons, text="Akzeptieren", command=lambda: controller.acceptwerte(PageFour, "Ökonomische Indikatoren"))
        button_4 = ttk.Button(Buttons, text="Auswerten", command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_5 = ttk.Button(Buttons, text="Abbrechen", command=lambda: controller.resetter())
        button_6 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial4, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)
        Buttons.columnconfigure(7, minsize=50)


        self.Ökonomisch_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökonomisch_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökonomisch_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Ökonomisch_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)

        name_1_1 = ttk.Label(self.Ökonomisch_1, text="Flechtmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_2 = ttk.Label(self.Ökonomisch_2, text="Multifilamentwickelmaschine 90", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_3 = ttk.Label(self.Ökonomisch_3, text="Multifilamentwickelmaschine 48", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_4 = ttk.Label(self.Ökonomisch_4, text="Nasswickelmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))

        label_1_0 = ttk.Label(self.Ökonomisch_1, text="Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_1_1 = ttk.Label(self.Ökonomisch_1, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_2 = ttk.Label(self.Ökonomisch_1, text="Flexibilität   (Skala:     5 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_3 = ttk.Label(self.Ökonomisch_1, text="Zeitliche Effizienz   (Skala:     3 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_0 = ttk.Label(self.Ökonomisch_2, text="Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_2_1 = ttk.Label(self.Ökonomisch_2, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_2 = ttk.Label(self.Ökonomisch_2, text="Flexibilität   (Skala:     5 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_3 = ttk.Label(self.Ökonomisch_2, text="Zeitliche Effizienz   (Skala:     3 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_0 = ttk.Label(self.Ökonomisch_3, text="Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_3_1 = ttk.Label(self.Ökonomisch_3, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_2 = ttk.Label(self.Ökonomisch_3, text="Flexibilität   (Skala:     5 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_3 = ttk.Label(self.Ökonomisch_3, text="Zeitliche Effizienz   (Skala:     3 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_0 = ttk.Label(self.Ökonomisch_4, text="Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_4_1 = ttk.Label(self.Ökonomisch_4, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_2 = ttk.Label(self.Ökonomisch_4, text="Flexibilität   (Skala:     5 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_3 = ttk.Label(self.Ökonomisch_4, text="Zeitliche Effizienz   (Skala:     3 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))

        self.entry_1_1 = ttk.Entry(self.Ökonomisch_1, textvariable = controller.get_page(StartPage).zeitAufwand[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_2 = ttk.Entry(self.Ökonomisch_1, textvariable = controller.get_page(StartPage).flexibilität[0], validate = "key", validatecommand =(regint, '%P'))
        self.entry_1_3 = ttk.Entry(self.Ökonomisch_1, textvariable = controller.get_page(StartPage).zeitEffizienz[0], validate = "key", validatecommand =(regint, '%P'))
        self.entry_2_1 = ttk.Entry(self.Ökonomisch_2, textvariable = controller.get_page(StartPage).zeitAufwand[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_2 = ttk.Entry(self.Ökonomisch_2, textvariable = controller.get_page(StartPage).flexibilität[1], validate = "key", validatecommand =(regint, '%P'))
        self.entry_2_3 = ttk.Entry(self.Ökonomisch_2, textvariable = controller.get_page(StartPage).zeitEffizienz[1], validate = "key", validatecommand =(regint, '%P'))
        self.entry_3_1 = ttk.Entry(self.Ökonomisch_3, textvariable = controller.get_page(StartPage).zeitAufwand[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_2 = ttk.Entry(self.Ökonomisch_3, textvariable = controller.get_page(StartPage).flexibilität[2], validate = "key", validatecommand =(regint, '%P'))
        self.entry_3_3 = ttk.Entry(self.Ökonomisch_3, textvariable = controller.get_page(StartPage).zeitEffizienz[2], validate = "key", validatecommand =(regint, '%P'))
        self.entry_4_1 = ttk.Entry(self.Ökonomisch_4, textvariable = controller.get_page(StartPage).zeitAufwand[3], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_2 = ttk.Entry(self.Ökonomisch_4, textvariable = controller.get_page(StartPage).flexibilität[3], validate = "key", validatecommand =(regint, '%P'))
        self.entry_4_3 = ttk.Entry(self.Ökonomisch_4, textvariable = controller.get_page(StartPage).zeitEffizienz[3], validate = "key", validatecommand =(regint, '%P'))

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
        button_6.grid(row=0, column=8)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_0.grid(row=1, column=0)
        label_1_1.grid(row=2, column=0)
        label_1_2.grid(row=3, column=0)
        label_1_3.grid(row=4, column=0)
        label_2_0.grid(row=1, column=0)
        label_2_1.grid(row=2, column=0)
        label_2_2.grid(row=3, column=0)
        label_2_3.grid(row=4, column=0)
        label_3_0.grid(row=1, column=0)
        label_3_1.grid(row=2, column=0)
        label_3_2.grid(row=3, column=0)
        label_3_3.grid(row=4, column=0)
        label_4_0.grid(row=1, column=0)
        label_4_1.grid(row=2, column=0)
        label_4_2.grid(row=3, column=0)
        label_4_3.grid(row=4, column=0)

        self.entry_1_1.grid(row=2, column=1)
        self.entry_1_2.grid(row=3, column=1)
        self.entry_1_3.grid(row=4, column=1)
        self.entry_2_1.grid(row=2, column=1)
        self.entry_2_2.grid(row=3, column=1)
        self.entry_2_3.grid(row=4, column=1)
        self.entry_3_1.grid(row=2, column=1)
        self.entry_3_2.grid(row=3, column=1)
        self.entry_3_3.grid(row=4, column=1)
        self.entry_4_1.grid(row=2, column=1)
        self.entry_4_2.grid(row=3, column=1)
        self.entry_4_3.grid(row=4, column=1)

        self.auswertung_1.grid(row=1, column=1)
        self.auswertung_2.grid(row=1, column=1)
        self.auswertung_3.grid(row=1, column=1)
        self.auswertung_4.grid(row=1, column=1)

        columnconfig(self.Ökonomisch_1, self.Ökonomisch_2, self.Ökonomisch_3, self.Ökonomisch_4)

        self.Ökonomisch_1.grid(row=0, column=0)
        self.Ökonomisch_3.grid(row=0, column=1)
        self.Ökonomisch_2.grid(row=1, column=0)
        self.Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=2, column=1)

        self.balloon.bind(label_1_1, 'Die Zeit, die für die Herstellung eines Tanks mit dem jew. \nHerstellungsverfahren benötigt wird.')
        self.balloon.bind(label_1_2, 'Das Ausmaß an zusätzlichen Konfigurationsmöglichkeiten des Herstellungsverfahrens \n(z.B. größere Maschinen können größere Tanks wickeln, ...).')
        self.balloon.bind(label_1_3, 'Die zeitliche Effizienz des jew. Herstellungsverfahrens, \nbasierend auf Erfahrungsberichten.')
        self.balloon.bind(label_2_1, 'Die Zeit, die für die Herstellung eines Tanks mit dem jew. \nHerstellungsverfahren benötigt wird.')
        self.balloon.bind(label_2_2, 'Das Ausmaß an zusätzlichen Konfigurationsmöglichkeiten des Herstellungsverfahrens \n(z.B. größere Maschinen können größere Tanks wickeln, ...).')
        self.balloon.bind(label_2_3, 'Die zeitliche Effizienz des jew. Herstellungsverfahrens, \nbasierend auf Erfahrungsberichten.')
        self.balloon.bind(label_3_1, 'Die Zeit, die für die Herstellung eines Tanks mit dem jew. \nHerstellungsverfahren benötigt wird.')
        self.balloon.bind(label_3_2, 'Das Ausmaß an zusätzlichen Konfigurationsmöglichkeiten des Herstellungsverfahrens \n(z.B. größere Maschinen können größere Tanks wickeln, ...).')
        self.balloon.bind(label_3_3, 'Die zeitliche Effizienz des jew. Herstellungsverfahrens, \nbasierend auf Erfahrungsberichten.')
        self.balloon.bind(label_4_1, 'Die Zeit, die für die Herstellung eines Tanks mit dem jew. \nHerstellungsverfahren benötigt wird.')
        self.balloon.bind(label_4_2, 'Das Ausmaß an zusätzlichen Konfigurationsmöglichkeiten des Herstellungsverfahrens \n(z.B. größere Maschinen können größere Tanks wickeln, ...).')
        self.balloon.bind(label_4_3, 'Die zeitliche Effizienz des jew. Herstellungsverfahrens, \nbasierend auf Erfahrungsberichten.')


class PageFive(ttk.Frame):
    """Page for Social-Economic dimension"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.balloon = Pmw.Balloon(parent)


        regint = controller.register(correct)
        regfloat = controller.register(correctfloat)

        Buttons = ttk.Frame(self)
        button_1 = ttk.Button(Buttons, text="Zurück",
                          command=lambda: controller.acceptwerte(PageFour, "Ökonomische Indikatoren"))
        button_2 = ttk.Button(Buttons, text="Nächste Seite",
                          command=lambda: controller.acceptwerte(PageSix, "Sozial-Ökonomisch-Ökologische Indikatoren"))
        button_3 = ttk.Button(Buttons, text="Akzeptieren", command=lambda: controller.acceptwerte(PageFive, "Sozial-Ökonomische Indikatoren"))
        button_4 = ttk.Button(Buttons, text="Auswerten", command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_5 = ttk.Button(Buttons, text="Abbrechen", command=lambda: controller.resetter())
        button_6 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial5, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)
        Buttons.columnconfigure(7, minsize=50)


        self.Sozial_Ökonomisch_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökonomisch_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökonomisch_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökonomisch_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)

        name_1_1 = ttk.Label(self.Sozial_Ökonomisch_1, text="Flechtmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_2 = ttk.Label(self.Sozial_Ökonomisch_2, text="Multifilamentwickelmaschine 90", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_3 = ttk.Label(self.Sozial_Ökonomisch_3, text="Multifilamentwickelmaschine 48", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_4 = ttk.Label(self.Sozial_Ökonomisch_4, text="Nasswickelmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))

        label_1_0 = ttk.Label(self.Sozial_Ökonomisch_1, text="Sozial-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_1_1 = ttk.Label(self.Sozial_Ökonomisch_1, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_0 = ttk.Label(self.Sozial_Ökonomisch_2, text="Sozial-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_2_1 = ttk.Label(self.Sozial_Ökonomisch_2, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_0 = ttk.Label(self.Sozial_Ökonomisch_3, text="Sozial-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_3_1 = ttk.Label(self.Sozial_Ökonomisch_3, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_0 = ttk.Label(self.Sozial_Ökonomisch_4, text="Sozial-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_4_1 = ttk.Label(self.Sozial_Ökonomisch_4, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))

        self.entry_1_1 = ttk.Entry(self.Sozial_Ökonomisch_1, textvariable = controller.get_page(StartPage).produktQualität[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_2 = ttk.Entry(self.Sozial_Ökonomisch_2, textvariable = controller.get_page(StartPage).produktQualität[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_3 = ttk.Entry(self.Sozial_Ökonomisch_3, textvariable = controller.get_page(StartPage).produktQualität[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_1_4 = ttk.Entry(self.Sozial_Ökonomisch_4, textvariable = controller.get_page(StartPage).produktQualität[3], validate = "key", validatecommand =(regfloat, '%P'))

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
        button_6.grid(row=0, column=8)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_0.grid(row=1, column=0)
        label_1_1.grid(row=2, column=0)
        label_2_0.grid(row=1, column=0)
        label_2_1.grid(row=2, column=0)
        label_3_0.grid(row=1, column=0)
        label_3_1.grid(row=2, column=0)
        label_4_0.grid(row=1, column=0)
        label_4_1.grid(row=2, column=0)

        self.entry_1_1.grid(row=2, column=1)
        self.entry_1_2.grid(row=2, column=1)
        self.entry_1_3.grid(row=2, column=1)
        self.entry_1_4.grid(row=2, column=1)

        self.auswertung_1.grid(row=1, column=1)
        self.auswertung_2.grid(row=1, column=1)
        self.auswertung_3.grid(row=1, column=1)
        self.auswertung_4.grid(row=1, column=1)

        columnconfig(self.Sozial_Ökonomisch_1, self.Sozial_Ökonomisch_2, self.Sozial_Ökonomisch_3, self.Sozial_Ökonomisch_4)

        self.Sozial_Ökonomisch_1.grid(row=0, column=0)
        self.Sozial_Ökonomisch_3.grid(row=0, column=1)
        self.Sozial_Ökonomisch_2.grid(row=1, column=0)
        self.Sozial_Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=2, column=1)

        self.balloon.bind(label_1_1, 'Der relative Porengehalt des Materials in einem fertigen Tank.')
        self.balloon.bind(label_2_1, 'Der relative Porengehalt des Materials in einem fertigen Tank.')
        self.balloon.bind(label_3_1, 'Der relative Porengehalt des Materials in einem fertigen Tank.')
        self.balloon.bind(label_4_1, 'Der relative Porengehalt des Materials in einem fertigen Tank.')


class PageSix(ttk.Frame):
    """Page for Sozial-Ecologic-Economic dimension"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.balloon = Pmw.Balloon(parent)


        regint = controller.register(correct)
        regfloat = controller.register(correctfloat)

        Buttons = ttk.Frame(self)
        button_1 = ttk.Button(Buttons, text="Zurück",
                          command=lambda: controller.acceptwerte(PageFive, "Sozial-Ökonomische Indikatoren"))
        button_3 = ttk.Button(Buttons, text="Akzeptieren", command=lambda: controller.acceptwerte(PageSix, "Sozial-Ökonomisch-Ökologische Indikatoren"))
        button_4 = ttk.Button(Buttons, text="Auswerten", command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_5 = ttk.Button(Buttons, text="Abbrechen", command=lambda: controller.resetter())
        button_6 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial6, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=30)
        Buttons.columnconfigure(7, minsize=50)


        self.Sozial_Ökologisch_Ökonomisch_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökologisch_Ökonomisch_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökologisch_Ökonomisch_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.Sozial_Ökologisch_Ökonomisch_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)

        name_1_1 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Flechtmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_2 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Multifilamentwickelmaschine 90", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_3 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Multifilamentwickelmaschine 48", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))
        name_1_4 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Nasswickelmaschine", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=14, weight='bold'))

        label_1_0 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Sozial-Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_1_1 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Innovativität   (Skala:     4 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_1_2 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_1, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_0 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Sozial-Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_2_1 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Innovativität   (Skala:     4 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_2_2 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_2, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_0 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Sozial-Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_3_1 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Innovativität   (Skala:     4 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_3_2 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_3, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_0 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Sozial-Ökologisch-Ökonomische Auswertung --->",
                              font=tkFont.Font(family="helvetica", size=11, weight='bold'))
        label_4_1 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Innovativität   (Skala:     4 = niedrig / 7 = hoch)" , font = tkFont.Font(family = "helvetica", size=10))
        label_4_2 = ttk.Label(self.Sozial_Ökologisch_Ökonomisch_4, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))

        self.entry_1_1 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).innovativität[0], validate = "key", validatecommand =(regint, '%P'))
        self.entry_1_2 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_1, textvariable = controller.get_page(StartPage).flächenVerbrauch[0], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_2_1 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).innovativität[1], validate = "key", validatecommand =(regint, '%P'))
        self.entry_2_2 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_2, textvariable = controller.get_page(StartPage).flächenVerbrauch[1], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_3_1 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).innovativität[2], validate = "key", validatecommand =(regint, '%P'))
        self.entry_3_2 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_3, textvariable = controller.get_page(StartPage).flächenVerbrauch[2], validate = "key", validatecommand =(regfloat, '%P'))
        self.entry_4_1 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).innovativität[3], validate = "key", validatecommand =(regint, '%P'))
        self.entry_4_2 = ttk.Entry(self.Sozial_Ökologisch_Ökonomisch_4, textvariable = controller.get_page(StartPage).flächenVerbrauch[3], validate = "key", validatecommand =(regfloat, '%P'))

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
        button_6.grid(row=0, column=8)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        label_1_0.grid(row=1, column=0)
        label_1_1.grid(row=2, column=0)
        label_1_2.grid(row=3, column=0)
        label_2_0.grid(row=1, column=0)
        label_2_1.grid(row=2, column=0)
        label_2_2.grid(row=3, column=0)
        label_3_0.grid(row=1, column=0)
        label_3_1.grid(row=2, column=0)
        label_3_2.grid(row=3, column=0)
        label_4_0.grid(row=1, column=0)
        label_4_1.grid(row=2, column=0)
        label_4_2.grid(row=3, column=0)

        self.entry_1_1.grid(row=2, column=1)
        self.entry_1_2.grid(row=3, column=1)
        self.entry_2_1.grid(row=2, column=1)
        self.entry_2_2.grid(row=3, column=1)
        self.entry_3_1.grid(row=2, column=1)
        self.entry_3_2.grid(row=3, column=1)
        self.entry_4_1.grid(row=2, column=1)
        self.entry_4_2.grid(row=3, column=1)

        self.auswertung_1.grid(row=1, column=1)
        self.auswertung_2.grid(row=1, column=1)
        self.auswertung_3.grid(row=1, column=1)
        self.auswertung_4.grid(row=1, column=1)

        columnconfig(self.Sozial_Ökologisch_Ökonomisch_1, self.Sozial_Ökologisch_Ökonomisch_2, self.Sozial_Ökologisch_Ökonomisch_3,
                     self.Sozial_Ökologisch_Ökonomisch_4)

        self.Sozial_Ökologisch_Ökonomisch_1.grid(row=0, column=0)
        self.Sozial_Ökologisch_Ökonomisch_3.grid(row=0, column=1)
        self.Sozial_Ökologisch_Ökonomisch_2.grid(row=1, column=0)
        self.Sozial_Ökologisch_Ökonomisch_4.grid(row=1, column=1)
        Buttons.grid(row=2, column=1)

        self.balloon.bind(label_1_1, 'Dieser Indikator beschreibt, wie zukunftsorientiert das jew. Herstellungsverfahren ist, \nbasierend auf Expertenschätzungen.')
        self.balloon.bind(label_1_2, 'Die gesamte Fläche, die für das Herstellungsverfahren (pro Maschine) benötigt wird. \nHier wird nicht nur die Maschine selbst betrachtet, \nsondern auch die gesamte zusätzliche Fläche, die ggf. benötigt wird \n(z.B. Arbeitsraum, Lagerraum, ggf. Kühlschrank, ...).')
        self.balloon.bind(label_2_1, 'Dieser Indikator beschreibt, wie zukunftsorientiert das jew. Herstellungsverfahren ist, \nbasierend auf Expertenschätzungen.')
        self.balloon.bind(label_2_2, 'Die gesamte Fläche, die für das Herstellungsverfahren (pro Maschine) benötigt wird. \nHier wird nicht nur die Maschine selbst betrachtet, \nsondern auch die gesamte zusätzliche Fläche, die ggf. benötigt wird \n(z.B. Arbeitsraum, Lagerraum, ggf. Kühlschrank, ...).')
        self.balloon.bind(label_3_1, 'Dieser Indikator beschreibt, wie zukunftsorientiert das jew. Herstellungsverfahren ist, \nbasierend auf Expertenschätzungen.')
        self.balloon.bind(label_3_2, 'Die gesamte Fläche, die für das Herstellungsverfahren (pro Maschine) benötigt wird. \nHier wird nicht nur die Maschine selbst betrachtet, \nsondern auch die gesamte zusätzliche Fläche, die ggf. benötigt wird \n(z.B. Arbeitsraum, Lagerraum, ggf. Kühlschrank, ...).')
        self.balloon.bind(label_4_1, 'Dieser Indikator beschreibt, wie zukunftsorientiert das jew. Herstellungsverfahren ist, \nbasierend auf Expertenschätzungen.')
        self.balloon.bind(label_4_2, 'Die gesamte Fläche, die für das Herstellungsverfahren (pro Maschine) benötigt wird. \nHier wird nicht nur die Maschine selbst betrachtet, \nsondern auch die gesamte zusätzliche Fläche, die ggf. benötigt wird \n(z.B. Arbeitsraum, Lagerraum, ggf. Kühlschrank, ...).')


class PageEnd(ttk.Frame):
    """Ending Page. Shows Sustainability triangles for each dimension and allows further examination of values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        Buttons = ttk.Frame(self)
        button_1 = ttk.Button(Buttons, text="Startseite (Werte erhalten)",
                          command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))
        button_2 = ttk.Button(Buttons, text="Startseite (Werte zurücksetzen)",
                          command=lambda: controller.resetter())
        button_3 = ttk.Button(Buttons, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial7, "Test"))

        Buttons.columnconfigure(2, minsize=100)
        Buttons.columnconfigure(4, minsize=40)

        boldStyle = ttk.Style()
        boldStyle.configure("Bold.Button", font=('10', 'bold'))


        self.End_1 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.End_2 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.End_3 = ttk.Frame(self, relief = "ridge", borderwidth = 5)
        self.End_4 = ttk.Frame(self, relief = "ridge", borderwidth = 5)

        name_1_1 = Button(self.End_1, text="Flechtmaschine", command=lambda: controller.show_frame(MaschineWerte1, "Flechtmaschine"))
        name_1_1.configure(font=('helvetica', '10', 'bold'))
        name_1_2 = Button(self.End_2, text="Multifilamentwickelmaschine 90", command=lambda: controller.show_frame(MaschineWerte2, "Multifilamentwickelmaschine 90"))
        name_1_2.configure(font=('helvetica', '10', 'bold'))
        name_1_3 = Button(self.End_3, text="Multifilamentwickelmaschine 48", command=lambda: controller.show_frame(MaschineWerte3, "Multifilamentwickelmaschine 48"))
        name_1_3.configure(font=('helvetica', '10', 'bold'))
        name_1_4 = Button(self.End_4, text="Nasswickelmaschine", command=lambda: controller.show_frame(MaschineWerte4, "Nasswickelmaschine"))
        name_1_4.configure(font=('helvetica', '10', 'bold'))

        self.auswertung_1 = Canvas(self.End_1, width=300, height=360)
        self.auswertung_2 = Canvas(self.End_2, width=300, height=360)
        self.auswertung_3 = Canvas(self.End_3, width=300, height=360)
        self.auswertung_4 = Canvas(self.End_4, width=300, height=360)

        points = [60, 240, 100, 240, 150, 120, 150, 0] #points for the sustainability triangle
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
        button_3.grid(row=0, column=3)

        name_1_1.grid(row=0, column=0)
        name_1_2.grid(row=0, column=0)
        name_1_3.grid(row=0, column=0)
        name_1_4.grid(row=0, column=0)

        self.auswertung_1.grid(row=1, column=0)
        self.auswertung_2.grid(row=1, column=0)
        self.auswertung_3.grid(row=1, column=0)
        self.auswertung_4.grid(row=1, column=0)



        self.End_1.grid(row=0, column=0)
        self.End_3.grid(row=0, column=1)
        self.End_2.grid(row=0, column=2)
        self.End_4.grid(row=0, column=3)
        Buttons.grid(row=2, column=2, columnspan=2)


class MaschineWerte1(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 0. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(1, minsize=100)
        self.columnconfigure(4, minsize=100)
        ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=14, sticky='ns')

        button_1 = ttk.Button(self, text="Zurück"
                          , command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_2 = ttk.Button(self, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial8, "Test"))

        self.columnconfigure(5, minsize=3)
        self.columnconfigure(7, minsize=3)


        self.wert_1_1 = Label(self, text= round(controller.get_page(StartPage).emissionen_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).emissionen_norm[0]))
        self.wert_1_2 = Label(self, text= round(controller.get_page(StartPage).giftMaterial_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).giftMaterial_norm[0]))

        self.wert_2_1 = Label(self, text=round(controller.get_page(StartPage).abfallProzentsatz_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).abfallProzentsatz_norm[0]))
        self.wert_2_2 = Label(self, text=round(controller.get_page(StartPage).abfallSzenarien_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).abfallSzenarien_norm[0]))
        self.wert_2_3 = Label(self, text=round(controller.get_page(StartPage).recyclingAbsolut_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingAbsolut_norm[0]))
        self.wert_2_4 = Label(self, text=round(controller.get_page(StartPage).recyclingRelativ_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingRelativ_norm[0]))

        self.wert_3_1 = Label(self, text=round(controller.get_page(StartPage).verbrauchEnergie_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchEnergie_norm[0]))
        self.wert_3_2 = Label(self, text=round(controller.get_page(StartPage).verbrauchMaterial_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchMaterial_norm[0]))
        self.wert_3_3 = Label(self, text=round(controller.get_page(StartPage).kostenEffizienz_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).kostenEffizienz_norm[0]))
        self.wert_3_4 = Label(self, text=round(controller.get_page(StartPage).kostenAufwand_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).kostenAufwand_norm[0]))

        self.wert_4_1 = Label(self, text=round(controller.get_page(StartPage).zeitAufwand_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).zeitAufwand_norm[0]))
        self.wert_4_2 = Label(self, text=round(controller.get_page(StartPage).flexibilität_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).flexibilität_norm[0]))
        self.wert_4_3 = Label(self, text=round(controller.get_page(StartPage).zeitEffizienz_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).zeitEffizienz_norm[0]))

        self.wert_5_1 = Label(self, text=round(controller.get_page(StartPage).produktQualität_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).produktQualität_norm[0]))

        self.wert_6_1 = Label(self, text=round(controller.get_page(StartPage).innovativität_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).innovativität_norm[0]))
        self.wert_6_2 = Label(self, text=round(controller.get_page(StartPage).flächenVerbrauch_norm[0].get(), 5), bg = colourer(controller.get_page(StartPage).flächenVerbrauch_norm[0]))

        name_1 = ttk.Label(self, text="Sozial-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_1_1 = ttk.Label(self, text="Treibhausgasemissionen   (g/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_1_2 = ttk.Label(self, text="Kritikalität des Materials   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_2 = ttk.Label(self, text="Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_2_1 = ttk.Label(self, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_2 = ttk.Label(self, text="Abfallszenarien    (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_3 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_4 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))

        name_3 = ttk.Label(self, text="Ökologisch-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_3_1 = ttk.Label(self, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_2 = ttk.Label(self, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_3 = ttk.Label(self, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_4 = ttk.Label(self, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))

        name_4 = ttk.Label(self, text="Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_4_1 = ttk.Label(self, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_2 = ttk.Label(self, text="Flexibilität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_3 = ttk.Label(self, text="Zeitliche Effizienz   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_5 = ttk.Label(self, text="Sozial-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_5_1 = ttk.Label(self, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))

        name_6 = ttk.Label(self, text="Sozial-Ökonomisch-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_6_1 = ttk.Label(self, text="Innovativität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_6_2 = ttk.Label(self, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))


        name_1.grid(row=0, column=0)


        name_1_1.grid(row=1, column=0)
        name_1_2.grid(row=2, column=0)


        name_2.grid(row=0, column=3)
        name_2_1.grid(row=1, column=3)
        name_2_2.grid(row=2, column=3)
        name_2_3.grid(row=3, column=3)
        name_2_4.grid(row=4, column=3)


        name_3.grid(row=4, column=0)
        name_3_1.grid(row=5, column=0)
        name_3_2.grid(row=6, column=0)
        name_3_3.grid(row=7, column=0)
        name_3_4.grid(row=8, column=0)


        name_4.grid(row=6, column=3)
        name_4_1.grid(row=7, column=3)
        name_4_2.grid(row=8, column=3)
        name_4_3.grid(row=9, column=3)


        name_5.grid(row=10, column=0)
        name_5_1.grid(row=11, column=0)


        name_6.grid(row=11, column=3)
        name_6_1.grid(row=12, column=3)
        name_6_2.grid(row=13, column=3)


        self.wert_1_1.grid(row=1, column=1)
        self.wert_1_2.grid(row=2, column=1)

        self.wert_2_1.grid(row=1, column=4)
        self.wert_2_2.grid(row=2, column=4)
        self.wert_2_3.grid(row=3, column=4)
        self.wert_2_4.grid(row=4, column=4)

        self.wert_3_1.grid(row=5, column=1)
        self.wert_3_2.grid(row=6, column=1)
        self.wert_3_3.grid(row=7, column=1)
        self.wert_3_4.grid(row=8, column=1)

        self.wert_4_1.grid(row=7, column=4)
        self.wert_4_2.grid(row=8, column=4)
        self.wert_4_3.grid(row=9, column=4)


        self.wert_5_1.grid(row=11, column=1)

        self.wert_6_1.grid(row=12, column=4)
        self.wert_6_2.grid(row=13, column=4)

        for i in range(15):
            self.rowconfigure(i, minsize=20)


        button_1.grid(row=15, column=4)
        button_2.grid(row=15,column = 6)


class MaschineWerte2(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 1. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(1, minsize=100)
        self.columnconfigure(4, minsize=100)
        ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=14, sticky='ns')

        button_1 = ttk.Button(self, text="Zurück"
                          , command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_2 = ttk.Button(self, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial9, "Test"))

        self.columnconfigure(5, minsize=3)
        self.columnconfigure(7, minsize=3)


        self.wert_1_1 = Label(self, text= round(controller.get_page(StartPage).emissionen_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).emissionen_norm[1]))
        self.wert_1_2 = Label(self, text= round(controller.get_page(StartPage).giftMaterial_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).giftMaterial_norm[1]))

        self.wert_2_1 = Label(self, text=round(controller.get_page(StartPage).abfallProzentsatz_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).abfallProzentsatz_norm[1]))
        self.wert_2_2 = Label(self, text=round(controller.get_page(StartPage).abfallSzenarien_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).abfallSzenarien_norm[1]))
        self.wert_2_3 = Label(self, text=round(controller.get_page(StartPage).recyclingAbsolut_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingAbsolut_norm[1]))
        self.wert_2_4 = Label(self, text=round(controller.get_page(StartPage).recyclingRelativ_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingRelativ_norm[1]))

        self.wert_3_1 = Label(self, text=round(controller.get_page(StartPage).verbrauchEnergie_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchEnergie_norm[1]))
        self.wert_3_2 = Label(self, text=round(controller.get_page(StartPage).verbrauchMaterial_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchMaterial_norm[1]))
        self.wert_3_3 = Label(self, text=round(controller.get_page(StartPage).kostenEffizienz_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).kostenEffizienz_norm[1]))
        self.wert_3_4 = Label(self, text=round(controller.get_page(StartPage).kostenAufwand_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).kostenAufwand_norm[1]))

        self.wert_4_1 = Label(self, text=round(controller.get_page(StartPage).zeitAufwand_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).zeitAufwand_norm[1]))
        self.wert_4_2 = Label(self, text=round(controller.get_page(StartPage).flexibilität_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).flexibilität_norm[1]))
        self.wert_4_3 = Label(self, text=round(controller.get_page(StartPage).zeitEffizienz_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).zeitEffizienz_norm[1]))

        self.wert_5_1 = Label(self, text=round(controller.get_page(StartPage).produktQualität_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).produktQualität_norm[1]))

        self.wert_6_1 = Label(self, text=round(controller.get_page(StartPage).innovativität_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).innovativität_norm[1]))
        self.wert_6_2 = Label(self, text=round(controller.get_page(StartPage).flächenVerbrauch_norm[1].get(), 5), bg = colourer(controller.get_page(StartPage).flächenVerbrauch_norm[1]))

        name_1 = ttk.Label(self, text="Sozial-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_1_1 = ttk.Label(self, text="Treibhausgasemissionen   (g/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_1_2 = ttk.Label(self, text="Kritikalität des Materials   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_2 = ttk.Label(self, text="Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_2_1 = ttk.Label(self, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_2 = ttk.Label(self, text="Abfallszenarien    (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_3 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_4 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))

        name_3 = ttk.Label(self, text="Ökologisch-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_3_1 = ttk.Label(self, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_2 = ttk.Label(self, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_3 = ttk.Label(self, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_4 = ttk.Label(self, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))

        name_4 = ttk.Label(self, text="Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_4_1 = ttk.Label(self, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_2 = ttk.Label(self, text="Flexibilität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_3 = ttk.Label(self, text="Zeitliche Effizienz   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_5 = ttk.Label(self, text="Sozial-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_5_1 = ttk.Label(self, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))

        name_6 = ttk.Label(self, text="Sozial-Ökonomisch-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_6_1 = ttk.Label(self, text="Innovativität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_6_2 = ttk.Label(self, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))


        name_1.grid(row=0, column=0)


        name_1_1.grid(row=1, column=0)
        name_1_2.grid(row=2, column=0)


        name_2.grid(row=0, column=3)
        name_2_1.grid(row=1, column=3)
        name_2_2.grid(row=2, column=3)
        name_2_3.grid(row=3, column=3)
        name_2_4.grid(row=4, column=3)


        name_3.grid(row=4, column=0)
        name_3_1.grid(row=5, column=0)
        name_3_2.grid(row=6, column=0)
        name_3_3.grid(row=7, column=0)
        name_3_4.grid(row=8, column=0)


        name_4.grid(row=6, column=3)
        name_4_1.grid(row=7, column=3)
        name_4_2.grid(row=8, column=3)
        name_4_3.grid(row=9, column=3)


        name_5.grid(row=10, column=0)
        name_5_1.grid(row=11, column=0)


        name_6.grid(row=11, column=3)
        name_6_1.grid(row=12, column=3)
        name_6_2.grid(row=13, column=3)


        self.wert_1_1.grid(row=1, column=1)
        self.wert_1_2.grid(row=2, column=1)

        self.wert_2_1.grid(row=1, column=4)
        self.wert_2_2.grid(row=2, column=4)
        self.wert_2_3.grid(row=3, column=4)
        self.wert_2_4.grid(row=4, column=4)

        self.wert_3_1.grid(row=5, column=1)
        self.wert_3_2.grid(row=6, column=1)
        self.wert_3_3.grid(row=7, column=1)
        self.wert_3_4.grid(row=8, column=1)

        self.wert_4_1.grid(row=7, column=4)
        self.wert_4_2.grid(row=8, column=4)
        self.wert_4_3.grid(row=9, column=4)


        self.wert_5_1.grid(row=11, column=1)

        self.wert_6_1.grid(row=12, column=4)
        self.wert_6_2.grid(row=13, column=4)

        for i in range(15):
            self.rowconfigure(i, minsize=20)


        button_1.grid(row=15, column=4)
        button_2.grid(row=15,column = 6)


class MaschineWerte3(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 2. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(1, minsize=100)
        self.columnconfigure(4, minsize=100)
        ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=14, sticky='ns')

        button_1 = Button(self, text="Zurück"
                          , command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_2 = ttk.Button(self, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial10, "Test"))

        self.columnconfigure(5, minsize=3)
        self.columnconfigure(7, minsize=3)


        self.wert_1_1 = Label(self, text= round(controller.get_page(StartPage).emissionen_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).emissionen_norm[2]))
        self.wert_1_2 = Label(self, text= round(controller.get_page(StartPage).giftMaterial_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).giftMaterial_norm[2]))

        self.wert_2_1 = Label(self, text=round(controller.get_page(StartPage).abfallProzentsatz_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).abfallProzentsatz_norm[2]))
        self.wert_2_2 = Label(self, text=round(controller.get_page(StartPage).abfallSzenarien_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).abfallSzenarien_norm[2]))
        self.wert_2_3 = Label(self, text=round(controller.get_page(StartPage).recyclingAbsolut_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingAbsolut_norm[2]))
        self.wert_2_4 = Label(self, text=round(controller.get_page(StartPage).recyclingRelativ_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingRelativ_norm[2]))

        self.wert_3_1 = Label(self, text=round(controller.get_page(StartPage).verbrauchEnergie_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchEnergie_norm[2]))
        self.wert_3_2 = Label(self, text=round(controller.get_page(StartPage).verbrauchMaterial_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchMaterial_norm[2]))
        self.wert_3_3 = Label(self, text=round(controller.get_page(StartPage).kostenEffizienz_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).kostenEffizienz_norm[2]))
        self.wert_3_4 = Label(self, text=round(controller.get_page(StartPage).kostenAufwand_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).kostenAufwand_norm[2]))

        self.wert_4_1 = Label(self, text=round(controller.get_page(StartPage).zeitAufwand_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).zeitAufwand_norm[2]))
        self.wert_4_2 = Label(self, text=round(controller.get_page(StartPage).flexibilität_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).flexibilität_norm[2]))
        self.wert_4_3 = Label(self, text=round(controller.get_page(StartPage).zeitEffizienz_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).zeitEffizienz_norm[2]))

        self.wert_5_1 = Label(self, text=round(controller.get_page(StartPage).produktQualität_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).produktQualität_norm[2]))

        self.wert_6_1 = Label(self, text=round(controller.get_page(StartPage).innovativität_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).innovativität_norm[2]))
        self.wert_6_2 = Label(self, text=round(controller.get_page(StartPage).flächenVerbrauch_norm[2].get(), 5), bg = colourer(controller.get_page(StartPage).flächenVerbrauch_norm[2]))

        name_1 = ttk.Label(self, text="Sozial-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_1_1 = ttk.Label(self, text="Treibhausgasemissionen   (g/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_1_2 = ttk.Label(self, text="Kritikalität des Materials   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_2 = ttk.Label(self, text="Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_2_1 = ttk.Label(self, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_2 = ttk.Label(self, text="Abfallszenarien    (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_3 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_4 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))

        name_3 = ttk.Label(self, text="Ökologisch-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_3_1 = ttk.Label(self, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_2 = ttk.Label(self, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_3 = ttk.Label(self, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_4 = ttk.Label(self, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))

        name_4 = ttk.Label(self, text="Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_4_1 = ttk.Label(self, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_2 = ttk.Label(self, text="Flexibilität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_3 = ttk.Label(self, text="Zeitliche Effizienz   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_5 = ttk.Label(self, text="Sozial-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_5_1 = ttk.Label(self, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))

        name_6 = ttk.Label(self, text="Sozial-Ökonomisch-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_6_1 = ttk.Label(self, text="Innovativität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_6_2 = ttk.Label(self, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))


        name_1.grid(row=0, column=0)


        name_1_1.grid(row=1, column=0)
        name_1_2.grid(row=2, column=0)


        name_2.grid(row=0, column=3)
        name_2_1.grid(row=1, column=3)
        name_2_2.grid(row=2, column=3)
        name_2_3.grid(row=3, column=3)
        name_2_4.grid(row=4, column=3)


        name_3.grid(row=4, column=0)
        name_3_1.grid(row=5, column=0)
        name_3_2.grid(row=6, column=0)
        name_3_3.grid(row=7, column=0)
        name_3_4.grid(row=8, column=0)


        name_4.grid(row=6, column=3)
        name_4_1.grid(row=7, column=3)
        name_4_2.grid(row=8, column=3)
        name_4_3.grid(row=9, column=3)


        name_5.grid(row=10, column=0)
        name_5_1.grid(row=11, column=0)


        name_6.grid(row=11, column=3)
        name_6_1.grid(row=12, column=3)
        name_6_2.grid(row=13, column=3)


        self.wert_1_1.grid(row=1, column=1)
        self.wert_1_2.grid(row=2, column=1)

        self.wert_2_1.grid(row=1, column=4)
        self.wert_2_2.grid(row=2, column=4)
        self.wert_2_3.grid(row=3, column=4)
        self.wert_2_4.grid(row=4, column=4)

        self.wert_3_1.grid(row=5, column=1)
        self.wert_3_2.grid(row=6, column=1)
        self.wert_3_3.grid(row=7, column=1)
        self.wert_3_4.grid(row=8, column=1)

        self.wert_4_1.grid(row=7, column=4)
        self.wert_4_2.grid(row=8, column=4)
        self.wert_4_3.grid(row=9, column=4)


        self.wert_5_1.grid(row=11, column=1)

        self.wert_6_1.grid(row=12, column=4)
        self.wert_6_2.grid(row=13, column=4)

        for i in range(15):
            self.rowconfigure(i, minsize=20)


        button_1.grid(row=15, column=4)
        button_2.grid(row=15,column = 6)


class MaschineWerte4(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(1, minsize=100)
        self.columnconfigure(4, minsize=100)
        ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=14, sticky='ns')

        button_1 = ttk.Button(self, text="Zurück"
                          , command=lambda: controller.show_frame(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))
        button_2 = ttk.Button(self, text=" ? ", command=lambda: controller.acceptwerte(PageTutorial11, "Test"))

        self.columnconfigure(5, minsize=3)
        self.columnconfigure(7, minsize=3)


        self.wert_1_1 = Label(self, text= round(controller.get_page(StartPage).emissionen_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).emissionen_norm[3]))
        self.wert_1_2 = Label(self, text= round(controller.get_page(StartPage).giftMaterial_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).giftMaterial_norm[3]))

        self.wert_2_1 = Label(self, text=round(controller.get_page(StartPage).abfallProzentsatz_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).abfallProzentsatz_norm[3]))
        self.wert_2_2 = Label(self, text=round(controller.get_page(StartPage).abfallSzenarien_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).abfallSzenarien_norm[3]))
        self.wert_2_3 = Label(self, text=round(controller.get_page(StartPage).recyclingAbsolut_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingAbsolut_norm[3]))
        self.wert_2_4 = Label(self, text=round(controller.get_page(StartPage).recyclingRelativ_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).recyclingRelativ_norm[3]))

        self.wert_3_1 = Label(self, text=round(controller.get_page(StartPage).verbrauchEnergie_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchEnergie_norm[3]))
        self.wert_3_2 = Label(self, text=round(controller.get_page(StartPage).verbrauchMaterial_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).verbrauchMaterial_norm[3]))
        self.wert_3_3 = Label(self, text=round(controller.get_page(StartPage).kostenEffizienz_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).kostenEffizienz_norm[3]))
        self.wert_3_4 = Label(self, text=round(controller.get_page(StartPage).kostenAufwand_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).kostenAufwand_norm[3]))

        self.wert_4_1 = Label(self, text=round(controller.get_page(StartPage).zeitAufwand_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).zeitAufwand_norm[3]))
        self.wert_4_2 = Label(self, text=round(controller.get_page(StartPage).flexibilität_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).flexibilität_norm[3]))
        self.wert_4_3 = Label(self, text=round(controller.get_page(StartPage).zeitEffizienz_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).zeitEffizienz_norm[3]))

        self.wert_5_1 = Label(self, text=round(controller.get_page(StartPage).produktQualität_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).produktQualität_norm[3]))

        self.wert_6_1 = Label(self, text=round(controller.get_page(StartPage).innovativität_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).innovativität_norm[3]))
        self.wert_6_2 = Label(self, text=round(controller.get_page(StartPage).flächenVerbrauch_norm[3].get(), 5), bg = colourer(controller.get_page(StartPage).flächenVerbrauch_norm[3]))

        name_1 = ttk.Label(self, text="Sozial-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_1_1 = ttk.Label(self, text="Treibhausgasemissionen   (g/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_1_2 = ttk.Label(self, text="Kritikalität des Materials   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_2 = ttk.Label(self, text="Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_2_1 = ttk.Label(self, text="Abfall   (m)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_2 = ttk.Label(self, text="Abfallszenarien    (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_3 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Absolut)   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_2_4 = ttk.Label(self, text="Anteil verwendetes Recyclingmaterial (Relativ)   (%)" , font = tkFont.Font(family = "helvetica", size=10))

        name_3 = ttk.Label(self, text="Ökologisch-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_3_1 = ttk.Label(self, text="Energieverbrauch   (Wh/kg)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_2 = ttk.Label(self, text="Materialverbrauch   (g)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_3 = ttk.Label(self, text="Kosteneffizienz   (Euro/s)" , font = tkFont.Font(family = "helvetica", size=10))
        name_3_4 = ttk.Label(self, text="Ressourcenkosten   (Euro/kg)" , font = tkFont.Font(family = "helvetica", size=10))

        name_4 = ttk.Label(self, text="Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_4_1 = ttk.Label(self, text="Zykluszeit   (min/Lage)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_2 = ttk.Label(self, text="Flexibilität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_4_3 = ttk.Label(self, text="Zeitliche Effizienz   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))

        name_5 = ttk.Label(self, text="Sozial-Ökonomische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_5_1 = ttk.Label(self, text="Produktqualität  (Porengehalt in %)" , font = tkFont.Font(family = "helvetica", size=10))

        name_6 = ttk.Label(self, text="Sozial-Ökonomisch-Ökologische Indikatoren", relief = 'ridge' , font = tkFont.Font(family = "helvetica", size=10))
        name_6_1 = ttk.Label(self, text="Innovativität   (Skala)" , font = tkFont.Font(family = "helvetica", size=10))
        name_6_2 = ttk.Label(self, text="Flächenverbrauch   (m^2)" , font = tkFont.Font(family = "helvetica", size=10))


        name_1.grid(row=0, column=0)


        name_1_1.grid(row=1, column=0)
        name_1_2.grid(row=2, column=0)


        name_2.grid(row=0, column=3)
        name_2_1.grid(row=1, column=3)
        name_2_2.grid(row=2, column=3)
        name_2_3.grid(row=3, column=3)
        name_2_4.grid(row=4, column=3)


        name_3.grid(row=4, column=0)
        name_3_1.grid(row=5, column=0)
        name_3_2.grid(row=6, column=0)
        name_3_3.grid(row=7, column=0)
        name_3_4.grid(row=8, column=0)


        name_4.grid(row=6, column=3)
        name_4_1.grid(row=7, column=3)
        name_4_2.grid(row=8, column=3)
        name_4_3.grid(row=9, column=3)


        name_5.grid(row=10, column=0)
        name_5_1.grid(row=11, column=0)


        name_6.grid(row=11, column=3)
        name_6_1.grid(row=12, column=3)
        name_6_2.grid(row=13, column=3)


        self.wert_1_1.grid(row=1, column=1)
        self.wert_1_2.grid(row=2, column=1)

        self.wert_2_1.grid(row=1, column=4)
        self.wert_2_2.grid(row=2, column=4)
        self.wert_2_3.grid(row=3, column=4)
        self.wert_2_4.grid(row=4, column=4)

        self.wert_3_1.grid(row=5, column=1)
        self.wert_3_2.grid(row=6, column=1)
        self.wert_3_3.grid(row=7, column=1)
        self.wert_3_4.grid(row=8, column=1)

        self.wert_4_1.grid(row=7, column=4)
        self.wert_4_2.grid(row=8, column=4)
        self.wert_4_3.grid(row=9, column=4)


        self.wert_5_1.grid(row=11, column=1)

        self.wert_6_1.grid(row=12, column=4)
        self.wert_6_2.grid(row=13, column=4)

        for i in range(15):
            self.rowconfigure(i, minsize=20)


        button_1.grid(row=15, column=4)
        button_2.grid(row=15,column = 6)


class PageTutorial1(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller


        button_1 = ttk.Button(self, text="Zurück"
                          , command=lambda: controller.acceptwerte(PageOne, "Sozial-Ökologische Indikatoren"))

        load1 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load1 = load1.resize((1355, 739), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1




        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial2(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller


        button_1 = ttk.Button(self, text="Zurück"
                          , command=lambda: controller.acceptwerte(PageTwo, "Ökologische Indikatoren"))

        load1 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load1 = load1.resize((1355, 739), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1




        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial3(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(PageThree, "Ökologisch-Ökonomische Indikatoren"))

        load1 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load1 = load1.resize((1355, 739), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial4(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(PageFour, "Ökonomische Indikatoren"))

        load1 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load1 = load1.resize((1355, 739), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial5(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(PageFive, "Sozial-Ökonomische Indikatoren"))

        load1 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load1 = load1.resize((1355, 739), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial6(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(PageSix, "Sozial-Ökonomisch-Ökologische Indikatoren"))

        load1 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load1 = load1.resize((1355, 739), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)


class PageTutorial7(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(PageEnd, "Visualisierung durch Nachhaltigkeitsdreieck"))

        load1 = Image.open(resource_path('/IMAGES/Capture8.png'))
        load1 = load1.resize((1355, 717), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)


class PageTutorial8(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(MaschineWerte1, "Flechtmaschine"))

        load1 = Image.open(resource_path('/IMAGES/Capture9.png'))
        load1 = load1.resize((1355, 578), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial9(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(MaschineWerte2, "Multifilamentwickelmaschine 90"))

        load1 = Image.open(resource_path('/IMAGES/Capture9.png'))
        load1 = load1.resize((1355, 578), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial10(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(MaschineWerte3, "Multifilamentwickelmaschine 48"))

        load1 = Image.open(resource_path('/IMAGES/Capture9.png'))
        load1 = load1.resize((1355, 578), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)

class PageTutorial11(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück"
                              , command=lambda: controller.acceptwerte(MaschineWerte4, "Nasswickelmaschine"))

        load1 = Image.open(resource_path('/IMAGES/Capture9.png'))
        load1 = load1.resize((1355, 578), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(load1)
        img1 = Label(self, image=render1)
        img1.image = render1

        img1.grid(row=0, column=0)
        button_1.grid(row=1, column=0)


class StartTutorial1(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller


        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial2, "Tutorial (2/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load2 = Image.open(resource_path('/IMAGES/Capture2.png'))
        load2 = load2.resize((1355, 583), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self, image=render2)
        img2.image = render2




        img2.grid(row=0, column=0, columnspan=3)

        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial2(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial1, "Tutorial (1/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial3, "Tutorial (3/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture3.png'))
        load3 = load3.resize((1355, 601), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial3(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial2, "Tutorial (2/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial4, "Tutorial (4/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture4.png'))
        load3 = load3.resize((1355, 693), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial4(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial3, "Tutorial (3/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial5, "Tutorial (5/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture5.png'))
        load3 = load3.resize((1355, 675), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial5(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial4, "Tutorial (4/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial6, "Tutorial (6/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture6.png'))
        load3 = load3.resize((1355, 673), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial6(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial5, "Tutorial (5/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial7, "Tutorial (7/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture7.png'))
        load3 = load3.resize((1355, 739), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial7(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial6, "Tutorial (6/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial8, "Tutorial (8/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture8.png'))
        load3 = load3.resize((1355, 717), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial8(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial7, "Tutorial (7/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial9, "Tutorial (9/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture9.png'))
        load3 = load3.resize((1355, 578), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial9(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial8, "Tutorial (8/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial10, "Tutorial (10/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture10.png'))
        load3 = load3.resize((1355, 504), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial10(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial9, "Tutorial (9/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial11, "Tutorial (11/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture11.png'))
        load3 = load3.resize((1355, 284), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial11(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial10, "Tutorial (10/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial12, "Tutorial (12/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture12.png'))
        load3 = load3.resize((1355, 431), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial12(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial11, "Tutorial (11/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial13, "Tutorial (13/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture13.png'))
        load3 = load3.resize((1355, 537), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial13(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial12, "Tutorial (12/14)"))
        button_2 = ttk.Button(self, text="Nächste Seite",
                              command=lambda: controller.show_frame(StartTutorial14, "Tutorial (14/14)"))
        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture14.png'))
        load3 = load3.resize((1355, 435), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)

class StartTutorial14(ttk.Frame):
    """Page for checking the normalised values for all indicators for Maschine 3. Also includes colour feedback on the values"""
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        button_1 = ttk.Button(self, text="Zurück",
                              command=lambda: controller.show_frame(StartTutorial13, "Tutorial (13/14)"))

        button_3 = ttk.Button(self, text="Abbrechen", command=lambda: controller.show_frame(StartPage, "Maschinenauswahl"))

        load3 = Image.open(resource_path('/IMAGES/Capture15.png'))
        load3 = load3.resize((1355, 509), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(load3)
        img3 = Label(self, image=render3)
        img3.image = render3




        img3.grid(row=0, column=0, columnspan=3)
        button_1.grid(row=1, column=0)

        button_3.grid(row=1, column=2)



app = H2MW()
Pmw.initialise(app)
app.set_theme("aquativo") #sets ThemedTK Theme
app.iconbitmap(resource_path('/IMAGES/H2MW_ICON.ico')) #Sets Application Icon
app.resizable(0,0) #Disables resizing

app.mainloop()
