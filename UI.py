#!/usr/bin/env python3
from tkinter import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3, os, sys

path = os.path.dirname(sys.argv[0])
os.chdir(path)

class App(Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.pack()

      self.entrythingy = Entry()
      self.entrythingy.pack()

      # here is the application variable
      self.contents = StringVar()
      # set it to some value
      self.contents.set("this is a variable")
      # tell the entry widget to watch this variable
      self.entrythingy["textvariable"] = self.contents

      # and here we get a callback when the user hits return.
      # we will have the program print out the value of the
      # application variable when the user hits return
      self.entrythingy.bind('<Key-Return>', self.print_contents)

   def print_contents(self, event):
      b = ''
      a = self.contents.get()
      for i in a.split(' '):
         b += i + '\n'
      with open('words', 'w+') as w:
         w.write(b)
      if os.name != 'nt':
         os.system('python3 vocabulary_processor.py')
      else:
         os.system('python vocabulary_processor.py')
      print('finished')


root = Tk()
app = App(master=root)
app.mainloop()
