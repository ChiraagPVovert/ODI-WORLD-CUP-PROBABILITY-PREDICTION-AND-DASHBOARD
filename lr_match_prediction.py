import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

teams_values = {
    'United State of America':0.1,
    'Oman': 0.2,
    'United Arab Emirates':0.3,
    'Scotland': 0.4,
    'Nepal': 0.5,
    'Zimbabwe':0.6,
    'Ireland': 0.7,
    'West Indies':0.8,
    'Netherlands': 0.9,
    'Afghanistan': 1.10,
    'Bangladesh': 1.2,
    'Sri Lanka': 1.3,
    'South Africa': 1.3,
    'England': 1.4,
    'Pakistan': 1.5,
    'New Zealand': 1.6,
    'Australia': 1.7,
    'India': 1.8,
}

teams_values_inverse = {v: k for k, v in teams_values.items()}

toss_values = {
    'Lost': 0,
    'Won': 1
}

toss_values_inverse = {v: k for k, v in toss_values.items()}

action_values = {
    'Set Target': 1,
    'Chase': 1
}

action_vaues_inverse = {v: k for k, v in action_values.items()}

result = {
    'Won': 1,
    'Lost': 0,
}

result_inverse = {v: k for k, v in result.items()}


# teams_values_inverse
# toss_values_inverse
# action_vaues_inverse
# result_inverse

def match_prediction_after_toss(team, toss_r):
    
    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')
    
    #df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]

    results = ['Won', 'Lost']

    df = df[df['Result'].isin(results)]

    df_1 = df[['Team', 'Toss', 'Result']]

    df_1 = df_1.replace({'Team': teams_values})

    df_1 = df_1.replace({'Toss': toss_values})

    df_1 = df_1.replace({'Result': result})

    x = df_1[['Team', 'Toss']].values
    y = df_1[['Result']].values

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            clf = LogisticRegression()

            clf.fit(x_train, y_train)

            test_predict = clf.predict(x_test)

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

    clf = LogisticRegression()

    clf.fit(x_train, y_train)

    team = [team]
    toss_r = [toss_r]

    pred_df = pd.DataFrame()

    pred_df['Team'] = team
    pred_df['Toss'] = toss_r

    pred_df = pred_df.replace({'Team': teams_values})

    pred_df = pred_df.replace({'Toss': toss_values})

    #print(pred_df)

    pred_x = pred_df[['Team', 'Toss']].values

    result_predict_proba = clf.predict_proba(pred_x)
    result_predict = clf.predict(pred_x)

    win_probability = round(result_predict_proba[0][1] * 100, 4)
    loss_probability = round(result_predict_proba[0][0] * 100, 4)

    return win_probability, loss_probability


def match_prediction_after_action(team, action_r):

    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]

    results = ['Won', 'Lost']

    df = df[df['Result'].isin(results)]

    df_1 = df[['Team', 'Action', 'Result']]

    df_1 = df_1.replace({'Team': teams_values})

    df_1 = df_1.replace({'Action': action_values})

    df_1 = df_1.replace({'Result': result})

    x = df_1[['Team', 'Action']].values
    y = df_1[['Result']].values

    # x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            clf = LogisticRegression()

            clf.fit(x_train, y_train)

            # test_predict = KNN.predict_proba(x_test)

            test_predict = clf.predict(x_test)

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

    clf = LogisticRegression()

    clf.fit(x_train, y_train)

    # test_predict = KNN.predict_proba(x_test)

    # test_predict = clf.predict(x_test)

    # accuracy = accuracy_score(test_predict,y_test)

    # Real Time Prediction

    team = [team]
    action = [action_r]

    pred_df = pd.DataFrame()

    pred_df['Team'] = team
    pred_df['Action'] = action_r

    pred_df = pred_df.replace({'Team': teams_values})

    pred_df = pred_df.replace({'Action': action_values})

    #print(pred_df)

    pred_x = pred_df[['Team', 'Action']].values

    # pred_x = pred_x.reshape(pred_x.shape[0], )

    # pred_x = preprocessing.StandardScaler().fit(pred_x).transform(pred_x.astype(float))

    result_predict_proba = clf.predict_proba(pred_x)
    result_predict = clf.predict(pred_x)

    # test_predict = KNN.predict_proba(x_test)

    test_predict = clf.predict(x_test)

    accuracy = accuracy_score(test_predict, y_test)

    a.append(accuracy)

    # return test_predict, y_test, df_1, a

    win_probability = round(result_predict_proba[0][1] * 100, 4)
    loss_probability = round(result_predict_proba[0][0] * 100, 4)

    return win_probability, loss_probability


def match_prediction_after_first_batting(team, runs_scored):

    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]

    results = ['Won', 'Lost']

    df = df[df['Result'].isin(results)]

    df_1 = df[['Team', 'Runs Scored', 'Result']]

    df_1 = df_1.replace({'Team': teams_values})

    # df_1= df_1.replace({'Action': action_values})

    df_1 = df_1.replace({'Result': result})

    x = df_1[['Team', 'Runs Scored']].values
    y = df_1[['Result']].values

    # x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            clf = LogisticRegression()

            clf.fit(x_train, y_train)

            # test_predict = KNN.predict_proba(x_test)

            test_predict = clf.predict(x_test)

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

    clf = LogisticRegression()

    clf.fit(x_train, y_train)

    # test_predict = KNN.predict_proba(x_test)

    # test_predict = clf.predict(x_test)

    # accuracy = accuracy_score(test_predict,y_test)

    # Real Time Prediction

    team = [team]
    runs_scored = [runs_scored]

    pred_df = pd.DataFrame()

    pred_df['Team'] = team
    pred_df['Runs Scored'] = runs_scored

    pred_df = pred_df.replace({'Team': teams_values})

    #print(pred_df)

    pred_x = pred_df[['Team', 'Runs Scored']].values

    # pred_x = pred_x.reshape(pred_x.shape[0], )

    # pred_x = preprocessing.StandardScaler().fit(pred_x).transform(pred_x.astype(float))

    result_predict_proba = clf.predict_proba(pred_x)
    result_predict = clf.predict(pred_x)

    # test_predict = KNN.predict_proba(x_test)

    test_predict = clf.predict(x_test)

    accuracy = accuracy_score(test_predict, y_test)

    a.append(accuracy)

    # return test_predict, y_test, df_1, a

    win_probability = round(result_predict_proba[0][1] * 100, 4)
    loss_probability = round(result_predict_proba[0][0] * 100, 4)

    return win_probability, loss_probability


def match_prediction_after_bowling_first(team, wickets_taken):

    df = pd.read_excel('assets/Form_analysis/Match_stats_and_results.xlsx')

    test_sizes = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25]
    random_states = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]

    results = ['Won', 'Lost']

    df = df[df['Result'].isin(results)]

    df_1 = df[['Team', 'Wickets Taken', 'Result']]

    df_1 = df_1.replace({'Team': teams_values})

    # df_1= df_1.replace({'Action': action_values})

    df_1 = df_1.replace({'Result': result})

    x = df_1[['Team', 'Wickets Taken']].values
    y = df_1[['Result']].values

    # x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))

    a = []
    tests = []
    randoms = []

    for i in test_sizes:

        for j in random_states:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=j)

            y_train = y_train.reshape(y_train.shape[0], )
            y_test = y_test.reshape(y_test.shape[0], )

            clf = LogisticRegression()

            clf.fit(x_train, y_train)

            # test_predict = KNN.predict_proba(x_test)

            test_predict = clf.predict(x_test)

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

    clf = LogisticRegression()

    clf.fit(x_train, y_train)

    # test_predict = KNN.predict_proba(x_test)

    # test_predict = clf.predict(x_test)

    # accuracy = accuracy_score(test_predict,y_test)

    # Real Time Prediction

    team = [team]
    wickets_taken = [wickets_taken]

    pred_df = pd.DataFrame()

    pred_df['Team'] = team
    pred_df['Wickets Taken'] = wickets_taken

    pred_df = pred_df.replace({'Team': teams_values})

    #print(pred_df)

    pred_x = pred_df[['Team', 'Wickets Taken']].values

    # pred_x = pred_x.reshape(pred_x.shape[0], )

    # pred_x = preprocessing.StandardScaler().fit(pred_x).transform(pred_x.astype(float))

    result_predict_proba = clf.predict_proba(pred_x)
    result_predict = clf.predict(pred_x)

    # test_predict = KNN.predict_proba(x_test)

    test_predict = clf.predict(x_test)

    accuracy = accuracy_score(test_predict, y_test)

    a.append(accuracy)

    # return test_predict, y_test, df_1, a

    win_probability = round(result_predict_proba[0][1] * 100, 4)
    loss_probability = round(result_predict_proba[0][0] * 100, 4)

    return win_probability, loss_probability

