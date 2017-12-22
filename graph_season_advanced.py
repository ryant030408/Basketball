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
from nba_py import game


# gets player advanced stats
def get_player_adv_logs(player_name, season='2016-17'):
    id = gf.get_player_id(player_name)
    try:
        player_info = pd.read_pickle('player_adv_game_logs/' + str(id) + '-' + season + '.pckl')
    except FileNotFoundError:
        print('File not found')
        player_info = game.BoxscoreAdvanced(id, season=season)
        player_info = player_info.sql_players_advanced()
        player_info.to_pickle('player_adv_game_logs/' + str(id) + '-' + season + '.pckl')
    return player_info


# graph advanced stats
def graph_player_advanced_per_year(self):
    print('yo')


print(get_player_adv_logs('LeBron James'))