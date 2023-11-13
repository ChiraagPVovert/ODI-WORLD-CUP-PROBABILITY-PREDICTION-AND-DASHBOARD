import dash_bootstrap_components as dbc
from .sidebar_1975 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__,name = 'MATCH AGGREGATES',order=9)

df = pd.read_excel('assets/1975_World_Cup/highest_match_aggregates_1975.xlsx')
df.reset_index(drop=True, inplace=True)

fig1 = px.scatter(df,x = 'Match',y = 'Runs',hover_data=['Match','Runs','Wkts'])
fig1.update_traces(marker_size=20)


df1 = df[['Match','Runs','Wkts','Overs','RR','Ground']]


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
                    html.H3('MATCH AGGREGATES - 1975 ODI WORLD CUP', style={'textAlign': 'center'}),
                    html.Br(),
                    #dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    ),
])