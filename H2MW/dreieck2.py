from tkinter import*
dreieck = Tk()
Leinwand = Canvas(dreieck, width= 200, height= 200, background= 'grey')
Leinwand.grid(row=1, column=1)

points = [10,180,75,180,30,120]
points2 = [75,180,140,180,120,120]
points3 = [30,120,75,120,50,60]
points4 = [75,120,120,120,100,60]
points5 = [50,60,75,120,100,60,75,0]
points6 = [30,120,75,180,120,120]
points7 = [70,140,80,140,90,120,80,100,70,100,60,120]

Leinwand.create_polygon(points,outline='#f11', fill='#1f1')
Leinwand.create_polygon(points2,outline='#f11', fill='#1f1')
Leinwand.create_polygon(points3,outline='#f11', fill='#1f1')
Leinwand.create_polygon(points4,outline='#f11', fill='#1f1')
Leinwand.create_polygon(points5,outline='#f11', fill='#1f1')
Leinwand.create_polygon(points6,outline='#f11', fill='#1f1')
#Leinwand.create_polygon(points7,outline='#f11', fill='#1f1')


dreieck.mainloop()