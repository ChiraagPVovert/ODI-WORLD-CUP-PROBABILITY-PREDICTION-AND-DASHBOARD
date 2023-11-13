import dash_bootstrap_components as dbc
from .sidebar_2011 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/2011_World_Cup/match_results_2011.xlsx')
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
                    html.H3('MATCH RESULTS - 2011 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The tenth Cricket World Cup was held in 2011, according to the ICC. It was performed in India, Sri Lanka, and Bangladesh for the first time. India became the first nation to win the Cricket World Cup final on home soil by defeating Sri Lanka by six wickets in the championship match at Mumbais Wankhede Stadium. Yuvraj Singh of India was named the winner of the competition. Two Asian teams competing in the World Cup final for the first time in tournament history. Also, it was the first time since the 1992 World Cup that Australia was absent from the championship game.'),
                    html.Br(),
                    html.H5('Commentary by Ravi Shastri - Dhoni finishes off in style. A magnificent strike into the crowd. India lift the World Cup after 28 years. The party starts in the dressing room and it’s an Indian captain who’s been absolutely magnificent in the night of the final'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])