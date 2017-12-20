import pandas as pd

def game_id_maker(num, season):
    return str('00' + str(season) + '0' + str(num).zfill(4))

def fix_ref_game_id(dframe):
    for index, row in dframe.iterrows():
        game_counter = row['GAME_ID']
        id = game_id_maker(game_counter, 216)
        # print(id)
        dframe.set_value(index, 'GAME_ID', id)
    return dframe

# for if you just have the game.officials() data
def add_game_id_refs(location_of_pickle):
    data = pd.read_pickle(location_of_pickle)# load pickle
    data['INDEX'] = range(1, len(data) + 1)# new index
    data['GAME_ID'] = 0# adds game id
    game_counter = 0 # counter of game ids

    # sets ref numbers to own column
    data.set_value(0, 'REF_NUM', 0)
    data.set_value(1, 'REF_NUM', 1)
    data.set_value(2, 'REF_NUM', 2)

    #rename index
    data = data.set_index('INDEX')


    for index, row in data.iterrows():
        if (row['REF_NUM'] == 0.0):
            game_counter += 1

        data.set_value(index, 'GAME_ID', game_counter)

        # print(row)
    return data

# returns dataframe with code and year
# CODES
# 1: Jumpshot
# 2: Miss
# 3: Free Throw
# 4: Rebound
# 5: Steal/Turnover
# 6: Foul
# 7: Game Violation
# 8: Sub
# 9: Timeout
# 10: Jumpball
# 11: Technical/Ejection
# 12: Start of Quarter
# 13: End of Quarter
#
def search_for_pbyp(code, path_to_pckl, name=None, games=None):
    if(code <= 1 & code >= 13):
        raise ValueError("Code must be between 1 and 13")
    data = pd.read_pickle(path_to_pckl)
    data = data[data['EVENTMSGTYPE'] == code]

    if(name != None):
        data = data[(data['VISITORDESCRIPTION'].str.contains(name) == True)
                    | (data['HOMEDESCRIPTION'].str.contains(name) == True)]
    if (games != None):
        data = data[data['GAME_ID'].isin(games)]

    return data





thing = pd.read_pickle('refs/refs_for_216.pckl')
print(thing.head())
thing2 = fix_ref_game_id(thing)
print(thing2.head())
