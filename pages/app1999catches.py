import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_1999 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name='CATCH RECORDS',order=4)

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
                    html.H3('CATCHES - 1999 ODI WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST CATCHES BY A FIELDER (EXCLUDING WICKET KEEPER)',
                                            'MOST CATCHES IN AN INNINGS BY A FIELDER (EXCLUDING WICKET KEEPER)'], id='request_catch_1999')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_catch_1999'),
                    html.Br(),
                    html.Div([], id='service_2_catch_1999')
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_catch_1999','children'),
        Output('service_2_catch_1999','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_catch_1999", 'value'),
        State('service_1_catch_1999','children'),
        State('service_2_catch_1999','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    catches = pd.read_excel('assets/1999_World_Cup/most_catches_1999.xlsx')
    catches_in_an_innings = pd.read_excel('assets/1999_World_Cup/most_catches_in_an_innings_1999.xlsx')

    if need == 'MOST CATCHES BY A FIELDER (EXCLUDING WICKET KEEPER)':
        catch = catches.sort_values(by=['Catches'],ascending=False)
        catch_data = catch[['Player','Matches','Catches','Country']]
        catch_data = pd.DataFrame(catch_data)
        catch_10 = catch.head(10)
        df1_fig = dbc.Table.from_dataframe(catch_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(catch_10, x='Player', y='Catches',
                     hover_data=['Player','Matches','Catches','Country'], color='Catches',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST CATCHES IN AN INNINGS BY A FIELDER (EXCLUDING WICKET KEEPER)':
        catch = catches_in_an_innings.sort_values(by=['Catches'],ascending=False)
        catch_data = catch[['Player','Catches','Country','Opposition']]
        catch_data = pd.DataFrame(catch_data)
        catch_10 = catch.head(10)
        df1_fig = dbc.Table.from_dataframe(catch_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(catch_10, x='Player', y='Catches',
                     hover_data=['Player','Catches','Country','Opposition'], color='Catches',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]
