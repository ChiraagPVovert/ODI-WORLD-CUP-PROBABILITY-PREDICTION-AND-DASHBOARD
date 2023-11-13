import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .sidebar_4000 import sidebar
import plotly.graph_objects as go
import plotly.figure_factory as ff

dash.register_page(__name__,name = 'BOWLER STATS',order=2)


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
                        html.H3('BOWLING STATS IN WORLD CUPS', style={'textAlign': 'center'}),
                        html.Br(),
                        html.Div([dcc.Dropdown(['MOST WICKETS', 'MOST OVERS BOWLED', 'MOST MAIDEN OVERS BOWLED',
                                                'BEST ECONOMY', 'BEST AVERAGE', 'BEST STRIKE RATE',
                                                'BEST BOWLING FIGURES IN AN INNINGS',
                                                ], id='request_bowl_all')]),
                        html.Br(),
                        html.Div(
                            [
                                dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                            ], style={"display": "flex", "justifyContent": "center"},
                        ),
                        html.Br(),
                        html.Div([], id='service_1_bowl_all'),
                        html.Br(),
                        html.Div([], id='service_2_bowl_all')
                    ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ])


@dash.callback(

    [
        Output('service_1_bowl_all', 'children'),
        Output('service_2_bowl_all', 'children'),
    ],

    [
        # Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_bowl_all", 'value'),
        State('service_1_bowl_all', 'children'),
        State('service_2_bowl_all', 'children'),
    ],

    prevent_initial_call=True,

)
def output(n_clicks, need, o1, o2):

    bowling = pd.read_excel('assets/Player_Stats/Bowl_complete.xlsx')
    bowling_in_an_innings = pd.read_excel('assets/Player_Stats/Bowling_innings.xlsx')

    if need == 'MOST WICKETS':

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_most_wickets.xlsx')

        bowling = bowling.sort_values(by=['Wickets'], ascending=False)
        bowling_data = bowling[['Player', 'Matches', 'Wickets', 'Economy', 'Average', 'Strike Rate', 'Country']]
        bowling_10 = bowling.head(10)
        #df1_fig = ff.create_table(bowling_data.head(50), index=False)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Wickets',
                       hover_data=['Country', 'Economy', 'Average', 'Strike Rate'], color='Wickets',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST OVERS BOWLED':

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_most_wickets.xlsx')

        bowling = bowling.sort_values(by=['Overs'], ascending=False)
        bowling_data = bowling[['Player', 'Overs', 'Economy', 'Average', 'Strike Rate', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Overs',
                       hover_data=['Country', 'Economy', 'Average', 'Strike Rate', 'Wickets'], color='Overs',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST MAIDEN OVERS BOWLED':

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_most_wickets.xlsx')

        bowling = bowling.sort_values(by=['Maidens'], ascending=False)
        bowling_data = bowling[['Player', 'Maidens', 'Economy', 'Average', 'Strike Rate', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Maidens',
                       hover_data=['Country', 'Economy', 'Average', 'Strike Rate', 'Wickets', 'Overs'], color='Maidens',
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

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_economy.xlsx')

        bowling = bowling.sort_values(by=['Economy'])
        bowling_data = bowling[['Player', 'Economy', 'Overs', 'Runs', 'Maidens', 'Average', 'Strike Rate', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Economy',
                       hover_data=['Country', 'Maidens', 'Average', 'Strike Rate', 'Wickets', 'Overs'], color='Economy',
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

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_average.xlsx')

        bowling = bowling.sort_values(by=['Average'])
        # bowling = bowling.where(bowling["Average"] != 0)
        bowling_data = bowling[['Player', 'Average', 'Overs', 'Runs', 'Economy', 'Maidens', 'Strike Rate', 'Wickets', 'Country']]
        bowling_10 = bowling.head(10)
        #df1_fig = ff.create_table(bowling_data.tail(-113).head(50), index=False)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)


        fig_1 = px.bar(bowling_10, x='Player', y='Average',
                       hover_data=['Country', 'Economy', 'Maidens', 'Strike Rate', 'Wickets', 'Overs'], color='Average',
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

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_sr.xlsx')

        bowling = bowling.sort_values(by=['Strike Rate'])
        # bowling = bowling.where(bowling["Average"] != 0)
        bowling_data = bowling[['Player', 'Strike Rate', 'Economy', 'Maidens', 'Average', 'Wickets', 'Overs', 'Country']]
        bowling_10 = bowling.head(10)
        #df1_fig = ff.create_table(bowling_data.tail(-112).head(50), index=False)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Strike Rate',
                       hover_data=['Country', 'Economy', 'Maidens', 'Average', 'Wickets', 'Overs'], color='Strike Rate',
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

        bowling = pd.read_excel('assets/Player_Stats/Bowling/Bowl_best_figures_in_an_innings.xlsx')

        bowling = bowling_in_an_innings.sort_values(by=['Wickets', 'Runs'], ascending=[False, True])
        # bowling = bowling.where(bowling["Average"] != 0)
        bowling_data = bowling[['Player', 'Overs', 'Maidens', 'Runs', 'Wickets', 'Economy', 'Country', 'Opposition']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='Player', y='Wickets',
                       hover_data=['Overs', 'Maidens', 'Runs', 'Wickets', 'Economy', 'Opposition', ], color='Wickets',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]