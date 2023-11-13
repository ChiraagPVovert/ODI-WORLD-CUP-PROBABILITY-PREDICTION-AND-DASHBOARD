import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import scatterplot
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def bat(team):

    df = pd.read_excel('All_odi_players_from_2019.xlsx')
    df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    df['YEAR'] = pd.DatetimeIndex(df['LATEST_GAME_PLAYED_DATE']).year
    bat_options = ['Batsman', 'WK Batsman']
    batsman_and_wk_df = df[df['ROLE'].isin(bat_options)]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['YEAR'] >= 2022]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['NO_OF_MATCHES_PLAYED'] >= 1]

    x = batsman_and_wk_df[['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE']].values
    y = batsman_and_wk_df[['RECENTLY_PLAYING_IN_ODI']].values

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            LR = LogisticRegression(random_state=2)

            LR.fit(x_train, y_train)

            test_predict = LR.predict(x_test)

            accuracy = accuracy_score(test_predict, y_test)

            a.append(accuracy)
            randoms.append(j)
            tests.append(i)

    ind = a.index(max(a))
    j = randoms[ind]
    i = tests[ind]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

    y_train = y_train.reshape(y_train.shape[0], )
    y_test = y_test.reshape(y_test.shape[0], )

    LR = LogisticRegression(random_state=2)

    LR.fit(x_train, y_train)

    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['COUNTRY'] == team]
    batsman_and_wk_df = batsman_and_wk_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'RECENTLY_PLAYING_IN_ODI']]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['RECENTLY_PLAYING_IN_ODI'] == 1]
    batsman_and_wk_df = batsman_and_wk_df.reset_index(drop=True)

    X_bat = batsman_and_wk_df[['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE']].values
    X_bat = X_bat.astype('float64')
    # X_bat = preprocessing.StandardScaler().fit(X_bat).transform(X_bat.astype(float))

    final_bat_predict = LR.predict_proba(X_bat)
    final_bat_predict_df = pd.DataFrame(final_bat_predict,
                                        columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_bat_predict_df = final_bat_predict_df.reset_index(drop=True)

    final_bat_predict_df = pd.concat([batsman_and_wk_df, final_bat_predict_df], axis=1, join='inner')

    return final_bat_predict_df[['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE',
                                 'PROBABILITY_OF_PLAYING']].sort_values(by=['PROBABILITY_OF_PLAYING'], ascending=False)


def bowl(team):

    df = pd.read_excel('All_odi_players_from_2019.xlsx')
    df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    df['YEAR'] = pd.DatetimeIndex(df['LATEST_GAME_PLAYED_DATE']).year
    # df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    bowler_options = ['Bowler']
    bowler_df = df[df['ROLE'].isin(bowler_options)]
    bowler_df = bowler_df[bowler_df['YEAR'] >= 2022]
    bowler_df = bowler_df[bowler_df['NO_OF_MATCHES_PLAYED'] >= 1]
    # print(bowler_df)

    x = bowler_df[['NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    y = bowler_df[['RECENTLY_PLAYING_IN_ODI']].values

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            LR = LogisticRegression(random_state=2)

            LR.fit(x_train, y_train)

            test_predict = LR.predict(x_test)

            accuracy = accuracy_score(test_predict, y_test)

            a.append(accuracy)
            randoms.append(j)
            tests.append(i)

    ind = a.index(max(a))
    j = randoms[ind]
    i = tests[ind]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

    y_train = y_train.reshape(y_train.shape[0], )
    y_test = y_test.reshape(y_test.shape[0], )

    LR = LogisticRegression(random_state=2)

    LR.fit(x_train, y_train)

    bowler_df = bowler_df[bowler_df['COUNTRY'] == team]
    bowler_df = bowler_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY',
         'RECENTLY_PLAYING_IN_ODI']]
    bowler_df = bowler_df[bowler_df['RECENTLY_PLAYING_IN_ODI'] == 1]
    bowler_df = bowler_df.reset_index(drop=True)

    X_bowl = bowler_df[['NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    X_bowl = X_bowl.astype('float64')
    # X_bowl = preprocessing.StandardScaler().fit(X_bowl).transform(X_bowl.astype(float))

    final_bowl_predict = LR.predict_proba(X_bowl)
    final_bowl_predict_df = pd.DataFrame(final_bowl_predict,
                                         columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_bowl_predict_df = final_bowl_predict_df.reset_index(drop=True)

    final_bowl_predict_df = pd.concat([bowler_df, final_bowl_predict_df], axis=1, join='inner')

    return final_bowl_predict_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY',
         'PROBABILITY_OF_PLAYING']].sort_values(by=['PROBABILITY_OF_PLAYING'], ascending=False)


def all_round(team):

    df = pd.read_excel('All_odi_players_from_2019.xlsx')
    df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    df['YEAR'] = pd.DatetimeIndex(df['LATEST_GAME_PLAYED_DATE']).year
    # df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    all_rounder_options = ['All Rounder']
    all_rounder_df = df[df['ROLE'].isin(all_rounder_options)]
    all_rounder_df = all_rounder_df[all_rounder_df['YEAR'] >= 2022]
    all_rounder_df = all_rounder_df[all_rounder_df['NO_OF_MATCHES_PLAYED'] >= 1]

    x = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    y = all_rounder_df[['RECENTLY_PLAYING_IN_ODI']].values

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            LR = LogisticRegression(random_state=2,max_iter=1000)

            LR.fit(x_train, y_train)

            test_predict = LR.predict(x_test)

            accuracy = accuracy_score(test_predict, y_test)

            a.append(accuracy)
            randoms.append(j)
            tests.append(i)

    ind = a.index(max(a))
    j = randoms[ind]
    i = tests[ind]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

    y_train = y_train.reshape(y_train.shape[0], )
    y_test = y_test.reshape(y_test.shape[0], )

    LR = LogisticRegression(random_state=2,max_iter=1000)

    LR.fit(x_train, y_train)

    all_rounder_df = all_rounder_df[all_rounder_df['COUNTRY'] == team]
    all_rounder_df = all_rounder_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY', 'RECENTLY_PLAYING_IN_ODI']]
    all_rounder_df = all_rounder_df[all_rounder_df['RECENTLY_PLAYING_IN_ODI'] == 1]
    all_rounder_df = all_rounder_df.reset_index(drop=True)

    X_all_round = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    X_all_round = X_all_round.astype('float64')
    # X_all_round = preprocessing.StandardScaler().fit(X_all_round).transform(X_all_round.astype(float))

    final_all_round_predict = LR.predict_proba(X_all_round)
    final_all_round_predict = pd.DataFrame(final_all_round_predict,
                                           columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_all_round_predict = final_all_round_predict.reset_index(drop=True)

    final_all_round_predict = pd.concat([all_rounder_df, final_all_round_predict], axis=1, join='inner')

    return final_all_round_predict[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY', 'PROBABILITY_OF_PLAYING']].sort_values(by=['PROBABILITY_OF_PLAYING'],
                                                                                  ascending=False)
