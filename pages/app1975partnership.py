import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_1975 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px


dash.register_page(__name__,name='PARTNERSHIP RECORDS',order=6)

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
                    html.H3('PARTNERSHIPS - 1975 ODI WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['PARTNERSHIP BY RUNS','PARTNERSHIP BY WICKETS'], id='request_partner')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_partner'),
                    html.Br(),
                    html.Div([], id='service_2_partner')
                ],xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_partner','children'),
        Output('service_2_partner','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_partner", 'value'),
        State('service_1_partner','children'),
        State('service_2_partner','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    partnership_by_runs = pd.read_excel('assets/1975_World_Cup/highest_partnership_by_runs_1975.xlsx')
    partnership_by_wicket = pd.read_excel('assets/1975_World_Cup/highest_partnership_by_wicket_1975.xlsx')

    if need == 'PARTNERSHIP BY RUNS':
        partnership = partnership_by_runs.sort_values(by=['Runs'],ascending=False)
        partnership = partnership[['Partners','Runs','Team','O/NO','Opposition','Ground']]
        partnership_10 = partnership.head(10)
        df1_fig = dbc.Table.from_dataframe(partnership, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(partnership_10, x='Partners', y='Runs',
                     hover_data=['Partners','Runs','Team','Opposition','Ground'], color='Runs',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'PARTNERSHIP BY WICKETS':
        partnership = partnership_by_wicket#.sort_values(by=['Runs'],ascending=False)
        partnership = partnership[['Partners','Runs','Wkt','Team','O/NO','Opposition','Ground']]
        partnership_10 = partnership.head(10)
        df1_fig = dbc.Table.from_dataframe(partnership, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(partnership_10, x='Partners', y='Runs',
                     hover_data=['Partners','Runs','Wkt','Team','Opposition','Ground'], color='Runs',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]