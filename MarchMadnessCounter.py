#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 09:01:36 2021

@author: willscott
"""

import pandas as pd

r_data = pd.read_csv('results.csv')
r_df = pd.DataFrame(r_data)

rounds = r_df.columns[1:]
cols = rounds

players = ['Will']

player_picks = {}

for i in players:
    data = pd.read_csv(f'{i} picks.csv')
    df = pd.DataFrame(data)
    player_picks[i] = {}
    player_picks[i]['df'] = df
    
def cleanList(l):
    l = [x for x in l if x == x]
    return(l)
    
def score(player_df):
    
    score = 0

    for i in range(0,len(cols)):
        p = (2**i)/2
        col = cols[i]
        picks = player_df[col].tolist()
        results = r_df[col].tolist()
        
        calls = sum(x in results for x in picks if x == x)
        
        points = p * calls
        score += points
        
    return(score)

for i in players:
    p_df = player_picks[i]['df'] 
    s = score(p_df)
    print(f'{i}: {s}')

