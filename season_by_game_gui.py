from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import pandas as pd
import graph_gui_functions as gf
from tkinter.filedialog import asksaveasfile
from matplotlib import pyplot as plt
import numpy as np


def get_gui(self):
    # stat combobox and label
    self.stats_l = tk.Label(self.game_by_game_by_year, text='Stat')
    self.stats_c = ttk.Combobox(self.game_by_game_by_year, values=self.player_stat_list, textvariable=self.stat_needed)

    self.stats_l.grid(row=0, column=0)
    self.stats_c.grid(row=0, column=1)

    # search button
    self.search_b = tk.Button(self.game_by_game_by_year, text='Search',
                              command=lambda: gf.which_to_search(self, self.player_team_radio_val.get()))
    self.search_b.grid(row=1, column=0, columnspan=2)
