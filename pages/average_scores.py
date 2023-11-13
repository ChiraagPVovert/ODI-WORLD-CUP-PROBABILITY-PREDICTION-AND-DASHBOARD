import pandas as pd

def average_runs_scored_batting_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Set Target'])]

    avg = df1.loc[:, 'Runs Scored'].mean()

    a = 'The average runs scored by ' + str_team + ' batting first is ' + str(int(round(avg, 0)))

    return a


def average_runs_scored_winning_toss_batting_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Set Target'])]
    df1 = df1[df1['Toss'].isin(['Won'])]

    avg = df1.loc[:, 'Runs Scored'].mean()

    a = 'The average runs scored by ' + str_team + ' batting first after winning the toss is ' + str(int(round(avg, 0)))

    return a


def average_runs_scored_losing_toss_batting_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Set Target'])]
    df1 = df1[df1['Toss'].isin(['Lost'])]

    avg = df1.loc[:, 'Runs Scored'].mean()

    a = 'The average runs scored by ' + str_team + ' batting first after losing the toss is ' + str(int(round(avg, 0)))

    return a


def average_runs_scored_batting_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Chase'])]

    avg = df1.loc[:, 'Runs Scored'].mean()

    a = 'The average runs scored by ' + str_team + ' batting second is ' + str(int(round(avg, 0)))

    return a


def average_runs_scored_winning_toss_batting_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Chase'])]
    df1 = df1[df1['Toss'].isin(['Won'])]

    avg = df1.loc[:, 'Runs Scored'].mean()

    a = 'The average runs scored by ' + str_team + ' batting second after winning the toss is ' + str(int(round(avg, 0)))

    return a


def average_runs_scored_losing_toss_batting_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Chase'])]
    df1 = df1[df1['Toss'].isin(['Lost'])]

    avg = df1.loc[:, 'Runs Scored'].mean()

    a = 'The average runs scored by ' + str_team + ' batting second after losing the toss is ' + str(int(round(avg, 0)))

    return a


def average_wickets_taken_bowling_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Set Target'])]

    avg = df1.loc[:, 'Wickets Taken'].mean()

    a = 'The average wickets taken by ' + str_team + ' bowling first is ' + str(int(round(avg, 0)))

    return a


def average_wickets_taken_winning_toss_bowling_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Set Target'])]
    df1 = df1[df1['Toss'].isin(['Won'])]

    avg = df1.loc[:, 'Wickets Taken'].mean()

    a = 'The average wickets taken by ' + str_team + ' bowling first after winning the toss is ' + str(
        int(round(avg, 0)))

    return a


def average_wickets_taken_losing_toss_bowling_first(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Set Target'])]
    df1 = df1[df1['Toss'].isin(['Lost'])]

    avg = df1.loc[:, 'Wickets Taken'].mean()

    a = 'The average wickets taken by ' + str_team + ' bowling first after losing the toss is ' + str(
        int(round(avg, 0)))

    return a


def average_wickets_taken_bowling_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Chase'])]

    avg = df1.loc[:, 'Wickets Taken'].mean()

    a = 'The average wickets taken by ' + str_team + ' bowling second is ' + str(int(round(avg, 0)))

    return a


def average_wickets_taken_winning_toss_bowling_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Chase'])]
    df1 = df1[df1['Toss'].isin(['Won'])]

    avg = df1.loc[:, 'Wickets Taken'].mean()

    a = 'The average wickets taken by ' + str_team + ' bowling second after winning the toss is ' + str(
        int(round(avg, 0)))

    return a


def average_wickets_taken_losing_toss_bowling_second(team):
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    str_team = team

    team = [str_team]

    df = df[df['Team'].isin(team)]

    df1 = df[df['Action'].isin(['Chase'])]
    df1 = df1[df1['Toss'].isin(['Lost'])]

    avg = df1.loc[:, 'Wickets Taken'].mean()

    a = 'The average wickets taken by ' + str_team + ' bowling second after losing the toss is ' + str(
        int(round(avg, 0)))

    return a

