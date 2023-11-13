import dash_bootstrap_components as dbc
from .sidebar_2019 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/2019_World_Cup/match_results_2019.xlsx')
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
                    html.H3('MATCH RESULTS - 2019 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Br(),
                    html.H5('The 12th edition of the One Day International (ODI) cricket competition, which is held every four years and is sponsored by the International Cricket Council, took place in 2019. It was held in 10 locations in England between May 30 and July 14, whereas only one location in Wales hosted the event. This was Englands fifth World Cup as host nation, while Wales hosted it for the third time.'),
                    html.Br(),
                    html.H5('England and New Zealand both won their respective elimination stage semifinals to go to the final, which was held at Londons Lords. Both teams scored 241 runs in the final, which was followed by the first Super Over in an ODI. The match finished in a draw. The first title for England was won using the boundary countback system after the Super Over also ended in a tie.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])