import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import copy


def layer_sizes(x_train, y_train):
    n_x = x_train.shape[0]
    n_y = y_train.shape[0]

    return (n_x, n_y)


# print(layer_sizes(x_train, y_train))


def initialize_parameters(n_x, n_h1, n_h2, n_h3, n_y):
    W1 = np.random.randn(n_h1, n_x) * 0.01
    b1 = np.zeros((n_h1, 1))
    W2 = np.random.randn(n_h2, n_h1) * 0.01
    b2 = np.zeros((n_h2, 1))
    W3 = np.random.randn(n_h3, n_h2) * 0.01
    b3 = np.zeros((n_h3, 1))
    W4 = np.random.randn(n_y, n_h3) * 0.01
    b4 = np.zeros((n_y, 1))

    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2, "W3": W3, "b3": b3, "W4": W4, "b4": b4}

    return parameters


# initialize_parameters(4,3,3,3,1)

def sigmoid(z):
    s = 1 / (1 + np.exp(-z))

    return s


def forward_propagation(x_train, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    W3 = parameters['W3']
    b3 = parameters['b3']
    W4 = parameters['W4']
    b4 = parameters['b4']

    Z1 = np.dot(W1, x_train) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    Z3 = np.dot(W3, A2) + b3
    A3 = np.tanh(Z3)
    Z4 = np.dot(W4, A3) + b4
    A4 = sigmoid(Z4)

    # print(A4.shape)
    # print(1,x_train.shape[1])

    assert (A4.shape == (1, x_train.shape[1]))

    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2, "Z3": Z3, "A3": A3, "Z4": Z4, "A4": A4}

    # print(A4)

    return A4, cache


def compute_cost(A4, y_train):
    m = y_train.shape[1]

    logprobs = np.multiply(np.log(A4), y_train) + np.multiply((1 - y_train), np.log(1 - A4))
    cost = - np.sum(logprobs) / m

    cost = float(np.squeeze(cost))

    return cost


def backward_propagation(parameters, cache, x_train, y_train):
    m = x_train.shape[1]

    W1 = parameters['W1']
    W2 = parameters['W2']
    W3 = parameters['W3']
    W4 = parameters['W4']
    A1 = cache['A1']
    A2 = cache['A2']
    A3 = cache['A3']
    A4 = cache['A4']

    dZ4 = A4 - y_train
    dW4 = (1 / m) * np.dot(dZ4, A3.T)
    db4 = (1 / m) * np.sum(dZ4, axis=1, keepdims=True)

    dZ3 = A3 - y_train
    dW3 = (1 / m) * np.dot(dZ3, A2.T)
    db3 = (1 / m) * np.sum(dZ3, axis=1, keepdims=True)

    dZ2 = A2 - y_train
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
    db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)

    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
    dW1 = (1 / m) * np.dot(dZ1, x_train.T)
    db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)

    grads = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2, "dW3": dW3, "db3": db3, "dW4": dW4, "db4": db4}

    return grads


def update_parameters(parameters, grads, learning_rate):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    W3 = parameters['W3']
    b3 = parameters['b3']
    W4 = parameters['W4']
    b4 = parameters['b4']

    dW1 = grads['dW1']
    db1 = grads['db1']
    dW2 = grads['dW2']
    db2 = grads['db2']
    dW3 = grads['dW3']
    db3 = grads['db3']
    dW4 = grads['dW4']
    db4 = grads['db4']

    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2
    W3 = W3 - learning_rate * dW3
    b3 = b3 - learning_rate * db3
    W4 = W4 - learning_rate * dW4
    b4 = b4 - learning_rate * db4

    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2, "W3": W3, "b3": b3, "W4": W4, "b4": b4}

    return parameters


def nn_model(x_train, y_train, n_h1, n_h2, n_h3, num_iterations=10000, print_cost=False):
    np.random.seed(3)
    n_x = layer_sizes(x_train, y_train)[0]
    n_y = layer_sizes(x_train, y_train)[1]

    parameters = initialize_parameters(n_x, n_h1, n_h2, n_h3, n_y)

    for i in range(0, num_iterations):
        A4, cache = forward_propagation(x_train, parameters)
        # print(A4)
        cost = compute_cost(A4, y_train)
        grads = backward_propagation(parameters, cache, x_train, y_train)
        parameters = update_parameters(parameters, grads, learning_rate=0.01)

    return parameters


def predict(parameters, X):
    # print(parameters)
    # print(X)

    A4, cache = forward_propagation(X, parameters)
    predictions = (A4 > 0.5)

    # print(A4)
    return predictions, A4


def initialize_data(year):
    df = pd.read_excel('All_odi_players_from_2019.xlsx')
    df['YEAR'] = pd.DatetimeIndex(df['LATEST_GAME_PLAYED_DATE']).year
    df['RECENTLY_PLAYING_IN_ODI'] = df['RECENTLY_PLAYING_IN_ODI'].map({'YES': 1, 'NO': 0})
    # df.head()

    bat_options = ['All Rounder']
    all_rounder_df = df[df['ROLE'].isin(bat_options)]
    all_rounder_df = all_rounder_df[all_rounder_df['YEAR'] >= year]
    # all_rounder_df = all_rounder_df[all_rounder_df['NO_OF_MATCHES_PLAYED']>=1]
    # all_rounder_df.head()

    all_rounder_df = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY', 'RECENTLY_PLAYING_IN_ODI']]
    # all_rounder_df.shape

    all_rounder_df[['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
                    'BOWLING_STRIKE_RATE', 'ECONOMY', 'RECENTLY_PLAYING_IN_ODI']] = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY', 'RECENTLY_PLAYING_IN_ODI']].astype(float)
    # all_rounder_df.info()

    # print(all_rounder_df.isnull().sum())

    data = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY', 'RECENTLY_PLAYING_IN_ODI']]
    # y = all_rounder_df[['RECENTLY_PLAYING_IN_ODI']]

    # print(data)
    # Divide the training and testing set

    # x_train = x.iloc[:50]
    # y_train = y.iloc[:50]
    # x_test = x.iloc[50:]
    # y_test = y.iloc[50:]

    df_train = data.sample(frac=0.8, random_state=1)
    df_test = data.drop(df_train.index)

    x_train = df_train[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']]
    x_test = df_test[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']]
    y_train = df_train[['RECENTLY_PLAYING_IN_ODI']]
    y_test = df_test[['RECENTLY_PLAYING_IN_ODI']]

    # print('X - train shape : ',x_train.shape)
    # print('Y - train shape : ',y_train.shape)
    # print('X - test shape : ',x_test.shape)
    # print('Y - test shape : ',y_test.shape)

    x_train = x_train.to_numpy()
    y_train = y_train.to_numpy()
    x_test = x_test.to_numpy()
    y_test = y_test.to_numpy()

    # Reshaping the numpy array.

    x_train = x_train.reshape(x_train.shape[0], -1).T
    x_test = x_test.reshape(x_test.shape[0], -1).T
    y_train = y_train.reshape(y_train.shape[0], -1).T
    y_test = y_test.reshape(y_test.shape[0], -1).T
    # print(x_train)
    # print(y_train)
    # print(x_test)
    # print(y_test)

    # print(x_train.shape)
    # print(y_train.shape)
    # print(x_test.shape)
    # print(y_test.shape)

    # Resizing the array

    x_train = x_train / 10
    x_test = x_test / 10

    # print(x_train)
    # print(x_test)
    # print(y_train)
    # print(y_test)

    return x_train, y_train, x_test, y_test


def model_predictions(team, year):
    df = pd.read_excel('All_odi_players_from_2019.xlsx')

    x_train, y_train, x_test, y_test = initialize_data(year)

    lr_model = nn_model(x_train, y_train, 5, 5, 5, num_iterations=10000, print_cost=True)

    params = {'W1': lr_model['W1'], 'b1': lr_model['b1'], 'W2': lr_model['W2'], 'b2': lr_model['b2'],
              'W3': lr_model['W3'], 'b3': lr_model['b3'], 'W4': lr_model['W4'], 'b4': lr_model['b4']}

    bowl_options = ['All Rounder']

    all_rounder_df = df[df['COUNTRY'] == team]
    all_rounder_df = all_rounder_df[all_rounder_df['ROLE'].isin(bowl_options)]
    all_rounder_df = all_rounder_df[all_rounder_df['RECENTLY_PLAYING_IN_ODI'] == 'YES']
    all_rounder_df = all_rounder_df[
        ['PLAYERS', 'NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']].copy()

    # print(all_rounder_df)

    X_bowl = all_rounder_df[
        ['NO_OF_MATCHES_PLAYED', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'WICKETS', 'BOWLING_AVERAGE',
         'BOWLING_STRIKE_RATE', 'ECONOMY']].values
    X_bowl = X_bowl.astype('float64')
    # X_bat = X_bat.to_numpy()
    X_bowl = X_bowl.transpose()

    # print(X_bowl)

    prediction, prob = predict(params, X_bowl)

    # print(prediction)
    # print(prob)

    final_all_round_predict_df = pd.DataFrame(np.transpose(prob), columns=['PROBABILITY_OF_PLAYING'])
    final_all_round_predict_df = final_all_round_predict_df.reset_index(drop=True)

    final_all_round_predict_df = pd.concat([all_rounder_df, final_all_round_predict_df], axis=1, join='inner')

    return final_all_round_predict_df

    # return np.transpose(prob)

# prob = model_predictions('INDIA',2022)

# print(prob)
