import dash_bootstrap_components as dbc
from .sidebar_2015 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/2015_World_Cup/match_results_2015.xlsx')
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
                    html.H3('MATCH RESULTS - 2015 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The International Cricket Council hosts the One Day International (ODI) cricket competition every four years for mens national teams. The 2015 ICC Cricket World Cup was the 11th edition of the tournament (ICC). Australia won the event, which was co-hosted by Australia and New Zealand from 14 February to 29 March 2015. The 1992 Cricket World Cup was the first tournament to be hosted in Australia and New Zealand, and this one was as well.'),
                    html.Br(),
                    html.H5('Australia and New Zealand, the co-hosts, faced off in the final. Australia won the fifth Cricket World Cup with a victory of seven wickets.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])