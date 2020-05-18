# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:04:44 2020

@author: Kumar
"""

import pandas as pd
match_file = "C:\\Users\\AKSHANSH\\.spyder-py3\\Work files\\IPL\\Data\\matches.csv"
match_df=pd.read_csv(match_file)

#How many matches we’ve got in the dataset?
print("total number of matches:\n",match_df['id'].max())

#How many seasons we’ve got in the dataset?
print("total number of matches:\n",match_df['season'].unique())

#Which Team had won by maximum runs?
match_df[['win_by_runs', 'winner']][match_df.win_by_runs == match_df.win_by_runs.max()]

#Which Team had won by maximum wickets?
match_df[['win_by_wickets', 'winner']]\
    [match_df.win_by_wickets == match_df.win_by_wickets.max()]
    
#Which Team had won by (closest margin) minimum runs?    
match_df[['win_by_runs', 'winner']][match_df.win_by_runs == match_df.win_by_runs.min()]    

#Which Team had won by minimum wickets?
match_df[['win_by_wickets', 'winner']]\
    [match_df.win_by_wickets == match_df.win_by_wickets.max()]
    
#Which season had most number of matches?
match_df.groupby('season').size().nlargest(1)   

#Which IPL Team is more successful?
match_df.groupby('winner').size().nlargest(1)

#Has Toss-winning helped in winning matches?
ss = match_df['toss_winner'] == match_df['winner']
ss.groupby(ss).size()