import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_5000 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import lr_match_prediction
import average_scores
from plotly.subplots import make_subplots


dash.register_page(__name__,name = 'MATCH 25 ENG VS SL')

#teams_values = {'India' : 18,
#                'Australia':17}

team1 = 'England'
team2 = 'Sri Lanka'

toss_won = 'Won'
toss_lost = 'Lost'

toss_action_set_target = 'Set Target'
toss_action_chase = 'Chase'

runs_scored = 156
wickets_taken = 10


team1_win_toss,team1_loss_toss = lr_match_prediction.match_prediction_after_toss(team1,toss_won)
team2_win_toss,team2_loss_toss = lr_match_prediction.match_prediction_after_toss(team2,toss_lost)

team1_action_win,team1_action_loss = lr_match_prediction.match_prediction_after_action(team1,toss_action_set_target)
team2_action_win,team2_action_loss = lr_match_prediction.match_prediction_after_action(team2,toss_action_chase)

first_innings_runs_win,first_innings_runs_loss = lr_match_prediction.match_prediction_after_first_batting(team1,runs_scored)
first_innings_wickets_win,first_innings_wickets_loss = lr_match_prediction.match_prediction_after_bowling_first(team2,wickets_taken)

data = {
    'TEAM':[team1,team2,team1,team2,team2,team1],
    'OPTION':[toss_won,toss_lost,toss_action_set_target,toss_action_chase,runs_scored,wickets_taken],
    'WIN PROBABILITY':[team1_win_toss,team2_win_toss,team1_action_win,team2_action_win,first_innings_runs_win,first_innings_runs_win],
    'LOSS PROBABILITY':[team1_loss_toss,team2_loss_toss,team1_action_loss,team2_action_loss,first_innings_runs_loss,first_innings_wickets_loss]
}

df = pd.DataFrame(data)


team1_1 = average_scores.average_runs_scored_batting_first(team1)
team1_2 = average_scores.average_runs_scored_winning_toss_batting_first(team1)
#team1_3 = average_scores.average_runs_scored_losing_toss_batting_first(team1)
#team1_4 = average_scores.average_runs_scored_batting_second(team1)
#team1_5 = average_scores.average_runs_scored_winning_toss_batting_second(team1)
#team1_6 = average_scores.average_runs_scored_losing_toss_batting_second(team1)

#team2_1 = average_scores.average_runs_scored_batting_first(team2)
#team2_2 = average_scores.average_runs_scored_winning_toss_batting_first(team2)
#team2_3 = average_scores.average_runs_scored_losing_toss_batting_first(team2)
team2_4 = average_scores.average_runs_scored_batting_second(team2)
#team2_5 = average_scores.average_runs_scored_winning_toss_batting_second(team2)
team2_6 = average_scores.average_runs_scored_losing_toss_batting_second(team2)

df1_dict =  {
            team1.upper():[team1_1,
                           team1_2,
                           #team1_3,
                           #team1_4,
                           #team1_5,
                           #team1_6
                           ],
            team2.upper():[#team2_1,
                           #team2_2,
                           #team2_3,
                           team2_4,
                           #team2_5,
                           team2_6,
            ],
        }

df1 = pd.DataFrame(df1_dict)


#team1_01 = average_scores.average_wickets_taken_bowling_first(team1)
#team1_02 = average_scores.average_wickets_taken_winning_toss_bowling_first(team1)
#team1_03 = average_scores.average_wickets_taken_losing_toss_bowling_first(team1)
team1_04 = average_scores.average_wickets_taken_bowling_second(team1)
team1_05 = average_scores.average_wickets_taken_winning_toss_bowling_second(team1)
#team1_06 = average_scores.average_wickets_taken_losing_toss_bowling_second(team1)

team2_01 = average_scores.average_wickets_taken_bowling_first(team2)
#team2_02 = average_scores.average_wickets_taken_winning_toss_bowling_first(team2)
team2_03 = average_scores.average_wickets_taken_losing_toss_bowling_first(team2)
#team2_04 = average_scores.average_wickets_taken_bowling_second(team2)
#team2_05 = average_scores.average_wickets_taken_winning_toss_bowling_second(team2)
#team2_06 = average_scores.average_wickets_taken_losing_toss_bowling_second(team2)

df2_dict =  {
            team1.upper():[#team1_01,
                           #team1_02,
                           #team1_03,
                           team1_04,
                           team1_05,
                           #team1_06
                           ],
            team2.upper():[team2_01,
                           #team2_02,
                           team2_03,
                           #team2_04,
                           #team2_05,
                           #team2_06
                           ],
        }

df2 = pd.DataFrame(df2_dict)

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.Br(),
                    html.H2('ENGLAND VS SRI LANKA', style={'textAlign':'center'}),
                    html.Br(),
                    html.P('* Predictions are done considering the form of the teams after 2019 ODI World Cup in ODI matches', style={'textAlign':'center'}),
                    #dcc.Graph(figure=fig_1),
                    html.Br(),
                    html.H3('AFTER TOSS RESULT PREDICTIONS', style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of England winning the game after winning the toss ", style={'textAlign':'center'}),
                    html.Br(),
                    #html.H4(str((team1_win_toss)) + " %", style={'textAlign': 'center'}),
                    html.H4(str((56.6052)) + " %", style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of Sri Lanka winning the game after losing the toss ", style={'textAlign':'center'}),
                    html.Br(),
                    #html.H4(str((team2_win_toss)) + " %", style={'textAlign': 'center'}),
                    html.H4(str((48.1659)) + " %", style={'textAlign': 'center'}),
                    html.Br(),
                    html.H3('AFTER CHOICE RESULTS PREDICTION', style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of England winning the game after Batting First ", style={'textAlign':'center'}),
                    html.Br(),
                    #html.H4(str((team1_action_win)) + " %", style={'textAlign': 'center'}),
                    html.H4(str((53.3909)) + " %", style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of Sri Lanka winning the game after Bowling First ", style={'textAlign':'center'}),
                    html.Br(),
                    #html.H4(str((team2_action_win)) + " %", style={'textAlign': 'center'}),
                    html.H4(str((50.1592 )) + " %", style={'textAlign': 'center'}),
                    html.Br(),
                    html.H3('AFTER FIRST INNINGS RESULTS PREDICTION', style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of Sri Lanka winning the game after taking "+str((wickets_taken))+" wickets Bowling first ", style={'textAlign':'center'}),
                    html.Br(),
                    #html.H4(str((first_innings_wickets_win)) + " %", style={'textAlign': 'center'}),
                    html.H4(str((74.2486)) + " %", style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of England winning the game after scoring "+str((runs_scored))+" Batting First ", style={'textAlign':'center'}),
                    html.Br(),
                    #html.H4(str((first_innings_runs_win)) + " %", style={'textAlign': 'center'}),
                    html.H4(str((41.3948)) + " %", style={'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    html.H3('BATTING ANALYSIS - IN ODIS AFTER 2019 ODI WORLD CUP', style={'textAlign': 'center'}),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True, style={'textAlign': 'center'}),
                    html.Br(),
                    html.H3('BOWLING ANALYSIS - IN ODIS AFTER 2019 ODI WORLD CUP', style={'textAlign': 'center'}),
                    html.Br(),
                    dbc.Table.from_dataframe(df2, striped=True, bordered=True, hover=True,style={'textAlign': 'center'}),

                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10
            ),

        ]
    )
    ])
