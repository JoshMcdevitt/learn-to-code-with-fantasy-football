# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:24:21 2023

@author: JMcDevitt
"""

import pandas as pd 
from os import path 
import seaborn as sns
from pandas import Series
from utilities import (generate_token, get_sims, LICENSE_KEY, get_players, 
                       OUTPUT_PATH)

#calls from import to get license key
token = generate_token(LICENSE_KEY)['token']

WEEK = 1
SEASON = 2021
NSIMS = 1000
SCORING = {'qb': 'pass6', 'skill': 'ppr', 'dst': 'high'}

team1 = ['jalen-hurts', 'saquon-barkley', 'clyde-edwards-helaire',
         'keenan-allen', 'cooper-kupp', 'dallas-goedert', 'jason-myers',
         'tb-dst']

team2 = ['matthew-stafford', 'christian-mccaffrey', 'antonio-gibson',
        'tyler-lockett', 'justin-jefferson', 'noah-fant', 'matt-gay',
        'gb-dst']
bench = ['darrell-henderson', 'ronald-jones', 'tony-pollard']

valid_players = get_players(token, season=SEASON, week=WEEK, **SCORING)

list(valid_players['fantasymath_id'])[:20]
['patrick-mahomes',
 'lamar-jackson',
 'josh-allen',
 'tom-brady',
 'aaron-rodgers',
 'russell-wilson',
 'jalen-hurts',
 'ryan-tannehill',
 'dak-prescott',
 'matthew-stafford',
 'justin-herbert',
 'matt-ryan',
 'trevor-lawrence',
 'kirk-cousins',
 'joe-burrow',
 'baker-mayfield',
 'sam-darnold',
 'ben-roethlisberger',
 'jameis-winston']

USE_SAVED_DATA = True

#this above uses live data and since its the offseason we will use saved data from csv
if USE_SAVED_DATA:
    valid_players = pd.read_csv(path.join('projects', 'wdis', 'data',
                                          'valid_players.csv'))
else:
    valid_players= get_players(token, season=SEASON, week=WEEK, **SCORING
        )
    #declaring players
players = team1 + team2 + bench

if USE_SAVED_DATA:
    sims = pd.read_csv(path.join('projects', 'wdis', 'data', 'sims.csv'))
else:
    sims = get_sims(token, players, week=WEEK, season=SEASON, nsims=NSIMS,
                    **SCORING)