import pandas as pd
from nba_py import team
import os.path
import pickle


# checks if file path is an actual file
def check_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

# is in form pre dataframe
def stat_downloader(stat, team_id, season='2016-17'):
    print(season)
    # stat_to_get = eval('team.' + stat + '(' + str(team_id) + ')')
    stat_to_get = eval('team.' + stat + '(' + str(team_id) + ', season="' + season + '")')
    c_path = 'team/' + stat + '/' + str(team_id) + season + '.pickle'
    if not os.path.exists('team/' + stat):
        os.makedirs('team/' + stat)
    if (check_file(c_path)):
        print('Found ' + stat + ' for ' + str(team_id))
        return pickle.load( open( c_path, "rb" ) )
    else:
        print('Downloading ' + stat + ' for ' + str(team_id))
        p_c = stat_to_get
        pickle_out = open(c_path, "wb")
        pickle.dump(p_c, pickle_out)
        pickle_out.close()
        return p_c

