# %%
# Python Script to Play Bonken or Bonkie Bonkie.
# Bonken is a famous game invented in the Oort Canal and 
# popularized by Dr. M.H.M. (Smartie) Heemskerk.
# Rules: https://staff.fnwi.uva.nl/m.h.m.heemskerk/
#
# Author: Dr. Kaustubh Hakim (c) 2020

import numpy as np
import pandas as pd

# %%
# Players
print('\nWelcome to the world of Bonkie Bonkie! \nFirst rule: Ensure that there is a candle on the table.')
input('Second rule: Wait! Is there a candle on the table. If yes, type y: ')
print('\nGo to the following website to download all rules.')
print('https://staff.fnwi.uva.nl/m.h.m.heemskerk/')
print('\nDo you think you are smarter than Smartie? Let\'s find out ...')
while True:
    try:
        player_A = input('Who has the 7 of spade? ')
        if player_A != '':
            break
    except ValueError:
        continue
while True:
    try:
        player_B = input('Enter name of the player sitting to the left of ' + player_A + ': ')
        if player_B != '':
            break
    except ValueError:
        continue
while True:
    try:
        player_C = input('Enter name of the player sitting to the left of ' + player_B + ': ')
        if player_C != '':
            break
    except ValueError:
        continue
while True:
    try:
        player_D = input('Enter name of the player sitting to the left of ' + player_C + ': ')
        if player_D != '':
            break
    except ValueError:
        continue

players = np.array([player_A, player_B, player_C, player_D])

# %%
# Enter Data
all_games = dict([('p1','Trump of Spades'),('p2','Trump of Hearts'),('p3','Trump of Clubs'),
                  ('p4','Trump of Diamonds'),('p5','No Trump'),('n1','Points of Hearts'),
                  ('n2','King of Hearts'),('n3','Kings and Jacks'),('n4','Queens'),('n5','Domino'),
                  ('n6','Duck'),('n7','7th and 13th Trick'),('n8','Last Trick')])

all_pos_games = np.array([
    dict([('p1','Trump of Spades'),('p2','Trump of Hearts'),('p3','Trump of Clubs'),('p4','Trump of Diamonds'),
          ('p5','No Trump')]),
    dict([('p1','Trump of Spades'),('p2','Trump of Hearts'),('p3','Trump of Clubs'),('p4','Trump of Diamonds'),
          ('p5','No Trump')]),
    dict([('p1','Trump of Spades'),('p2','Trump of Hearts'),('p3','Trump of Clubs'),('p4','Trump of Diamonds'),
          ('p5','No Trump')]),
    dict([('p1','Trump of Spades'),('p2','Trump of Hearts'),('p3','Trump of Clubs'),('p4','Trump of Diamonds'),
          ('p5','No Trump')])])

all_neg_games = np.array([
    dict([('n1','Points of Hearts'),('n2','King of Hearts'),('n3','Kings and Jacks'),('n4','Queens'),
          ('n5','Domino'),('n6','Duck'),('n7','7th and 13th Trick'),('n8','Last Trick')]),
    dict([('n1','Points of Hearts'),('n2','King of Hearts'),('n3','Kings and Jacks'),('n4','Queens'),
          ('n5','Domino'),('n6','Duck'),('n7','7th and 13th Trick'),('n8','Last Trick')]),
    dict([('n1','Points of Hearts'),('n2','King of Hearts'),('n3','Kings and Jacks'),('n4','Queens'),
          ('n5','Domino'),('n6','Duck'),('n7','7th and 13th Trick'),('n8','Last Trick')]),
    dict([('n1','Points of Hearts'),('n2','King of Hearts'),('n3','Kings and Jacks'),('n4','Queens'),
          ('n5','Domino'),('n6','Duck'),('n7','7th and 13th Trick'),('n8','Last Trick')])])

counter_pos = np.array([1, 1, 1, 1])
counter_neg = np.array([2, 2, 2, 2])

data = {player_A : pd.Series(np.zeros(13), index = all_games.values()),
        player_B : pd.Series(np.zeros(13), index = all_games.values()),
        player_C : pd.Series(np.zeros(13), index = all_games.values()),
        player_D : pd.Series(np.zeros(13), index = all_games.values())} 
df   = pd.DataFrame(data)

# %%
# Run Interactive Bonkie
for i in range(12):
    chooser = i % 4
    bidder  = (i+1) % 4
    dealer  = (i+2) % 4
    leader  = (i+3) % 4
    print('\n\nGames', players[chooser], 'can choose\n')
    if all_pos_games[chooser] != {}:
        for key, value in all_pos_games[chooser].items():
            print(key, ' : ', value)
    if all_neg_games[chooser] != {}:
        for key, value in all_neg_games[chooser].items():
            print(key, ' : ', value)
    while True:
        try:
            game_key = input('\nChoose game (type game key): ')
            available_keys = list(all_pos_games[chooser]) + list(all_neg_games[chooser])
            if game_key in available_keys:
                break
            else:
                print("\nERROR: That is not a valid game key. Try again...")
        except ValueError:
            print("\nERROR: That is not a valid game key. Try again...")
    if 'p' in game_key:
        counter_pos[chooser] = counter_pos[chooser] - 1
        for j in range(4):
            all_pos_games[j].pop(game_key,None)
        if counter_pos[chooser] == 0:
            keys = all_pos_games[chooser].copy().keys()
            for key in keys:
                all_pos_games[chooser].pop(key,None)
        print('\nGame chosen by',players[chooser],'is', all_games[game_key])
    elif 'n' in game_key:
        counter_neg[chooser] = counter_neg[chooser] - 1
        for j in range(4):
            all_neg_games[j].pop(game_key,None)
        if counter_neg[chooser] == 0:
            keys = all_neg_games[chooser].copy().keys()
            for key in keys:
                all_neg_games[chooser].pop(key,None)
        print('\nGame chosen by', players[chooser], 'is', all_games[game_key])
    bid_array = np.zeros((4,4))
    for j in range(3):
        cur_bidder = (bidder + j) % 4
        print('\n', players[cur_bidder], 'is bidding...\n')
        for k in range(4):
            cur_asker  = (bidder + j + k) % 4
            if cur_asker == cur_bidder:
                continue
            verdict = input('Does ' + players[cur_bidder] + ' want to bid against ' \
                            + players[cur_asker] + '? (type y if yes) ')
            if verdict == 'y':
                bid_array[cur_bidder,cur_asker] = 1
    for k in range(4):
        cur_asker = (chooser + k) % 4
        if cur_asker == chooser:
            continue
        if bid_array[cur_asker, chooser] == 1:
            input('\nDoes ' + players[chooser] + ' want to double bid against ' \
                  + players[cur_asker] + '? (type y if yes) ')
            bid_array[chooser, cur_asker] = 1
    
    print('\n', players[leader], 'leads...\n')
    
    points_array = np.zeros(4)
    for j in range(4):
        this_player = (chooser + j) % 4
        while True:
            try:
                value = input('How many points won by ' + players[this_player] + '? ')
                val = int(value)
                break
            except ValueError:
                print("\nERROR: That is not a valid number. Try again...")
        points_array[this_player] = value
    total_points = np.zeros(4)
    for j in range(4):
        this_player1 = (chooser + j) % 4
        this_player2 = (chooser + j + 1) % 4
        this_player3 = (chooser + j + 2) % 4
        this_player4 = (chooser + j + 3) % 4
        total_points[this_player1] = points_array[this_player1] \
        + (points_array[this_player1] - points_array[this_player2]) \
        * (bid_array[this_player1,this_player2] + bid_array[this_player2,this_player1]) \
        + (points_array[this_player1] - points_array[this_player3]) \
        * (bid_array[this_player1,this_player3] + bid_array[this_player3,this_player1]) \
        + (points_array[this_player1] - points_array[this_player4]) \
        * (bid_array[this_player1,this_player4] + bid_array[this_player4,this_player1])
        df.at[all_games[game_key],players[this_player1]] = total_points[this_player1]
    print('\nStandings after Game no.', str(i+1), ':', str(11-i), 'more games to go...\n',
          df.append(df.sum().rename('Total')))
    input('\n\nPress any key to continue...')
    if i != 11:
        print('\n\n', players[leader], 'deals the cards ...')
        
print('\n\nTHE ULTIMATE BONKER IS', df.sum().rename('Total').idxmax(axis='columns'), '\n\n')