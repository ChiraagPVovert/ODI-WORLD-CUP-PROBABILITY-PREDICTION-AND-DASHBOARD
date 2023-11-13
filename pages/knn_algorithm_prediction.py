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
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_excel('All_odi_players_from_2019.xlsx')
df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})


def bat(team):
    df['YEAR'] = pd.DatetimeIndex(df['LATEST_GAME_PLAYED_DATE']).year
    bat_options = ['Batsman', 'WK Batsman']
    batsman_and_wk_df = df[df['ROLE'].isin(bat_options)]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['YEAR'] >= 2022]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['NO_OF_MATCHES_PLAYED'] >= 1]

    x = batsman_and_wk_df[['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE']].values
    y = batsman_and_wk_df[['RECENTLY_PLAYING_IN_ODI']].values

    x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=4)

    y_train = y_train.reshape(y_train.shape[0], )
    y_test = y_test.reshape(y_test.shape[0], )

    train_a = []
    test_a = []
    K = []

    KNN = KNeighborsClassifier(n_neighbors=36)  # dist(x, y) = sqrt(sum((xi - yi)**2))

    KNN.fit(x_train, y_train)

    batsman_and_wk_df = df[df['RECENTLY_PLAYING_IN_ODI'] == 1]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['ROLE'].isin(bat_options)]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['COUNTRY'] == team]
    batsman_and_wk_df = batsman_and_wk_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE']]
    batsman_and_wk_df = batsman_and_wk_df.reset_index(drop=True)

    X_bat = batsman_and_wk_df[['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE']].values
    X_bat = X_bat.astype('float64')
    X_bat = preprocessing.StandardScaler().fit(X_bat).transform(X_bat.astype(float))

    final_bat_predict = KNN.predict_proba(X_bat)
    final_bat_predict_df = pd.DataFrame(final_bat_predict,
                                        columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_bat_predict_df = final_bat_predict_df.reset_index(drop=True)

    final_bat_predict_df = pd.concat([batsman_and_wk_df, final_bat_predict_df], axis=1, join='inner')

    return final_bat_predict_df[['PLAYERS','NO_OF_MATCHES_PLAYED','RUNS','BATTING_AVG','BATTING_STRIKE_RATE','PROBABILITY_OF_PLAYING']].sort_values(by=['PROBABILITY_OF_PLAYING'], ascending=False)


def bowl(team):
    df['YEAR'] = pd.DatetimeIndex(df['LATEST_GAME_PLAYED_DATE']).year
    # df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    bowler_options = ['Bowler']
    bowler_df = df[df['ROLE'].isin(bowler_options)]
    bowler_df = bowler_df[bowler_df['YEAR'] >= 2022]
    bowler_df = bowler_df[bowler_df['NO_OF_MATCHES_PLAYED'] >= 1]
    # print(bowler_df)

    x = bowler_df[['NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    y = bowler_df[['RECENTLY_PLAYING_IN_ODI']].values

    x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=4)

    # print('Train set:', x_train.shape, y_train.shape)
    # print('Test set:', x_test.shape, y_test.shape)

    y_train = y_train.reshape(y_train.shape[0], )
    y_test = y_test.reshape(y_test.shape[0], )

    train_a = []
    test_a = []
    K = []

    KNN = KNeighborsClassifier(n_neighbors=41)  # dist(x, y) = sqrt(sum((xi - yi)**2))

    KNN.fit(x_train, y_train)

    bowler_df = df[df['COUNTRY'] == team]
    bowler_df = bowler_df[bowler_df['RECENTLY_PLAYING_IN_ODI'] == 1]
    bowler_df = bowler_df[bowler_df['ROLE'].isin(bowler_options)]
    bowler_df = bowler_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY']]
    bowler_df = bowler_df.reset_index(drop=True)

    X_bowl = bowler_df[['NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    X_bowl = X_bowl.astype('float64')
    X_bowl = preprocessing.StandardScaler().fit(X_bowl).transform(X_bowl.astype(float))

    final_bowl_predict = KNN.predict_proba(X_bowl)
    final_bowl_predict_df = pd.DataFrame(final_bowl_predict,
                                         columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_bowl_predict_df = final_bowl_predict_df.reset_index(drop=True)

    final_bowl_predict_df = pd.concat([bowler_df, final_bowl_predict_df], axis=1, join='inner')

    return final_bowl_predict_df[['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'WICKETS', 'BOWLING_AVERAGE', 'BOWLING_STRIKE_RATE', 'ECONOMY','PROBABILITY_OF_PLAYING']].sort_values(by=['PROBABILITY_OF_PLAYING'], ascending=False)


def all_round(team):
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

    x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=3)

    y_train = y_train.reshape(y_train.shape[0], )
    y_test = y_test.reshape(y_test.shape[0], )

    train_a = []
    test_a = []
    K = []

    KNN = KNeighborsClassifier(n_neighbors=16)  # dist(x, y) = sqrt(sum((xi - yi)**2))

    KNN.fit(x_train, y_train)

    all_rounder_df = df[df['COUNTRY'] == team]
    all_rounder_df = all_rounder_df[all_rounder_df['RECENTLY_PLAYING_IN_ODI'] == 1]
    all_rounder_df = all_rounder_df[all_rounder_df['ROLE'].isin(all_rounder_options)]
    all_rounder_df = all_rounder_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']]
    all_rounder_df = all_rounder_df.reset_index(drop=True)

    X_all_round = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    X_all_round = X_all_round.astype('float64')
    X_all_round = preprocessing.StandardScaler().fit(X_all_round).transform(X_all_round.astype(float))

    final_all_round_predict = KNN.predict_proba(X_all_round)
    final_all_round_predict = pd.DataFrame(final_all_round_predict,
                                           columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_all_round_predict = final_all_round_predict.reset_index(drop=True)

    final_all_round_predict = pd.concat([all_rounder_df, final_all_round_predict], axis=1, join='inner')

    return final_all_round_predict[
        ['PLAYERS','NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY','PROBABILITY_OF_PLAYING']].sort_values(by=['PROBABILITY_OF_PLAYING'], ascending=False)


# bat_df = bat('INDIA')
# bowl_df = bowl('INDIA')
# all_rounder_df = all_round('INDIA')