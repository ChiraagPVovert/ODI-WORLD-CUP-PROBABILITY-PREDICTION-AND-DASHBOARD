import dash
from dash import dcc, html, callback, Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
import pandas as pd
from skimage import io
import cv2

dash.register_page(__name__,name = 'CRIC-OVERT' ,path='/', order=0000000000000000)


# Define a custom CSS style for the main content
content_style = {
    'max-width': '1000px',
    'margin': '0 auto',
    'padding': '20px',
    'background-color': '#f5f5f5',
    'border-radius': '10px',
    'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
    'text-align': 'center',  # Center the text
}

# Create a stylish button with centered text
form_analysis_button = dbc.Button("For latest analysis - Explore Form Analysis", color="primary", size="lg", href="http://www.cricovert.com/5000-team-form")

# Create a stylish and centered header
header = dbc.Card(
    dbc.CardBody([
        html.H1('CRIC-OVERT', className='display-4', style={'color': '#173f5f'}),
        html.H4('Your Ultimate Cricket Companion', style={'color': '#173f5f'}),
    ]),
    className="mb-4",
    style={'text-align': 'center'},  # Center the card
)

# Beautiful and centered text content
text_content = dbc.Card(
    dbc.CardBody([
        html.P('Welcome to the home of cricket aficionados! Cric-Overt is your gateway to the thrilling world of ODI World Cup statistics and cricket insights. Whether you are a passionate cricket enthusiast or a casual observer, we have a treasure trove of knowledge for you.', className='lead', style={'color': '#333'}),
        html.P('At our website, we believe that data analysis is the key to unlocking success, just as it is in the game of cricket. By leveraging advanced algorithms and data analytics tools, we provide insights that can help you make strategic decisions and stay ahead of the competition. Our goal is to help you score big and achieve your goals.', className='lead', style={'color': '#333'}),
        html.P('Harnessing the power of advanced machine learning, we analyze data to provide you with accurate predictions and recommendations. Stay one step ahead with our data-driven insights.',className='lead', style={'color': '#333'}),
        html.P('', className='lead', style={'color': '#333'}),
        html.P('', className='lead', style={'color': '#333'}),
    ]),
    className="mb-4",
    style={'text-align': 'center'},  # Center the card
)

# Assemble the layout
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(header),
        ]),
        dbc.Row([
            dbc.Col(text_content),
        ]),
        dbc.Row([
            dbc.Col(form_analysis_button),
        ]),
    ], style=content_style)
])


'''layout = [
    html.Div([
    dbc.Row(
        dbc.Col(
                [
                html.H1('CRIC-OVERT', style={'textAlign': 'center'}),
                html.Br(),
                html.H4('Welcome to the homepage of Cric-Overt, your go-to destination of ODI World Cups. Our website is dedicated to providing you with the ODI World Cup statistics from the first to the latest and more from the world of cricket. Whether you are a die-hard fan or a casual observer, we have something for everyone.', style={'textAlign': 'center'}),
                html.Br(),
                html.H4('Our website uses advanced machine learning techniques to analyze data and provide insights. We use Machine Learning Algorithms to analyze and interpret complex datasets. By utilizing this cutting-edge algorithm, we are able to provide accurate predictions and recommendations that can help you make informed decisions based on data-driven insights.', style={'textAlign': 'center'}),
                html.Br(),
                html.H4('At our website, we believe that data analysis is the key to unlocking success, just as it is in the game of cricket. By leveraging advanced algorithms and data analytics tools, we provide insights that can help you make strategic decisions and stay ahead of the competition. Our goal is to help you score big and achieve your goals.', style={'textAlign': 'center'}),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div([html.A([html.H3('For everyday match analysis and predictions visit - FORM ANALYSIS')], href='http://www.cricovert.com/5000-team-form', style={"color": "black", "text-decoration": "none",'textAlign': 'center'})])
                #html.H3('For everyday match updates visit - FORM ANALYSIS')
                #html.H4('', style={'textAlign': 'center'}),
                #html.Br(),
                #html.H2('DATA',style={'textAlign': 'center'}),
                #html.Br(),
                #html.H6(' BATSMANS AND WICKET KEEPERS - No of matches played, Total runs scored, Batting average, Batting Strike Rate ',style={'textAlign': 'center'}),
                #html.Br(),
                #html.H6(' BOWLERS - No of matches played, Total wickets, Bowling economy, Bowling strike rate, Bowling Average',style={'textAlign': 'center'}),
                #html.Br(),
                #html.H6(' ALL ROUNDERS - No of matches played, Total runs scored, Batting average, Batting Strike Rate , Total wickets, Bowling economy, Bowling strike rate, Bowling Average',style={'textAlign': 'center'})
                ]
       )
    )
])
]'''

'''@dash.callback(

    [
        Output('a','children'),
        Output('b','children')
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_cric_overt", 'value'),
        State('a','children'),
        State('b','children')
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    if need == 'K-NEAREST NEIGHBORS':

        img = cv2.imread('assets/Images/KNN.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('K-NEAREST NEIGHBORS',style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* The KNN algorithm is arguably the simplest machine learning algorithm. Building the model consists only of storing the training dataset.'),
            html.H6('* The KNN algorithm considers its nearest data points, where the number of data points to consider will be mentioned to the best of accuracy obtained.'),
            html.H6('* The value obtained after considering all the nearest neighbor data points is the predicted output.')
            ])
            ,dcc.Graph(figure=fig,config={'displayModeBar': True})]

    elif need == 'SUPPORT VECTOR MACHINES':

        img = cv2.imread('assets/Images/SVM.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('SUPPORT VECTOR MACHINES', style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* Support Vector Machine, often known as SVM, can be used for classification and regression tasks, they typically perform best in the classification problems.'),
            html.H6('* In this supervised machine learning algorithm, we look for the optimal hyperplane to divide the classes.'),
            html.H6('* The best hyperplane is the one that is farthest from the classes, and this is what SVM primarily aims to achieve.')
        ])
            , dcc.Graph(figure=fig, config={'displayModeBar': True})]

    elif need == 'LOGISTIC REGRESSION':

        img = cv2.imread('assets/Images/LR.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('LOGISTIC REGRESSION', style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* One of the most often used Machine Learning algorithms, within the category of Supervised Learning, is logistic regression. Using a predetermined set of independent factors, it is used to predict the categorical dependent variable.'),
            html.H6('* Given its capacity to offer probabilities and categorise new data using continuous and discrete datasets, logistic regression is an important machine learning technique.'),
            html.H6('* When classifying observations using various sources of data, logistic regression can be used to quickly identify the factors that will work well.')
        ])
            , dcc.Graph(figure=fig, config={'displayModeBar': True})]

    elif need == 'ARTIFICIAL NEURAL NETWORK - LOGISTIC REGRESSION':

        img = cv2.imread('assets/Images/ANN.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('ARTIFICIAL NEURAL NETWORK - LOGISTIC REGRESSION', style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* A technique for binary classification is logistic regression. It can be modelled as a function with any number of inputs and a range of 0 to 1 for the output.'),
            html.H6('* A machine learning method for categorization issues is the artificial neural network. An ANN is a collection of connected input and output networks where each connection has a weight assigned to it. One input layer, one or more intermediate layers, and one output layer make up this structure.'),
            html.H6()
        ])
            , dcc.Graph(figure=fig, config={'displayModeBar': True})]
            '''
