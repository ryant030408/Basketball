class Player:

    def __init__(self, player_id):
        self.player_id = player_id


    # gets players name from id
    def get_name(self):
        import pandas as pd
        try:
            players_list = pd.read_pickle('player_lists/master.pckl')
            player = players_list[players_list['PERSON_ID'] == self.player_id]
            return (player['DISPLAY_FIRST_LAST'].iloc[0])
        except FileNotFoundError as e:
            print('File not found: ')
            print(e)
        except:
            print('Failed to load player name')

    # get player image
    def get_player_image(self):
        from pathlib import Path

        player_picture = Path('images/' + str(self.player_id) + '.png')
        if(player_picture.exists()):
            return player_picture
        else:
            raise Exception('Picture does not exist')

    # def get game logs for a season
    def get_game_logs(self, season='2016-17', reg_season=True):
        import pandas as pd

        try:
            if(reg_season == True):
                player_info = pd.read_pickle('player_game_logs/' + str(self.player_id) + '-' + season + '.pckl')
            else:
                player_info = pd.read_pickle('player_game_logs/' + str(self.player_id) + '-' + season + 'p.pckl')
            return player_info
        except FileNotFoundError:
            from nba_py import player
            print('File not found while retrieving game logs, retrieving now...')
            if(reg_season == True):
                player_info = player.PlayerGameLogs(self.player_id, season=season)
                player_info = player_info.info()
                player_info.to_pickle('player_game_logs/' + str(self.player_id) + '-' + season + '.pckl')
            else:
                player_info = player.PlayerGameLogs(self.player_id, season=season, season_type='Playoffs')
                player_info = player_info.info()
                player_info.to_pickle('player_game_logs/' + str(self.player_id) + '-' + season + 'p.pckl')
            return player_info





p = Player(2544)
print(p.get_name())
print(p.get_player_image())
print(p.get_game_logs())