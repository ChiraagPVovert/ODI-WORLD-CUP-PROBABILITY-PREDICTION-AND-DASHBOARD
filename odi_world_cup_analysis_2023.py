import pandas as pd


def most_toss_won():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]

    # print(df)

    df1 = df.groupby(['Team'])['Action'].agg('count').reset_index()
    df1.rename(columns={'Action': 'Most Toss Won'}, inplace=True)
    df1 = df1.sort_values('Most Toss Won', ascending=False)

    return df1


def most_toss_lost():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]

    # print(df)

    df1 = df.groupby(['Team'])['Action'].agg('count').reset_index()
    df1.rename(columns={'Action': 'Most Toss Lost'}, inplace=True)
    df1 = df1.sort_values('Most Toss Lost', ascending=False)

    return df1


def most_matches_won():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most Matches Won'}, inplace=True)
    df1 = df1.sort_values('Most Matches Won', ascending=False)

    return df1


def most_matches_lost():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most Matches Lost'}, inplace=True)
    df1 = df1.sort_values('Most Matches Lost', ascending=False)

    return df1


def most_won_toss_choose_chase():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    df = df[df['Toss'].isin(toss)]

    # print(df)

    df1 = df.groupby(['Team'])['Action'].agg('count').reset_index()
    df1.rename(columns={'Action': 'Total times choose to chase winning the toss'}, inplace=True)
    df1 = df1.sort_values('Total times choose to chase winning the toss', ascending=False)

    return df1


def most_lost_toss_option_chase():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    df = df[df['Toss'].isin(toss)]

    # print(df)

    df1 = df.groupby(['Team'])['Action'].agg('count').reset_index()
    df1.rename(columns={'Action': 'Total times set to chase losing the toss'}, inplace=True)
    df1 = df1.sort_values('Total times set to chase losing the toss', ascending=False)

    return df1


def most_won_toss_choose_set_target():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    df = df[df['Toss'].isin(toss)]

    # print(df)

    df1 = df.groupby(['Team'])['Action'].agg('count').reset_index()
    df1.rename(columns={'Action': 'Total times choose to set target winning the toss'}, inplace=True)
    df1 = df1.sort_values('Total times choose to set target winning the toss', ascending=False)

    return df1


def most_lost_toss_option_set_target():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    df = df[df['Toss'].isin(toss)]

    # print(df)

    df1 = df.groupby(['Team'])['Action'].agg('count').reset_index()
    df1.rename(columns={'Action': 'Total times set to set target losing the toss'}, inplace=True)
    df1 = df1.sort_values('Total times set to set target losing the toss', ascending=False)

    return df1


def most_matches_won_after_winning_the_toss():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches won after winning the toss'}, inplace=True)
    df1 = df1.sort_values('Most matches won after winning the toss', ascending=False)

    return df1


def most_matches_won_after_losing_the_toss():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches won after losing the toss'}, inplace=True)
    df1 = df1.sort_values('Most matches won after losing the toss', ascending=False)

    return df1


def most_matches_lost_after_winning_the_toss():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches lost after winnnig the toss'}, inplace=True)
    df1 = df1.sort_values('Most matches lost after winnnig the toss', ascending=False)

    return df1


def most_matches_lost_after_losing_the_toss():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches lost after losing the toss'}, inplace=True)
    df1 = df1.sort_values('Most matches lost after losing the toss', ascending=False)

    return df1


def most_matches_won_after_winning_the_toss_and_chasing():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Chase']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches won after winning the toss and chasing'}, inplace=True)
    df1 = df1.sort_values('Most matches won after winning the toss and chasing', ascending=False)

    return df1


def most_matches_won_after_winning_the_toss_and_set_target():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Set Target']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches won after winning the toss and setting target'}, inplace=True)
    df1 = df1.sort_values('Most matches won after winning the toss and setting target', ascending=False)

    return df1


def most_matches_won_after_losing_the_toss_and_chasing():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Chase']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches won after losing the toss and chasing'}, inplace=True)
    df1 = df1.sort_values('Most matches won after losing the toss and chasing', ascending=False)

    return df1


def most_matches_won_after_losing_the_toss_and_set_target():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Set Target']
    result = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches won after losing the toss and setting target'}, inplace=True)
    df1 = df1.sort_values('Most matches won after losing the toss and setting target', ascending=False)

    return df1


def most_matches_lost_after_winning_the_toss_and_chasing():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Chase']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches lost after winning the toss and chasing'}, inplace=True)
    df1 = df1.sort_values('Most matches lost after winning the toss and chasing', ascending=False)

    return df1


def most_matches_lost_after_winning_the_toss_and_set_target():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Set Target']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches lost after winning the toss and setting target'}, inplace=True)
    df1 = df1.sort_values('Most matches lost after winning the toss and setting target', ascending=False)

    return df1


def most_matches_lost_after_losing_the_toss_and_chasing():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Chase']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches lost after losing the toss and chasing'}, inplace=True)
    df1 = df1.sort_values('Most matches lost after losing the toss and chasing', ascending=False)

    return df1


def most_matches_lost_after_losing_the_toss_and_set_target():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Set Target']
    result = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    df = df[df['Result'].isin(result)]

    # print(df)

    df1 = df.groupby(['Team'])['Result'].agg('count').reset_index()
    df1.rename(columns={'Result': 'Most matches lost after losing the toss and setting target'}, inplace=True)
    df1 = df1.sort_values('Most matches lost after losing the toss and setting target', ascending=False)

    return df1


def most_runs_scored_batting_first():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Runs Scored', 'Match']]

    # print(df)

    df1 = df.sort_values('Runs Scored', ascending=False)

    return df1


def most_runs_scored_batting_second():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Runs Scored', 'Match']]

    # print(df)

    df1 = df.sort_values('Runs Scored', ascending=False)

    return df1


def most_runs_scored_winning_toss_batting_first():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Runs Scored', 'Match']]

    # print(df)

    df1 = df.sort_values('Runs Scored', ascending=False)

    return df1


def most_runs_scored_winning_toss_batting_second():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Runs Scored', 'Match']]

    # print(df)

    df1 = df.sort_values('Runs Scored', ascending=False)

    return df1


def most_runs_scored_losing_toss_batting_first():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Runs Scored', 'Match']]

    # print(df)

    df1 = df.sort_values('Runs Scored', ascending=False)

    return df1


def most_runs_scored_losing_toss_batting_second():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Runs Scored', 'Match']]

    # print(df)

    df1 = df.sort_values('Runs Scored', ascending=False)

    return df1


def most_wickets_taken_bowling_first():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Wickets Taken', 'Match']]

    # print(df)

    df1 = df.sort_values('Wickets Taken', ascending=False)

    return df1


def most_wickets_taken_bowling_second():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Wickets Taken', 'Match']]

    # print(df)

    df1 = df.sort_values('Wickets Taken', ascending=False)

    return df1


def most_wickets_taken_wining_toss_bowling_first():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Wickets Taken', 'Match']]

    # print(df)

    df1 = df.sort_values('Wickets Taken', ascending=False)

    return df1


def most_wickets_taken_wining_toss_bowling_second():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Won']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Wickets Taken', 'Match']]

    # print(df)

    df1 = df.sort_values('Wickets Taken', ascending=False)

    return df1


def most_wickets_taken_losing_toss_bowling_first():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Wickets Taken', 'Match']]

    # print(df)

    df1 = df.sort_values('Wickets Taken', ascending=False)

    return df1


def most_wickets_taken_losing_toss_bowling_second():
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    toss = ['Lost']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]

    df = df[['Team', 'Wickets Taken', 'Match']]

    # print(df)

    df1 = df.sort_values('Wickets Taken', ascending=False)

    return df1

def avg_runs_bat_first():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Runs Scored']]
    
    df = df.groupby('Team')['Runs Scored'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Runs Scored': 'Average Runs'})
    df = df.round({"Average Runs":0}) 
    df = df.sort_values('Average Runs',ascending=False)

    return df


def avg_runs_bat_second():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Runs Scored']]
    
    df = df.groupby('Team')['Runs Scored'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Runs Scored': 'Average Runs'})
    df = df.round({"Average Runs":0}) 
    df = df.sort_values('Average Runs',ascending=False)

    return df

def avg_runs_win_toss_bat_first():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Runs Scored']]
    
    df = df.groupby('Team')['Runs Scored'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Runs Scored': 'Average Runs'})
    df = df.round({"Average Runs":0}) 
    df = df.sort_values('Average Runs',ascending=False)

    return df

def avg_runs_win_toss_bat_second():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Runs Scored']]
    
    df = df.groupby('Team')['Runs Scored'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Runs Scored': 'Average Runs'})
    df = df.round({"Average Runs":0}) 
    df = df.sort_values('Average Runs',ascending=False)

    return df

def avg_runs_loss_toss_bat_first():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Runs Scored']]
    
    df = df.groupby('Team')['Runs Scored'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Runs Scored': 'Average Runs'})
    df = df.round({"Average Runs":0}) 
    df = df.sort_values('Average Runs',ascending=False)

    return df

def avg_runs_loss_toss_bat_second():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Runs Scored']]
    
    df = df.groupby('Team')['Runs Scored'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Runs Scored': 'Average Runs'})
    df = df.round({"Average Runs":0}) 
    df = df.sort_values('Average Runs',ascending=False)

    return df

def avg_wickets_bowl_first():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Wickets Taken']]
    
    df = df.groupby('Team')['Wickets Taken'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Wickets Taken': 'Average Wickets'})
    df = df.round({"Average Wickets":0}) 
    df = df.sort_values('Average Wickets',ascending=False)

    return df

def avg_wickets_bowl_second():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Wickets Taken']]
    
    df = df.groupby('Team')['Wickets Taken'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Wickets Taken': 'Average Wickets'})
    df = df.round({"Average Wickets":0}) 
    df = df.sort_values('Average Wickets',ascending=False)

    return df

def avg_wickets_win_toss_bowl_first():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Wickets Taken']]
    
    df = df.groupby('Team')['Wickets Taken'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Wickets Taken': 'Average Wickets'})
    df = df.round({"Average Wickets":0}) 
    df = df.sort_values('Average Wickets',ascending=False)

    return df

def avg_wickets_win_toss_bowl_second():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']
    toss = ['Won']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Wickets Taken']]
    
    df = df.groupby('Team')['Wickets Taken'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Wickets Taken': 'Average Wickets'})
    df = df.round({"Average Wickets":0}) 
    df = df.sort_values('Average Wickets',ascending=False)

    return df

def avg_wickets_loss_toss_bowl_first():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Chase']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Wickets Taken']]
    
    df = df.groupby('Team')['Wickets Taken'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Wickets Taken': 'Average Wickets'})
    df = df.round({"Average Wickets":0}) 
    df = df.sort_values('Average Wickets',ascending=False)

    return df

def avg_wickets_loss_toss_bowl_second():
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    match_type = ['2023 ODI World Cup']
    action = ['Set Target']
    toss = ['Lost']

    df = df[df['Match Type'].isin(match_type)]
    df = df[df['Toss'].isin(toss)]
    df = df[df['Action'].isin(action)]
    
    df = df[['Team','Wickets Taken']]
    
    df = df.groupby('Team')['Wickets Taken'].mean()
    df = df.to_frame().reset_index()
    df = df.rename(columns= {'Wickets Taken': 'Average Wickets'})
    df = df.round({"Average Wickets":0}) 
    df = df.sort_values('Average Wickets',ascending=False)

    return df

