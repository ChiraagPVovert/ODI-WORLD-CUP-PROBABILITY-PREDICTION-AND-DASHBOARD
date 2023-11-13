import dash_bootstrap_components as dbc
from .sidebar_2007 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/2007_World_Cup/match_results_2007.xlsx')
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
                    html.H3('MATCH RESULTS - 2007 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The ninth edition of the One Day International (ODI) cricket competition, the 2007 ICC Cricket World Cup, was held in the West Indies from March 13 to April 28, 2007. 51 matches were played over all, three fewer than at the 2003 World Cup.'),
                    html.Br(),
                    html.H5('Initially, the 16 competing teams were split into four groups, with the top two teams from each group advancing to a Super 8 format. From there, Australia, New Zealand, Sri Lanka, and South Africa advanced to the World Cup finals, where Australia defeated Sri Lanka to win the tournament for the third time in a row and a record-tying fourth time overall. Australias streak of 29 World Cup games without a loss, which began on May 23, 1999, during the 1999 World Cups group stage, was extended by their unblemished record in the competition.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])