"""
This scripts presents an interactive overview of the Volvo thermal evaporation chamber and the attached instruments

Created by Tobias H. Hemmingsen (tohoy)
Created on 28-11-2024
"""

# Import libraries
import tkinter as tk



class Instrument:
    def __init__(self, x1, y1, x2, y2, color, name, description):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.name = name
        self.description = description

def drawTheVolvo(instruments):
    canvas.delete("all")
    canvas.create_rectangle(150, 50, w-50, h-50, fill='grey')
    for instrument in instruments:
        drawInstrument(instrument)

def drawInstrument(instrument):
    canvas.create_rectangle(instrument.x1, instrument.y1, instrument.x2, instrument.y2, fill=instrument.color)

# Create the main window
w = 500
h = 300

window = tk.Tk()
window.title("Volvo interactive diagram")
window.minsize(width=w, height=h)


# Make a sketch of the Volvo
canvas = tk.Canvas(window, width=w, height=h, bg='white')
canvas.pack()

canvas.create_rectangle(150, 50, w-50, h-50, fill='grey')



# Make detailed sketches of the instruments
Instrument1 = Instrument(100, 100, 150, 200, 'blue', 'Instrument1', 'This is a description of Instrument1')
Instrument2 = Instrument(200, 100, 250, 200, 'red', 'Instrument2', 'This is a description of Instrument2')

instruments = [Instrument1, Instrument2]

drawTheVolvo(instruments)


# Add the ability to click on instruments to view more
def showDescription(event):
    x = event.x
    y = event.y
    instrumentClicked = False
    for instrument in instruments:
        if instrument.x1 < x < instrument.x2 and instrument.y1 < y < instrument.y2:
            # Clear the canvas
            canvas.delete("all")
            # Draw the instrument
            drawInstrument(instrument)
            # Add the name and description
            canvas.create_text(300, 10, text=instrument.name)
            canvas.create_text(300, 30, text=instrument.description)
            instrumentClicked = True

    if instrumentClicked == False:
        drawTheVolvo(instruments)


canvas.bind("<Button-1>", showDescription)




window.mainloop()
