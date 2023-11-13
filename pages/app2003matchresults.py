import dash_bootstrap_components as dbc
from .sidebar_2003 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/2003_World_Cup/match_results_2003.xlsx')
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
                    html.H3('MATCH RESULTS - 2003 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.H5('The eighth Cricket World Cup hosted by the International Cricket Council, took place in 2003. From 9 February to 23 March 2003, South Africa, Zimbabwe, and Kenya co-hosted it. The first World Cup to be held in Africa was this one.'),
                    html.Br(),
                    html.H5('In a pool game against England, Pakistan bowler Shoaib Akhtar also established a world record, becoming the sports quickest bowler with a top speed of 161.3 km/h (100.23 mph).'),
                    html.Br(),
                    html.H5('Australia eventually emerged victorious in the tournament, winning all 11 of their games and defeating India in the championship match at Wanderers Stadium in Johannesburg. Australia was the only team to win three World Cups, and this was their third.'),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])