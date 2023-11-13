import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2015 import sidebar
import os
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__,name = 'BATTING RECORDS',order=2)

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
                    html.H3('BATTING - 2015 ODI WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST RUNS', 'HIGHEST SCORERS IN AN INNINGS', 'BEST AVERAGE',
                                            'BEST STRIKE RATE','MOST BOUNDARIES','MOST RUNS FROM BOUNDARIES','MOST 100s','MOST 50s',
                                            'BEST STRIKE RATE IN AN INNINGS','MOST BOUNDARIES IN AN INNINGS',
                                            'MOST RUNS FROM BOUNDARIES IN AN INNINGS'], id='request_bat_2015')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([],id='service_1_bat_2015'),
                    html.Br(),
                    html.Div([], id='service_2_bat_2015')
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_bat_2015','children'),
        Output('service_2_bat_2015','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_bat_2015", 'value'),
        State('service_1_bat_2015','children'),
        State('service_2_bat_2015','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    batting = pd.read_excel('assets/2015_World_Cup/bat_most_runs_hs_avg_sr_bf_no_hund_fifties_ducks_sixes_fours_2015.xlsx')
    batting_in_an_innings = pd.read_excel('assets/2015_World_Cup/bat_most_runs_from_fours_sixes_in_an_innings_2015.xlsx')

    if need == 'MOST RUNS':
        batting = batting.sort_values(by=['Runs'],ascending=False)
        batting_data = batting[['Player','Runs','HS', 'Ave','SR','Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='Runs',
                     hover_data=['Country', 'HS', 'Ave','SR'], color='Runs',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'HIGHEST SCORERS IN AN INNINGS':

        batting = batting.sort_values(by=['HS'], ascending=False)
        batting_data = batting[['Player', 'HS', 'Runs', 'Ave','HS_O/NO','SR','Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='HS',
                       hover_data=['Country', 'Runs', 'Ave', 'SR'], color='HS',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST AVERAGE':

        batting = batting.sort_values(by=['Ave'], ascending=False)
        batting_data = batting[['Player', 'Ave','Runs', 'HS', 'SR', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='Ave',
                       hover_data=['Country', 'Runs', 'HS', 'SR'], color='Ave',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE':

        batting = batting.sort_values(by=['SR'], ascending=False)
        batting_data = batting[['Player', 'SR', 'Runs', 'HS', 'Ave', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='SR',
                       hover_data=['Country', 'Runs', 'HS', 'Ave'], color='SR',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST BOUNDARIES':

        batting = batting.sort_values(by=['BOUNDARIES'], ascending=False)
        batting_data = batting[['Player', '4s', '6s', 'BOUNDARIES','RUNS FROM BOUNDARIES','Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = go.Figure()
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting['4s'],
            name='FOURS',
            #marker_color='indianred'
        ))
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting['6s'],
            name='SIXES',
            #marker_color='lightsalmon'
        ))
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]
    elif need == 'MOST RUNS FROM BOUNDARIES':

        batting = batting.sort_values(by=['RUNS FROM BOUNDARIES'], ascending=False)
        batting_data = batting[['Player', 'RUNS FROM BOUNDARIES', 'Runs', 'HS', 'Ave','Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='RUNS FROM BOUNDARIES',
                       hover_data=['Country', 'Runs', 'HS', 'Ave','RUNS FROM BOUNDARIES'], color='RUNS FROM BOUNDARIES',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST 100s':

        batting = batting.sort_values(by=['100s'], ascending=False)
        batting_data = batting[['Player', '100s','Runs', 'HS', 'SR','Ave', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(12), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='100s',
                       hover_data=['Country', 'Runs', 'HS', 'SR','Ave'], color='100s',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST 50s':

        batting = batting.sort_values(by=['50s'], ascending=False)
        batting_data = batting[['Player', '50s','Runs', 'HS', 'SR','Ave', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(44), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='50s',
                       hover_data=['Country', 'Runs', 'HS', 'SR','Ave'], color='50s',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['SR'], ascending=False)
        batting_data = batting_in_an_innings[['Player','Runs', 'Balls','4s','6s','SR', 'Country','Opposition']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='SR',
                       hover_data=['Runs', 'Balls','4s','6s', 'Country','Opposition'], color='SR',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST BOUNDARIES IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['4 and 6'], ascending=False)
        batting_data = batting_in_an_innings[['Player','Runs', 'Balls','4s','6s','SR', 'Country','Opposition']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = go.Figure()
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting_10['4s'],
            name='FOURS',
            # marker_color='indianred'
        ))
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting_10['6s'],
            name='SIXES',
            # marker_color='lightsalmon'
        ))
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST RUNS FROM BOUNDARIES IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['4+6'], ascending=False)
        batting_data = batting_in_an_innings[['Player', 'Runs', 'Balls', '4s', '6s','4+6', 'SR', 'Country', 'Opposition']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='Player', y='4+6',
                       hover_data=['Runs', 'Balls', '4s', '6s', 'Country', 'Opposition'], color='4+6',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]