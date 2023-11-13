import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_4000 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name = 'WICKET KEEPER RECORDS',order=3)

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
                    html.H3('WICKET KEEPER - ALL WORLD CUPS', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST DISMISSALS INVOLVING A WICKET KEEPER','MOST STUMPS BY A WICKET KEEPER',
                                            'MOST CATCHES BY A WICKET KEEPER',
                                            'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS','MOST STUMPS BY A WICKET KEEPER IN AN INNINGS',
                                            'MOST CATCHES BY A WICKET KEEPER IN AN INNINGS'], id='request_wk_all')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_wk_all'),
                    html.Br(),
                    html.Div([], id='service_2_wk_all')
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
    ])

@dash.callback(

        [
            Output('service_1_wk_all', 'children'),
            Output('service_2_wk_all', 'children'),
        ],

        [
            # Input('teams', "value"),
            Input('inp-button', "n_clicks")
        ],

        [
            State("request_wk_all", 'value'),
            State('service_1_wk_all', 'children'),
            State('service_2_wk_all', 'children'),
        ],

        prevent_initial_call=True,

    )
def output(n_clicks, need, o1, o2):

    wk = pd.read_excel('assets/Player_Stats/Wk/most_wk_dismissals.xlsx')
    wk_innings = pd.read_excel('assets/Player_Stats/Wk/most_wk_dismissals_in_an_innings.xlsx')

    if need == 'MOST DISMISSALS INVOLVING A WICKET KEEPER':

        wk = wk.sort_values(by=['Dismissals'],ascending=False)
        wk = wk[['Player','Match','Catches','Stumps','Dismissals']]
        wk = wk
        #df1_fig = dbc.Table.from_dataframe(wk.head(50), striped=True, bordered=True, hover=True)
        df1_fig = dbc.Table.from_dataframe(wk.head(50), striped=True, bordered=True, hover=True)


        fig_1 = px.bar(wk.head(10), x='Player', y='Dismissals',
                     hover_data=['Player','Match','Catches','Stumps','Dismissals'], color='Dismissals',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST STUMPS BY A WICKET KEEPER':

        wk = wk.sort_values(by=['Stumps'], ascending=False)
        wk = wk[['Player', 'Match', 'Catches', 'Stumps', 'Dismissals']]
        wk = wk
        df1_fig = dbc.Table.from_dataframe(wk.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk.head(10), x='Player', y='Stumps',
                       hover_data=['Player', 'Match', 'Catches','Stumps', 'Dismissals'], color='Stumps',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST CATCHES BY A WICKET KEEPER':

        wk = wk.sort_values(by=['Catches'], ascending=False)
        wk = wk[['Player', 'Match', 'Catches', 'Stumps', 'Dismissals']]
        wk = wk
        df1_fig = dbc.Table.from_dataframe(wk.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk.head(10), x='Player', y='Catches',
                       hover_data=['Player', 'Match', 'Catches','Stumps', 'Dismissals'], color='Catches',
                       # labels={'pop': 'population of Canada'},
                       height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS':
        wk_innings = wk_innings.sort_values(by=['Dismissals'],ascending=False)
        wk_innings = wk_innings[['Player','Catches','Stumps','Dismissals','Match','Ground']]
        wk_innings_10 = wk_innings.head(10)
        #df1_fig = ff.create_table(wk_innings.head(50), index=False)
        df1_fig = dbc.Table.from_dataframe(wk_innings.head(50), striped=True, bordered=True, hover=True)


        fig_1 = px.bar(wk_innings_10, x='Player', y='Dismissals',
                     hover_data=['Catches','Stumps','Match','Ground'], color='Dismissals',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST STUMPS BY A WICKET KEEPER IN AN INNINGS':
        wk_innings = wk_innings.sort_values(by=['Stumps'],ascending=False)
        wk_innings = wk_innings[['Player','Stumps','Catches','Dismissals','Match','Ground']]
        wk_innings_10 = wk_innings.head(10)
        #df1_fig = ff.create_table(wk_innings.head(50), index=False)
        df1_fig = dbc.Table.from_dataframe(wk_innings.head(50), striped=True, bordered=True, hover=True)


        fig_1 = px.bar(wk_innings_10, x='Player', y='Stumps',
                     hover_data=['Catches','Dismissals','Match','Ground'], color='Stumps',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST CATCHES BY A WICKET KEEPER IN AN INNINGS':
        wk_innings = wk_innings.sort_values(by=['Catches'],ascending=False)
        wk_innings = wk_innings[['Player','Catches','Stumps','Dismissals','Match','Ground']]
        wk_innings_10 = wk_innings.head(10)
        #df1_fig = ff.create_table(wk_innings.head(50), index=False)
        df1_fig = dbc.Table.from_dataframe(wk_innings.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk_innings_10, x='Player', y='Catches',
                     hover_data=['Stumps','Dismissals','Match','Ground'], color='Catches',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]