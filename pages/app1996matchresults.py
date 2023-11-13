import dash_bootstrap_components as dbc
from .sidebar_1996 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1996_World_Cup/match_results_1996.xlsx')
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
                    html.H3('MATCH RESULTS - 1996 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The sixth Cricket World Cup, also known as the Wills World Cup 1996 after the Wills Navy Cut brand produced by event sponsor ITC, was held in 1996. It was put on by the International Cricket Council (ICC). Sri Lanka served as the first-time hosts of the World Cup, which was the second to be hosted by Pakistan and India (who had also served as the hosts of the 1987 Cricket World Cup). On March 17, 1996, at the Gaddafi Stadium in Lahore, Pakistan, Sri Lanka defeated Australia by a score of 7 wickets to win the championship.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])