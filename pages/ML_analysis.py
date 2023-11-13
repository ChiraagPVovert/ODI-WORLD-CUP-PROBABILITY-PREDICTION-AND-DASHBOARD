import dash
from dash import dash_table
from dash import dcc, html, callback, Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import Model_data_prediction
from dash.dash_table.Format import Group
import plotly.graph_objects as go
import plotly.figure_factory as ff


dash.register_page(__name__, name='DATA ANALYSIS',order = 1000000000000000)

app = dash.Dash(__name__,
                external_scripts=["https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9935242688300411"]
                )

teams = ['INDIA','AUSTRALIA','ENGLAND','NEW ZEALAND','BANGLADESH','AFGHANISTAN','PAKISTAN','SOUTH AFRICA','SRI LANKA','NETHERLANDS']
model_algorithms = ['K-Nearest Neighbors','Support Vector Machine','Logistic Regression','Artificial Neural Network - Logistic Regression']

layout = html.Div(
    [
        html.Div(
            [
            dbc.Row(
                [
                    html.Div(
                        [
                            html.Br(),
                            html.H3('DATA ANALYSIS USING ALGORITHMS'),
                            html.Br(),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(
                        [
                            html.Br(),
                            html.H5('With meticulous analysis, we have established the expected probabilities for every players entry into the playing eleven.'),
                            html.Br(),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(
                        [
                        dbc.Col(
                            [
                                dcc.Dropdown(options=teams,id='teams'),
                            ], xs=5, sm=5, md=5, lg=4, xl=4, xxl=4
                        ),
                        html.Br(),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(
                        [
                            html.Br(),
                            dbc.Button("SUBMIT", id = "inp-button", className = "data_input", n_clicks = 0),
                            html.Br(),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                ],
             ),
        ],
    ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([ ], id='bat_plot'),
                        html.Br(),
                        html.Div([ ], id='bat'),
                        html.Br(),
                        html.Div([ ], id='bowl_plot'),
                        html.Br(),
                        html.Div([ ], id='bowl'),
                        html.Br(),
                        html.Div([ ], id='all_round_plot'),
                        html.Br(),
                        html.Div([ ], id='all_round'),
                        html.Br(),
                        #dcc.Graph(id='graph'),
                    ]
                )
            ]
        )
    ]
)

@dash.callback(

    [
        Output('bat','children'),
        Output('bowl','children'),
        Output('all_round','children'),
        Output('bat_plot','children'),
        Output('bowl_plot','children'),
        Output('all_round_plot','children'),
        #Output('graph', 'figure')
    ],

    [
        #Input('teams', "value"),
        #Input('algo', 'value'),
        #Input('year', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("teams", 'value'),
        #State("algo", 'value'),
        State('bat_plot','children'),
        State('bowl_plot','children'),
        State('all_round_plot','children'),
    ],

        prevent_initial_call=True,

    )

def update_output(n_clicks,teams_val,bat_plot,bowl_plot,all_round_plot):

    #print(teams)
    '''if algo_val == 'K-Nearest Neighbors':
        algo = 'KNN'
    elif algo_val == 'Support Vector Machine':
        algo = 'SVM'
    elif algo_val == 'Logistic Regression':
        algo = 'LR'
    elif algo_val == 'Artificial Neural Network - Logistic Regression':
        algo = 'ANN'
        '''

    #print(teams_val,algo,year_val)

    algo = 'LR'

    bat,bowl,all_rounder = Model_data_prediction.model_predictions(teams_val,algo)

    #bat_table = ff.create_table(bat)
    #bowl_table = ff.create_table(bowl)
    #all_rounder_table = ff.create_table(all_rounder)

    bat_table = dbc.Table.from_dataframe(bat, striped=True, bordered=True, hover=True)
    bowl_table = dbc.Table.from_dataframe(bowl, striped=True, bordered=True, hover=True)
    all_rounder_table = dbc.Table.from_dataframe(all_rounder, striped=True, bordered=True, hover=True)

    #bat_table = dash_table.DataTable(bat.to_dict('records'), [{"name": i, "id": i} for i in bat.columns])
    #bowl_table = dash_table.DataTable(bowl.to_dict('records'), [{"name": i, "id": i} for i in bowl.columns])
    #all_rounder_table = dash_table.DataTable(all_rounder.to_dict('records'), [{"name": i, "id": i} for i in all_rounder.columns])

    fig_bat = go.Figure(data=[go.Pie(labels=bat.PLAYERS, values=bat.PROBABILITY_OF_PLAYING, hole=.3)])
    fig_bat.update_layout(title_text="BATSMAN AND WICKET KEEPERS",annotations=[dict(text='BATSMAN/WK', x=0.5, y=0.5, font_size=10, showarrow=False)])
    fig_bat.update_traces(textposition='inside', textinfo='percent+label')
    fig_bat.update_layout(width=1550, height=500)

    fig_bowl = go.Figure(data=[go.Pie(labels=bowl.PLAYERS, values=bowl.PROBABILITY_OF_PLAYING, hole=.3)])
    fig_bowl.update_layout(title_text="BOWLERS",annotations=[dict(text='BOWLERS', x=0.5, y=0.5, font_size=10, showarrow=False)])
    fig_bowl.update_traces(textposition='inside', textinfo='percent+label')
    fig_bowl.update_layout(width=1550, height=500)

    fig_all_rounder = go.Figure(data=[go.Pie(labels=all_rounder.PLAYERS, values=all_rounder.PROBABILITY_OF_PLAYING, hole=.3)])
    fig_all_rounder.update_layout(title_text="ALL ROUNDERS",annotations=[dict(text='ALL ROUNDERS', x=0.5, y=0.5, font_size=10, showarrow=False)])
    fig_all_rounder.update_traces(textposition='inside', textinfo='percent+label')
    fig_all_rounder.update_layout(width=1550, height=500)

    #print(bat)

    return[
            html.Div(bat_table),
            html.Div(bowl_table),
            html.Div(all_rounder_table),
            dcc.Graph(figure=fig_bat),
            dcc.Graph(figure=fig_bowl),
            dcc.Graph(figure=fig_all_rounder)
        ]

