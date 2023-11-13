import dash_bootstrap_components as dbc
from .sidebar_1999 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1999_World_Cup/match_results_1999.xlsx')
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
                    html.H3('MATCH RESULTS - 1999 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The International Cricket Council organised the seventh edition of the Cricket World Cup in 1999, officially known as the ICC Cricket World Cup 99. (ICC). Scotland, Ireland, Wales, and the Netherlands served as co-hosts, with England serving as the primary host. Australia won the competition by defeating Pakistan by 8 wickets in the championship game at Londons Lords Cricket Ground. Other semifinalists included New Zealand and South Africa.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])