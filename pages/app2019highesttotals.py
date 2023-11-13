import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2019 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px


dash.register_page(__name__,name = 'HIGHEST TOTALS',order=7)

df = pd.read_excel('assets/2019_World_Cup/highest_totals_2019.xlsx')
df.reset_index(drop=True, inplace=True)
df = df.sort_values(by=['Runs'])

fig1 = px.line(df.tail(10),x = 'Match',y = 'Runs',text='Team',hover_data=['Score','Match'])
fig1.update_layout(width=1200, height=500)

'''fig1 = go.Figure(data=[go.Scatter(
    x=df.tail(10).Match, y=df.tail(10).Score,
    mode='markers',
    marker_size=50)
])'''

df1 = df[['Team','Score','Runs','Opposition','Ground']]
df1 = df1.sort_values(by=['Runs'],ascending= False)
df1 = df1[['Team','Score','Opposition','Ground']]
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
                    html.H3('HIGHEST TOTALS - 2019 ODI WORLD CUP', style={'textAlign': 'center'}),
                    html.Br(),
                    #dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10),

        ]
    ),
])