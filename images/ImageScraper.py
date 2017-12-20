import sqlite3
import urllib.request

import os

site =  'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/'
def player_image(player_id):
    player_image_name = str(player_id) + '.png'
    pic = urllib.request.urlretrieve(site + player_image_name, player_image_name)

# DB STUFF
sqlite_file = '../BasketballRoasterMaker/db_for_bb_gm.db'

# Connecting to the database file
conn = sqlite3.connect(os.path.expanduser('~/Documents/Github/BasketballRoasterMaker/db_for_bb_gm.db'))
c = conn.cursor()

sql = "SELECT player_id FROM players WHERE player_id > 0"

c.execute(sql)
ids = c.fetchall()
conn.close()
counter = 1
for id in ids:
    print(counter)
    counter = counter+1
    try:
        player_image(id[0])
    except:
        pass