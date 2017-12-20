import pandas as pd
from matplotlib import pyplot as plt
from PIL import ImageTk, Image
from nba_py import player, team
import graph_gui_functions as gf
import tkinter as tk
import numpy

# clears stats
def clear_tots(self):
    self.season_tots_stats = []

# sums stat for total
def get_stat(data):
    return(data.sum())

# finds which item to search for, team or player
def which_to_search(self, num):
    if(num == 1):
        graph_team_totals(self)
    else:
        graph_player_year_tots(self)

# graph player data
def graph_player_year_tots(self):
    player = self.players_c.get()
    stat = self.stats_c.get()
    if(self.current_stat == None):
        self.current_stat = stat
    elif(self.current_stat != stat):
        gf.clear_plot(self)
        clear_tots(self)
        self.current_stat = stat
    year = self.year_to_use.get()
    info = gf.get_player_game_log(player, season=year)
    self.season_tots_stats.append(info)
    gf.clear_plot(self)
    index = 0
    for item in self.season_tots_stats:
        sumstat = get_stat(item[stat])
        colour = numpy.random.rand(3, )
        plt.bar(index, sumstat, color=colour, label=gf.get_player_name(item['Player_ID'].iloc[0]) + ' ' + stat + ' ' + year + ' ' + str(sumstat))
        index = index+1
        self.current_list.insert(tk.END, gf.get_player_name(item['Player_ID'].iloc[0]) + ' ' + stat + ' ' + year + ' ' + str(sumstat))
    plt.grid(True)
    plt.legend()
    plt.savefig('testplot.jpg')
    img = ImageTk.PhotoImage(Image.open('testplot.jpg'))

    self.imageplot.configure(image=img)
    self.imageplot.image = img

# plot team stuff
def graph_team_totals(self):
    team = self.teams_c.get()
    id = gf.get_team_id(team)
    stat = self.stats_c.get()
    if (self.current_stat == None):
        self.current_stat = stat
    elif (self.current_stat != stat):
        gf.clear_plot(self)
        clear_tots(self)
        self.current_stat = stat
    year = self.year_to_use.get()
    info = gf.get_team_game_logs(id, season=year)
    self.season_tots_stats.append(info)
    gf.clear_plot(self)
    index=0
    for item in self.season_tots_stats:
        colour = numpy.random.rand(3, )
        sumstat =  get_stat(item[stat])
        plt.bar(index, sumstat, color=colour, label=gf.team_ids[str(item['Team_ID'].iloc[0])] + ' ' + stat + ' ' + year + ' ' + str(sumstat))
        index = index+1
        self.current_list.insert(tk.END, gf.team_ids[str(item['Team_ID'].iloc[0])] + ' ' + stat + ' ' + year + ' ' + str(sumstat))
    plt.grid(True)
    plt.legend()
    plt.savefig('testplot.jpg')
    img = ImageTk.PhotoImage(Image.open('testplot.jpg'))

    self.imageplot.configure(image=img)
    self.imageplot.image = img



