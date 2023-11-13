import pandas as pd

def team_results(team):

    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    df = df[df['Team'].isin(team)]

    won = df['Result'].value_counts()['Won']
    lost = df['Result'].value_counts()['Lost']

    if 'No Result' in df['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }

    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

def toss_wins(team):

    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    df = df[df['Team'].isin(team)]

    won = df['Toss'].value_counts()['Won']
    lost = df['Toss'].value_counts()['Lost']


    df_dict = {'Team': [str_team, str_team],
               'Result': ['Won', 'Lost'],
               'Count': [won, lost],
               }

    df2 = pd.DataFrame.from_dict(df_dict)

    return df2


def results_batting_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    set_target = ['Set Target']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(set_target)]
    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    if 'No Result' in df1['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df3 = pd.DataFrame.from_dict(df_dict)

    return df3


def results_bowling_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    chase = ['Chase']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(chase)]
    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    if 'No Result' in df1['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df4 = pd.DataFrame.from_dict(df_dict)

    return df4


def results_winning_toss_and_chasing(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    chase = ['Chase']
    toss = ['Won']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    df1 = df1[df1['Action'].isin(chase)]

    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    if 'No Result' in df1['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def results_winning_toss_and_defending(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    defend = ['Set Target']
    toss = ['Won']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    df1 = df1[df1['Action'].isin(defend)]

    won = df1['Result'].value_counts()['Won']

    if 'Lost' in df1['Result'].values:
        lost = df1['Result'].value_counts()['Lost']
    else:
        lost = 0

    if 'No Result' in df1['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def results_losing_toss_and_chasing(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    chase = ['Chase']
    toss = ['Lost']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    df1 = df1[df1['Action'].isin(chase)]

    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    if 'No Result' in df1['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def results_losing_toss_and_defending(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    defend = ['Set Target']
    toss = ['Lost']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    df1 = df1[df1['Action'].isin(defend)]

    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    if 'No Result' in df1['Result'].values:
        no_r = df['Result'].value_counts()['No Result']
    else:
        no_r = 0

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def action_after_toss_won(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    toss = ['Won']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    # df1 = df1[df1['Action'].isin(defend)]

    won = df1['Action'].value_counts()['Chase']

    lost = df1['Action'].value_counts()['Set Target']

    df_dict = {'Team': [str_team, str_team],
               'Action': ['Chase', 'Set Target'],
               'Count': [won, lost],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def action_after_toss_lost(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    toss = ['Lost']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    # df1 = df1[df1['Action'].isin(defend)]

    won = df1['Action'].value_counts()['Chase']

    lost = df1['Action'].value_counts()['Set Target']

    df_dict = {'Team': [str_team, str_team],
               'Action': ['Chase', 'Set Target'],
               'Count': [won, lost],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def toss_won_result(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    toss = ['Won']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    # df1 = df1[df1['Action'].isin(defend)]

    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    df_dict = {'Team': [str_team, str_team],
               'Result': ['Won', 'Lost'],
               'Count': [won, lost],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def toss_lost_result(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    toss = ['Lost']

    df = df[df['Team'].isin(team)]

    df1 = df[df['Toss'].isin(toss)]
    # df1 = df1[df1['Action'].isin(defend)]

    won = df1['Result'].value_counts()['Won']

    lost = df1['Result'].value_counts()['Lost']

    df_dict = {'Team': [str_team, str_team],
               'Result': ['Won', 'Lost'],
               'Count': [won, lost],
               }
    df = pd.DataFrame.from_dict(df_dict)

    return df


def runs_batting_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    action = ['Set Target']

    df = df[df['Team'].isin(team)]
    df1 = df[df['Action'].isin(action)]
    df1 = df1.sort_values(by=['Runs Scored'], ascending=False)

    return df1


def runs_batting_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    action = ['Chase']

    df = df[df['Team'].isin(team)]
    df1 = df[df['Action'].isin(action)]
    df1 = df1.sort_values(by=['Runs Scored'], ascending=False)

    return df1


def wickets_taken_bowling_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    action = ['Chase']

    df = df[df['Team'].isin(team)]
    df1 = df[df['Action'].isin(action)]
    df1 = df1.sort_values(by=['Wickets Taken'], ascending=False)

    return df1


def wickets_taken_bowling_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [team]

    action = ['Set Target']

    df = df[df['Team'].isin(team)]
    df1 = df[df['Action'].isin(action)]
    df1 = df1.sort_values(by=['Wickets Taken'], ascending=False)

    return df1

