#-------------------------------------------------------------------------------
# Name:        bookv3
# Purpose:
#
# Author:      Flo HB
#
# Created:     21/08/2015
# Copyright:   (c) Flo HB 2015
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#import GUI library
from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox

#create the book class incorporating instance variables and methods
class Book:
    def __init__(self, title_i, author_i, isbn_i, publisher_i):
        self.title = title_i
        self.author= author_i
        self.isbn=isbn_i
        self.type= 'Book'
        self.is_read= False
        self.publisher= publisher_i

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_type(self):
        return self.type

    def get_isbn(self):
        return self.isbn

    def get_is_read(self):
        return self.is_read

    def read(self):
        self.is_read = True

    def get_publisher(self):
        return self.publisher



#create the GUI interface
class GUI:

    def __init__(self):

        # similar to root in other texts
        window = Tk()
        window.title("Data Entry Screen")
        #setting root window and size
        window.minsize(width=250, height=200)

        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all books entered via the gui
        self.recordlist = []

        #creating label and field variable in GUI for each entry field
        name_label = Label(window, text='Enter Title:')
        name_label.grid(row = 1, column = 1)
        self.name_field = Entry(window)
        self.name_field.grid(row = 2, column = 1)

        author_label = Label(window, text='Enter author:')
        author_label.grid(row = 3, column = 1)
        self.author_field = Entry(window)
        self.author_field.grid(row = 4, column = 1)

        isbn_label = Label(window, text='Enter isbn:')
        isbn_label.grid(row = 5, column = 1)
        self.isbn_field = Entry(window)
        self.isbn_field.grid(row = 6, column = 1)

        publisher_label = Label(window, text='Enter publisher:')
        publisher_label.grid(row = 7, column = 1)
        self.publisher_field = Entry(window)
        self.publisher_field.grid(row = 8, column = 1)

        #buttons
        button_label = Label(window, text='Press to validate:')
        button_label.grid(row = 5, column = 2)
        button = Button(window, text='Submit', command=self.doSubmit)
        button.grid(row = 6, column = 2)

        button_label1 = Label(window, text='Convert Record to csv')
        button_label1.grid(row = 7, column = 2)
        button1 = Button(window, text='write to csv', command=self.writetocsv)
        button1.grid(row = 8, column = 2)

        #waiting for user input - event driven program
        window.mainloop()


    def doSubmit(self):
        #this is the callback method for the 'Submit' button
        if len(self.name_field.get()) <1 or len(self.author_field.get()) <1 or len(self.isbn_field.get()) <1 or len(self.publisher_field.get()) <1:
            tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
        else:
            try:
                validated_isbn = int(self.isbn_field.get())
                self.recordlist.append(Book(self.name_field.get(),self.author_field.get(), self.isbn_field.get(), self.publisher_field.get()))
                self.ready_to_write= True
                tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                self.author_field.delete(0, END) #command to clear field
                self.name_field.delete(0, END)
                self.isbn_field.delete(0, END)
                self.publisher_field.delete(0, END)
            except:
                tkinter.messagebox.showwarning('Warning!','Please enter numeric isbn code')
                print('Please enter numeric isbn code')


    def writetocsv(self):
        #this is the callback method for the 'write to csv' button
        import csv
        file_name = 'books.csv'

        if self.ready_to_write: #cheacks data has been previously validated
            ofile = open('C:/Users/Flo/Dropbox/Documents/Portable Python 3.2.1.1/App/'+file_name, 'a') #open with write('w') or append('a') privelages
            writer = csv.writer(ofile, delimiter=',', lineterminator = '\n')
            #cycles through list of records created by gui
            for record in self.recordlist:
                print(record.get_title())
                writer.writerow([record.get_title(),record.get_author(), record.get_isbn(), record.get_is_read(), record.get_publisher()])
            #explicitly closes the output file
            ofile.close()
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

def main():
    pass

if __name__ == '__main__':
    main()

#initialises the programme
GUI()
