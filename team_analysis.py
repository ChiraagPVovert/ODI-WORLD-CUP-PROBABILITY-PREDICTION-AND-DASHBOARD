import pandas as pd

def all_matches_played(team):

    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    df = df[df['COUNTRY'].isin(team)]

    gsm = df['GROUP STAGE MATCHES'].values
    gsm = gsm[0]

    qfp = df['QUARTER FINALS PLAYED'].values
    qfp = qfp[0]

    sfp = df['SEMI FINALS PLAYED'].values
    sfp = sfp[0]

    fp = df['FINALS PLAYED'].values
    fp = fp[0]

    df_dict = {'Team': [str_team, str_team, str_team, str_team],
               'Result': ['Group Stage Matches Played', 'Quarter Finals Played', 'Semi Finals Played', 'Finals Played'],
               'Count': [gsm, qfp, sfp, fp],
               }
    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

def all_matches_results(team):
    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    df = df[df['COUNTRY'].isin(team)]

    won = df['WON'].values
    won = won[0]

    lost = df['LOST'].values
    lost = lost[0]

    no_r = df['TIED/NO-RESULT'].values
    no_r = no_r[0]

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

def group_stage_matches_results(team):
    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    df = df[df['COUNTRY'].isin(team)]

    won = df['GROUP STAGE MATCHES WON'].values
    won = won[0]

    lost = df['GROUP STAGE MATCHES LOST'].values
    lost = lost[0]

    no_r = df['GROUP STAGE MATCHES TIED'].values
    no_r = no_r[0]

    df_dict = {'Team': [str_team, str_team, str_team],
               'Result': ['Won', 'Lost', 'No Result'],
               'Count': [won, lost, no_r],
               }
    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

def qf_results(team):
    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    df = df[df['COUNTRY'].isin(team)]

    won = df['QUARTER FINALS WON'].values
    won = won[0]

    lost = df['QUARTER FINALS LOST'].values
    lost = lost[0]

    df_dict = {'Team': [str_team, str_team],
               'Result': ['Won', 'Lost'],
               'Count': [won, lost],
               }
    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

def sf_results(team):
    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    df = df[df['COUNTRY'].isin(team)]

    won = df['SEMI FINALS WON'].values
    won = won[0]

    lost = df['SEMI FINALS LOST'].values
    lost = lost[0]

    df_dict = {'Team': [str_team, str_team],
               'Result': ['Won', 'Lost'],
               'Count': [won, lost],
               }
    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

def finals_results(team):
    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')

    str_team = team

    team = [team]

    # team = [team]

    df = df[df['COUNTRY'].isin(team)]

    won = df['FINALS WON'].values
    won = won[0]

    lost = df['FINALS LOST'].values
    lost = lost[0]

    df_dict = {'Team': [str_team, str_team],
               'Result': ['Won', 'Lost'],
               'Count': [won, lost],
               }
    df1 = pd.DataFrame.from_dict(df_dict)

    return df1

