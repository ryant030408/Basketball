from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import pandas as pd
import graph_gui_functions as gf
import season_by_game_gui as sesg
import season_totals_gui as sestg
import menu_funcs as mf
import top_of_gui as tog
from tkinter.filedialog import asksaveasfile
from matplotlib import pyplot as plt
import numpy as np




# tkinter frame for gui
class BasketballViewer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)



        # combo state
        dis = 'disabled'
        en = 'enabled'

        # graph specs
        self.y_ticks = 10
        self.x_ticks = 10


        # stats to pull
        self.player_stat_list = ['MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                                 'OREB', 'DREB','REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS']
        self.team_stat_list = ['FGM', 'FGA','FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB',
                               'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

        # for side piece
        self.current_list = []

        # current stat
        self.current_stat = NONE

        # for bar chart totals stats
        self.season_tots_stats = []

        # window specs
        self.minsize(900, 400)

        # add menu
        self.menu_bar = mf.MenuBar(self)
        self.config(menu=self.menu_bar)


        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open('testplot.jpg'))

        # title
        self.title('Basketball')

        # create notebook
        self.nBook = ttk.Notebook(self)
        self.game_by_game_by_year = ttk.Frame(self.nBook)
        self.year_totals = ttk.Frame(self.nBook)
        self.nBook.add(self.game_by_game_by_year, text='Game Logs')
        self.nBook.add(self.year_totals, text='Season Totals')

        # constant vars
        self.player_name = StringVar()
        self.stat_needed = StringVar()
        self.team_name = StringVar()
        self.year_to_use = StringVar()
        self.player_team_radio_val = tk.IntVar()

        # top gui container
        self.top_frame = ttk.LabelFrame(self, text='Global Options')

        tog.get_top_gui(self)  # sets up top row of gui
        sesg.get_gui(self) # sets up gui items for per game
        sestg.get_season_tot_gui(self) # sets up season totals gui

        # widgets


        # graph container
        self.graph_lf = ttk.LabelFrame(self, text='Graph')
        self.imageplot = tk.Label(self.graph_lf, image=img)

        # list of in use items
        self.current_list = tk.Listbox(self)

        # save so map shows outside of function
        self.imageplot.image = img

        # pack
        self.top_frame.grid(row=0, column=0)

        self.nBook.grid(row=1, column=0, columnspan=5)


        self.current_list.grid(row=0, column=5, rowspan=3)

        self.graph_lf.grid(pady=1, padx=1, row=5, columnspan=20)
        self.imageplot.pack()
        # self.nBook.grid(row=6, column=0)

        # bind func to year combobox to update years players
        self.years_c.bind("<<ComboboxSelected>>", lambda _ : gf.update_players_year_change(self))





app = BasketballViewer()
app.mainloop()