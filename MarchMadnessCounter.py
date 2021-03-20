#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 09:01:36 2021

@author: willscott
"""

import pandas as pd
import numpy as np

r_data = pd.read_csv('results.csv')
r_df = pd.DataFrame(r_data)

rounds = r_df.columns[1:]
cols = rounds

players = ['Will','Mamta','Paul']

player_picks = {}

for i in players:
    data = pd.read_csv(f'{i} picks.csv')
    df = pd.DataFrame(data)
    player_picks[i] = {}
    player_picks[i]['df'] = df
    
def cleanList(l):
    l = [x for x in l if x == x]
    return(l)


def baseline(results_df):
    
    score = 0
    
    for i in range(0,len(cols)):
        p = (2**i)/2
        results = cleanList(results_df[cols[i]].tolist())
        points = p * len(results)
        score += points
    
    score = score/2
    
    return(score)
        
    
def score(player_df):
    
    score = 0

    for i in range(0,len(cols)):
        p = (2**i)/2
        col = cols[i]
        picks = cleanList(player_df[col].tolist())
        results = cleanList(r_df[col].tolist())        
        
        calls = sum(x in results for x in picks if x == x)
        
        points = p * calls
        score += points
        
    return(score)

def project(player_df,complete_rounds):
    
    t_df = player_df
    
    for i in range(0,complete_rounds):
        col = cols[i]
        picks = cleanList(t_df[col].tolist())
        results = cleanList(r_df[col].tolist())  
        
        for t in picks:
            if t not in results:
                for r in range(i,len(cols)):
                    t_df[cols[i]] = t_df[cols[i]].replace(t,np.nan)
    
    score = 0
    for i in range(0,len(cols)):
        p = (2**i)/2
        col = cols[i]
        calls = len(cleanList(t_df[col].tolist()))
        points = p * calls
        score += points
    return(score)
        
        
print(baseline(r_df))
for i in players:
    p_df = player_picks[i]['df'] 
    s = score(p_df)
    projection = project(p_df,1)
    print(f'{i}: {s} - {projection}')

