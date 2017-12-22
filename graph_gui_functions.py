import pandas as pd
from matplotlib import pyplot as plt
from PIL import ImageTk, Image
from nba_py import player, team
import tkinter as tk
import numpy
import graph_tots_functions as gtf


team_ids = {"1610612737":   "ATL",
            "1610612738":	"BOS",
            "1610612739":	"CLE",
            "1610612740":	"NOP",
            "1610612741":	"CHI",
            "1610612742":	"DAL",
            "1610612743":	"DEN",
            "1610612744":	"GSW",
            "1610612745":	"HOU",
            "1610612746":	"LAC",
            "1610612747":	"LAL",
            "1610612748":	"MIA",
            "1610612749":	"MIL",
            "1610612750":	"MIN",
            "1610612751":	"BKN",
            "1610612752":	"NYK",
            "1610612753":	"ORL",
            "1610612754":	"IND",
            "1610612755":	"PHI",
            "1610612756":	"PHX",
            "1610612757":	"POR",
            "1610612758":	"SAC",
            "1610612759":	"SAS",
            "1610612760":	"OKC",
            "1610612761":	"TOR",
            "1610612762":	"UTA",
            "1610612763":	"MEM",
            "1610612764":	"WAS",
            "1610612765":	"DET",
            "1610612766":	"CHA"}

plt.figure(figsize=(10, 5))


# gets team game log for every game of a given season
def get_team_game_logs(team_id, season='2016-17'):
    try:
        team_info = pd.read_pickle('team_game_logs/' + str(team_id) + '-' + season + '.pckl')
    except FileNotFoundError:
        print('File not found')
        team_info = team.TeamGameLogs(team_id, season=season)
        team_info = team_info.info()
        team_info.to_pickle('team_game_logs/' + str(team_id) + '-' + season + '.pckl')
    return team_info

# get player game logs
def get_player_game_log(player_name, season='2016-17'):
    id = get_player_id(player_name)
    try:
        player_info = pd.read_pickle('player_game_logs/' + str(id) + '-' + season + '.pckl')
    except FileNotFoundError:
        print('File not found')
        player_info = player.PlayerGameLogs(id, season=season)
        player_info = player_info.info()
        player_info.to_pickle('player_game_logs/' + str(id) + '-' + season + '.pckl')
    return player_info

# strip data for stats list
def strip_player_data(data):
    new_data = data.drop(['TEAM_ID', 'GAME_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID',
                      'PLAYER_NAME', 'START_POSITION', 'COMMENT'], axis=1)
    return new_data

# renames columns for stats
def rename_stats(data):
    new_data = data.rename(index=str, columns={"MIN": "Minutes", "DIST": "Distance Traveled"})
    return new_data


def make_player_chart(self):
    player = self.players_c.get()
    stat = self.stats_c.get()
    year = self.year_to_use.get()
    info = get_player_game_log(player, season=self.year_to_use.get())
    colour = numpy.random.rand(3, )
    plt.plot(info[stat], c=colour, label=player + ' ' + stat + ' ' + year)
    plt.grid(True)
    plt.xlabel('Games')
    plt.legend()
    plt.savefig('testplot.jpg')
    img = ImageTk.PhotoImage(Image.open('testplot.jpg'))
    self.current_list.insert(tk.END, player + ' ' + stat + ' ' + year)
    self.imageplot.configure(image=img)
    self.imageplot.image = img

def make_team_chart(self):
    year = self.year_to_use.get()
    team = self.teams_c.get()
    id = get_team_id(team)
    stat = self.stats_c.get()
    info = get_team_game_logs(id, season=year)
    colour = numpy.random.rand(3, )
    plt.plot(info[stat], c=colour, label=team + ' ' + stat + ' ' + year)
    plt.grid(True)
    plt.xlabel('Games')
    plt.legend()
    plt.savefig('testplot.jpg')
    img = ImageTk.PhotoImage(Image.open('testplot.jpg'))
    self.current_list.insert(tk.END, team + ' ' + stat + ' ' + year)
    self.imageplot.configure(image=img)
    self.imageplot.image = img

def clear_plot(self, full=0):
    if(full == 1):
        gtf.clear_tots(self)
    plt.gcf().clear()
    plt.savefig('testplot.jpg')
    img = ImageTk.PhotoImage(Image.open('testplot.jpg'))
    self.current_list.delete(0, tk.END)
    self.imageplot.configure(image=img)
    self.imageplot.image = img

# radio buttons
def selection(self, num):
    # combo state
    dis = 'disabled'
    en = 'enabled'
    if (num == 1):
        self.players_c.configure(state=dis)
        self.teams_c.configure(state=en)
        self.stats_c.configure(values=self.team_stat_list)
    else:
        self.players_c.configure(state=en)
        self.teams_c.configure(state=dis)
        self.stats_c.configure(values=self.player_stat_list)
    clear_plot(self)

# finds which item to search for, team or player
def which_to_search(self, num):
    print(num)
    if(num == 1):
        make_team_chart(self)
    else:
        make_player_chart(self)
# gets team id using dictionary of values
def get_team_id(team_abbr):
    for key, values in team_ids.items():
        if(values == team_abbr):
            return key


# creates array of years in format for nba_py
# TODO add more years
def year_creator():
    yeara = 2017
    yearb = 18
    years = []
    for i in range(0, 10):
        years.append(str(yeara) + '-' + str(yearb).zfill(2))
        yeara = yeara-1
        yearb = yearb-1
    return years

# gets player list for current season selected in year
def get_player_list(self):
    try:
        players = pd.read_pickle('player_lists/' + self.year_to_use.get() + '.pckl')
    except FileNotFoundError:
        players = player.PlayerList(league_id='00', season=self.year_to_use.get(), only_current=0)
        players = players.info()
        players = players[players['ROSTERSTATUS'] == 1]
        players.to_pickle('player_lists/' + self.year_to_use.get() + '.pckl')
    return players

# used when year combobox is clicked
def update_players_year_change(self):
    players = get_player_list(self)
    self.players_c.configure(values=players['DISPLAY_FIRST_LAST'].tolist())

# get player name
def get_player_name(player_id):
    players = pd.read_pickle('player_lists/master.pckl')
    players = players[players['PERSON_ID'] == player_id]
    return(players['DISPLAY_FIRST_LAST'].unique())

# gets players id from master list
def get_player_id(player_name):
    players = pd.read_pickle('player_lists/master.pckl')
    players = players[players['DISPLAY_FIRST_LAST'] == player_name]
    return(int(players['PERSON_ID']))

# returns team abbreviated names
def get_team_abbr():
    return (list(team_ids.values()))

# get team name
def get_team_name(id):
    print('')