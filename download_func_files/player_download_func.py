import pandas as pd
from nba_py import player
import os.path
import pickle


# checks if file path is an actual file
def check_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False


# is in form pre dataframe
def stat_downloader(stat, player_id, per_mode='PerGame', season='2016-17'):
    stat_to_get = eval('player.' + stat + '(' + str(player_id) + ', season="' + season + '")')
    c_path = 'player/' + stat + '/' + str(player_id) + season + '.pickle'
    if not os.path.exists('player/' + stat):
        os.makedirs('player/' + stat)
    if (check_file(c_path)):
        print('Found ' + stat + ' for ' + str(player_id))
        return pickle.load( open( c_path, "rb" ) )
    else:
        print('Downloading ' + stat + ' for ' + str(player_id))
        p_c = stat_to_get
        pickle_out = open(c_path, "wb")
        pickle.dump(p_c, pickle_out)
        pickle_out.close()
        return p_c



stat_downloader("PlayerGameLogs", 2544, season='2015-16')