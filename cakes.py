#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hillyerbrandtf
#
# Created:     24/08/2015
# Copyright:   (c) hillyerbrandtf 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

"""Code Listing 1.4"""

from tkinter import *
import random

class GraphicalCake:

    def __init__(self, canvas, x, y, w, h):
        """ Sets up coordinates of cakes bounding area"""
        self.canvas = canvas
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.num_layers = random.randrange(2,6)
        self.cake_colour = "#993322"
        self.fill_colour = self.random_colour()

    def draw(self):
        """ Sets up coordinates at which cake begins to be drawn. These coordinates
            are based on those of the cake's bounding area but allow for
            some margin around the edges"""

        x = self.x + self.w / 10
        y = self.y + 3 * self.h / 4
        w = 4 * self.w/5

        thickness = w / 10
        filling_thickness = w / 30
        h = thickness + filling_thickness
        cherry_r = filling_thickness

        for i in range(self.num_layers):
            #lower oval - recall that \ means that the next line is a continuation of the current line
            self.canvas.create_oval(x, y + thickness, x + w, y + thickness + h, fill = self.cake_colour, outline = self.cake_colour)
            # rectangle for thickness
            self.canvas.create_rectangle(x, y + h / 2, x + w, y + thickness + h /2 , fill=self.cake_colour, outline = self.cake_colour)
            #top oval
            self.canvas.create_oval(x, y, x + w, y + h, fill = self.cake_colour)
            y -= filling_thickness
            # lower oval Ã¢â‚¬â€œ the following three lines would be a single long line of code
            self.canvas.create_oval(x, y + filling_thickness, x + w, y + filling_thickness + h, fill = self.fill_colour, outline = self.fill_colour)
            #rectangle for thickness
            self.canvas.create_rectangle(x, y + h / 2, x + w, y + filling_thickness +  h / 2, fill = self.fill_colour, outline = self.fill_colour)
            #top oval
            self.canvas.create_oval(x, y, x + w, y + h, fill  = self.fill_colour)
            y -= thickness
        #cherry on the top
        self.canvas.create_oval(x + w / 2 - cherry_r, y + cherry_r, x + w / 2 +  cherry_r, y + 3 * cherry_r, fill = "red")

    def random_colour(self):
        """Returns a random colour as a hexidecimal string"""
        hex_chars =['a','b','c','d','e','f','1','2','3','4',
                '5','6','7','8','9','0']
        s = "#"
        for i in range(6):
             s += hex_chars[random.randrange(len(hex_chars))]
        return s



class Bakery:

    def __init__(self, parent):
        """Dictates the size of the "bakery window" and how many "shelves" it has """
        NUM_ROWS = 2 # the number of "shelves - too many may produce overlap"
        NUM_COLS = 5 # How many cakes per shelf
        CW = 600 # width of the canvas
        CHT = 300 # heigth of the canvas

        canvas = Canvas(parent, width = CW, height = CHT, bg = "white")
        canvas.grid(column = 0, row = 0)

        cakes = []
        #Loop below creates enough cakes to fill the window and appends to a list
        #Each cake is passed the x, y, width, and height of its bounding area
        #so it can calculate the coordinates at which to draw itself
        for i in range(NUM_ROWS):
           for j in range(NUM_COLS):
            cakes.append(GraphicalCake(canvas, j * CW / NUM_COLS, i * CHT / NUM_ROWS, CW / NUM_COLS, CHT / NUM_ROWS ))

        #Loop below asks each cake to draw itself
        for i in range(len(cakes)):
            cakes[i].draw()

#if name == '__main__':
    root = Tk()
    root.title("A Bakery window of yummy cakes")
    b = Bakery(root)
    root.mainloop()
