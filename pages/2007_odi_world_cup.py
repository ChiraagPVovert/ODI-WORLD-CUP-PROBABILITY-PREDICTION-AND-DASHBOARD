import dash
from dash import html, dcc, Input, Output, State, callback,dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .sidebar_2007 import sidebar
import plotly.graph_objects as go
import plotly.figure_factory as ff


dash.register_page(__name__, name = '2007 ODI WORLD CUP', order=1111111111110000)

df = pd.read_excel('assets/2007_World_Cup/points_table_2007.xlsx')
df = df.fillna(' ')
df = df[['SUPER EIGHTS','TEAMS','MATCHES','W','L','T','N/R','POINTS','NRR']]
df1 = df[:8]
df1.reset_index(drop=True, inplace=True)

df2 = df[8:13]
df2.columns = df2.iloc[0]
df2 = df2[1:]
df2.reset_index(drop=True, inplace=True)

df3 = df[13:18]
df3.columns = df3.iloc[0]
df3 = df3[1:]
df3.reset_index(drop=True, inplace=True)

df4 = df[18:23]
df4.columns = df4.iloc[0]
df4 = df4[1:]
df4.reset_index(drop=True, inplace=True)

df5 = df[23:28]
df5.columns = df5.iloc[0]
df5 = df5[1:]
df5.reset_index(drop=True, inplace=True)

fig1 = go.Figure(data=[go.Pie(labels=df1.TEAMS, values=df1.POINTS, pull=[0, 0, 0, 0, 0, 0, 0, 0.2])])
fig2 = go.Figure(data=[go.Pie(labels=df2.TEAMS, values=df2.POINTS, pull=[0, 0, 0, 0, 0.2])])
fig3 = go.Figure(data=[go.Pie(labels=df3.TEAMS, values=df2.POINTS, pull=[0, 0, 0, 0, 0.2])])
fig4 = go.Figure(data=[go.Pie(labels=df4.TEAMS, values=df2.POINTS, pull=[0, 0, 0, 0, 0.2])])
fig5 = go.Figure(data=[go.Pie(labels=df5.TEAMS, values=df2.POINTS, pull=[0, 0, 0, 0, 0.2])])

fig1.update_layout(width=1200, height=500)
fig2.update_layout(width=1200, height=500)
fig3.update_layout(width=1200, height=500)
fig4.update_layout(width=1200, height=500)
fig5.update_layout(width=1200, height=500)


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
                    html.H3('POINTS TABLE - 2007 ODI WORLD CUP', style={'textAlign': 'center'}),
                    html.Br(),
                    #dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    #dash_table.DataTable(df2.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    dcc.Graph(figure=fig2),
                    html.Br(),
                    #dash_table.DataTable(df3_fig.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    dcc.Graph(figure=fig3),
                    #dash_table.DataTable(df4_fig.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    dcc.Graph(figure=fig4),
                    #dash_table.DataTable(df5_fig.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True),
                    html.Br(),
                    dcc.Graph(figure=fig5)
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10),

        ]
    ),

])





