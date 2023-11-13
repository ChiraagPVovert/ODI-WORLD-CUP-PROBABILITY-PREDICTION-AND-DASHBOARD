import dash
from dash import html, dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_1975 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__, name='BOWLING RECORDS', order=3)


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
                        html.H3('BOWLING - 1975 ODI WORLD CUP', style={'textAlign': 'center'}),
                        html.Br(),
                        html.Div([dcc.Dropdown(['MOST WICKETS', 'MOST OVERS BOWLED', 'MOST MAIDEN OVERS BOWLED',
                                                'BEST ECONOMY', 'BEST AVERAGE', 'BEST STRIKE RATE',
                                                'BEST BOWLING FIGURES IN AN INNINGS',
                                                'LEAST RUNS CONCEDED IN AN INNINGS',
                                                'MOST RUNS CONCEDED IN AN INNINGS',
                                                'MOST MAIDENS BOWLED IN AN INNINGS', 'MOST WICKETS TAKEN IN AN INNINGS',
                                                'BEST ECONOMY IN AN INNINGS'], id='request_bowl')]),
                        html.Br(),
                        html.Div(
                            [
                                dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                            ], style={"display": "flex", "justifyContent": "center"},
                        ),
                        html.Br(),
                        html.Div([], id='service_1_bowl'),
                        html.Br(),
                        html.Div([], id='service_2_bowl')
                    ],xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ])


@dash.callback(

    [
        Output('service_1_bowl', 'children'),
        Output('service_2_bowl', 'children'),
    ],

    [
        # Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_bowl", 'value'),
        State('service_1_bowl', 'children'),
        State('service_2_bowl', 'children'),
    ],

    prevent_initial_call=True,

)
def output(n_clicks, need, o1, o2):
    bowling = pd.read_excel('assets/1975_World_Cup/bowl_wkts_avg_econ_sr_4w_5w_bbi_1975.xlsx')
    bowling_in_an_innings = pd.read_excel('assets/1975_World_Cup/bowl_innings_wkts_econ_runsconc_sr_1975.xlsx')

    if need == 'MOST WICKETS':
        bowling = bowling.sort_values(by=['Wickets'], ascending=False)
        bowling_data = bowling[['Player', 'Wickets', 'Econ', 'Ave', 'SR', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Wickets',
                       hover_data=['Country', 'Econ', 'Ave', 'SR'], color='Wickets',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST OVERS BOWLED':
        bowling = bowling.sort_values(by=['Overs'], ascending=False)
        bowling_data = bowling[['Player', 'Overs', 'Econ', 'Ave', 'SR', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Overs',
                       hover_data=['Country', 'Econ', 'Ave', 'SR', 'Wickets'], color='Overs',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST MAIDEN OVERS BOWLED':
        bowling = bowling.sort_values(by=['Maidens'], ascending=False)
        bowling_data = bowling[['Player', 'Maidens', 'Econ', 'Ave', 'SR', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Maidens',
                       hover_data=['Country', 'Econ', 'Ave', 'SR', 'Wickets', 'Overs'], color='Maidens',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST ECONOMY':
        bowling = bowling.sort_values(by=['Econ'])
        bowling_data = bowling[['Player', 'Econ', 'Overs', 'Runs', 'Maidens', 'Ave', 'SR', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Econ',
                       hover_data=['Country', 'Maidens', 'Overs', 'Runs', 'Ave', 'SR', 'Wickets', 'Overs'],
                       color='Econ',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST AVERAGE':
        bowling = bowling.sort_values(by=['Ave'])
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Ave', 'Econ', 'Overs', 'Runs', 'Maidens', 'SR', 'Wickets', 'Country']]
        bowling_10 = bowling.iloc[13:].head(10)
        df1_fig = dbc.Table.from_dataframe(bowling.iloc[13:], striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Ave',
                       hover_data=['Country', 'Econ', 'Overs', 'Runs', 'Maidens', 'SR', 'Wickets', 'Overs'], color='Ave',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE':
        bowling = bowling.sort_values(by=['SR'])
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'SR', 'Econ', 'Overs', 'Runs', 'Maidens', 'Ave', 'Wickets', 'Overs', 'Country']]
        bowling_10 = bowling.iloc[13:].head(10)
        df1_fig = dbc.Table.from_dataframe(bowling.iloc[13:], striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='SR',
                       hover_data=['Country', 'Econ', 'Maidens', 'Ave', 'Wickets', 'Overs'], color='SR',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST BOWLING FIGURES IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['Wkts'], ascending=False)
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Wkts',
                       hover_data=['Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Opposition', ], color='Wkts',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'LEAST RUNS CONCEDED IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['Runs'], ascending=True)
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Runs',
                       hover_data=['Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Opposition', ], color='Runs',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST RUNS CONCEDED IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['Runs'], ascending=False)
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Runs',
                       hover_data=['Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Opposition', ], color='Runs',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST MAIDENS BOWLED IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['Mdns'], ascending=False)
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Mdns',
                       hover_data=['Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Opposition', ], color='Mdns',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST WICKETS TAKEN IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['Wkts'], ascending=False)
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Wkts',
                       hover_data=['Overs', 'Wkts', 'Mdns', 'Runs', 'Econ', 'SR', 'Opposition', ], color='Wkts',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST ECONOMY IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['Econ'], ascending=True)
        # bowling = bowling.where(bowling["Ave"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Mdns', 'Runs', 'Wkts', 'Econ', 'SR', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Econ',
                       hover_data=['Overs', 'Econ', 'Mdns', 'Runs', 'Wkts', 'SR', 'Opposition', ], color='Econ',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]