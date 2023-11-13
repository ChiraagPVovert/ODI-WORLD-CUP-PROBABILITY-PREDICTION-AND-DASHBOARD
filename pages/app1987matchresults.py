import dash_bootstrap_components as dbc
from .sidebar_1987 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/1987_World_Cup/match_results_1987.xlsx')
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
                    html.H3('MATCH RESULTS - 1987 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The fourth Cricket World Cup took place in 1987, and was formally called as the Reliance Cup 1987 due to sponsorship. The first such competition outside of England was place in India and Pakistan from 8 October to 8 November 1987. The one-day format remained the same from the eight-team 1983 competition with the exception of the change from 60 to 50 overs per team, which is now the norm for all ODIs.Australia won the cup because England was unable to get the remaining 17 runs from the final over.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])