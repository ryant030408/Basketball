import pandas as pd
from nba_py import game, player, team
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import graph_gui_functions as gf

# gui
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # window specs
        self.minsize(900, 400)

        # title
        self.title('Downloader')

        #------------------------------------

        # frame for year
        self.year_frame = Frame(self)

        # year drop down
        self. yearVar = StringVar()
        self.year_combobox = ttk.Combobox(self.year_frame, values=gf.year_creator(), textvariable=self.yearVar)
        self.year_combobox.pack()

        # add year drop down to gui
        self.year_frame.grid(row=0, column=0)

        #------------------------------------




app = App()
app.mainloop()