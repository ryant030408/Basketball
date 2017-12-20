import tkinter as tk
import sys
from tkinter.filedialog import asksaveasfilename
from PIL import Image
from nba_py import player
import pandas as pd

# adds menu to tkinter pane
class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=file_menu)
        file_menu.add_command(label="Exit", underline=1, command=self.quit)
        file_menu.add_command(label="Save Graph", underline=2, command=self.save)
        file_menu.add_command(label="Update Players", underline=3, command=self.update_master_player_list)

    # quits
    def quit(self):
        sys.exit(0)
    # lets user save graph
    def save(self):
        f = asksaveasfilename(defaultextension='.jpg')
        img = Image.open('testplot.jpg')
        try:
            img.save(f)
            print(f)
        except:
            print('SAVE ERROR')
    # updates list of all players past and current
    def update_master_player_list(self):
        try:
            players_old = pd.read_pickle('player_lists/master.pckl')
            players_new = player.PlayerList(league_id='00', season='2017-18', only_current=0).info()
            if (players_old != players_old):
                players_new.to_pickle('player_lists/master.pckl')
        except FileNotFoundError:
            players = player.PlayerList(league_id='00', season='2017-18', only_current=0)
            players = players.info()
            players.to_pickle('player_lists/master.pckl')

