import dash_bootstrap_components as dbc
from .sidebar_1975 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1975_World_Cup/match_results_1975.xlsx')
df.reset_index(drop=True, inplace=True)

#fig1 = px.line(df.tail(10),x = 'Match',y = 'Runs',hover_data=['Match','Runs','Wkts'])

df1 = df[['Match','Winner','Ground']]


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
                    html.H3('MATCH RESULTS - 1975 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The 1975 Cricket World Cup Final was a One Day International cricket match played at Lords, London on 21 June 1975 to determine the winner of the 1975 Cricket World Cup. It was the second time that the West Indies and Australia had met in the tournament after playing against each other in the group stage. The West Indies won the match by 17 runs to claim their first title.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])