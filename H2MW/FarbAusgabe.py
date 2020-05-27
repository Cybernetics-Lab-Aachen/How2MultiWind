from tkinter import *



class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        self.wert = DoubleVar()

        self.wert.set(0.1)



        canvas = Canvas(self)
        canvas.create_rectangle(20, 10, 120, 80, outline="#000000", fill=colourer(0.9))


        canvas.pack(fill=BOTH, expand=1)

def colourer(wert):

        if wert <= 0.5:

            hex_1 = hex(int(wert * 255))

            if int(wert * 255) > 15:
                return( '#ff' + hex_1[2:4] + '00' )
            else:
                return('#ff0' + hex_1[2:4] + '00' )

        else:

            hex_1 = hex(int(255 - ((wert - 0.5) * 255)))

            print('#' + hex_1[2:4] + 'ff00')
            return('#' + hex_1[2:4] + 'ff00')


def main():


    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


points = [20, 360, 130, 360, 80, 240, 60, 240]
points2 = [170, 360, 280, 360, 240, 240, 220, 240]
points3 = [60, 240, 150, 240, 100, 120]
points4 = [150, 240, 240, 240, 200, 120]
points5 = [100, 120, 150, 240, 200, 120, 150, 0]
points6 = [80, 240, 130, 360, 170, 360, 220, 240]

if __name__ == '__main__':
    main()