import dash_bootstrap_components as dbc
from .sidebar_1992 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1992_World_Cup/match_results_1992.xlsx')
df.reset_index(drop=True, inplace=True)

#fig1 = px.line(df.tail(10),x = 'Match',y = 'Runs',hover_data=['Match','Runs','Wkts'])

df1 = df[['Match','Winner','Ground']]
df1 = pd.DataFrame(df1)


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
                    html.H3('MATCH RESULTS - 1992 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The International Cricket Council conducted the fifth edition of the Cricket World Cup in 1992, which was formally known as the Benson & Hedges World Cup 1992. (ICC). From February 22 to March 25, 1992, Australia and New Zealand hosted the event. Pakistan defeated England in the championship match by a margin of 22 runs to win the World Cup for the first time.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])