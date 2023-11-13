import dash_bootstrap_components as dbc
from .sidebar_1983 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1983_World_Cup/match_results_1983.xlsx')
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
                    html.H3('MATCH RESULTS - 1983 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The third iteration of the Cricket World Cup was held in 1983 (formally known as the Prudential Cup 83). From June 9 to June 25, 1983, it took place throughout England and Wales. India was assigned to bat against the West Indies in the championship after losing the toss. Only Krishnamachari Srikkanth (38 off 57 balls) and Mohinder Amarnath (26 off 80 balls) offered any real fight as Roberts, Marshall, Joel Garner, Michael Holding, and Gomes skillfully assisted them in destroying the Indian batters. Unexpected tail resistance allowed India to gather 183. (all out, 54.4 overs). The West Indies were bowled out for 140 from 52 overs by the Indian bowling, who took full advantage of the weather and pitch conditions to win by 43 runs and pulled off one of the greatest shocks in cricket history.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])