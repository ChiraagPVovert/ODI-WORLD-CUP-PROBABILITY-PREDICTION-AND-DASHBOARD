import dash_bootstrap_components as dbc
from .sidebar_1979 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1979_World_Cup/match_results_1979.xlsx')
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
                    html.H3('MATCH RESULTS - 1979 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The second Cricket World Cup took place in 1979, and it was formally known as the Prudential Cup 1979. The International Cricket Conference organised it, and it took place from June 9 to June 23 in England. Following victories against Pakistan and New Zealand in their respective semifinal matches, the West Indies and England faced off in the championship match at Lords, with the West Indies retaining their crown from four years prior with a 92 run triumph.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])