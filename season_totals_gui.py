from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import pandas as pd
import graph_gui_functions as gf
import graph_tots_functions as gtf
from tkinter.filedialog import asksaveasfile
from matplotlib import pyplot as plt
import numpy as np


def get_season_tot_gui(self):
    # stat combobox and label
    self.stats_tot_l = tk.Label(self.year_totals, text='Stat')
    self.stats_tot_c = ttk.Combobox(self.year_totals, values=self.player_stat_list, textvariable=self.stat_needed)

    self.stats_tot_l.grid(row=0, column=0)
    self.stats_tot_c.grid(row=0, column=1)

    # search button
    self.search_tot_b = tk.Button(self.year_totals, text='Search',
                              command=lambda: gtf.which_to_search(self, self.player_team_radio_val.get()))
    self.search_tot_b.grid(row=1, column=0, columnspan=2)