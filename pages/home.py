import dash
from dash import dcc, html, callback, Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import team_analysis

dash.register_page(__name__,name = 'TEAM ANALYSIS' , order=1100000000000000,
                   meta_tags=[{'name': 'viewport',
                               'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
                             }]
                   )

df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')
df.reset_index(drop=True, inplace=True)
df = df.sort_values(by=['WIN-PERCENTAGE'], ascending=False)

fig1 = px.bar(df,x = 'COUNTRY',y = 'WIN-PERCENTAGE',color='GROUP STAGE MATCHES',hover_data=['WON','LOST'])
fig1.update_layout(width=1550,height=500)

country = ['Afghanistan','Australia','Bangladesh','England',
           'India','Netherlands','New Zealand','Pakistan',
           'South Africa','Sri Lanka']

country = [i.upper() for i in country]


layout = [
    html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3('TEAM STATS IN WORLD CUPS', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    html.H5('WIN PERCENTAGE OF COUNTRIES IN WORLD CUPS', style={'textAlign': 'center'}),
                    html.Br(),
                    # dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    html.Br(),
                    html.H5('TEAM STATS IN ODI WORLD CUPS', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Div(
                        [
                        dbc.Col(
                            [
                                dcc.Dropdown(country,id='request_team_stats')
                            ], xs=9, sm=9, md=9, lg=5, xl=5, xxl=5
                        ),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                    #html.Div([dcc.Dropdown(country, id='request_team_stats'),],style={"display": "flex", "justifyContent": "center"}),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Div([], id='request_team_stats_fig'),
                    html.Br(),
                    #html.Div([], id='request_team_stats_table'),
                ], #xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            ),

        ]
    ),
])
]


@dash.callback(

    [
        Output('request_team_stats_fig','children'),
        #Output('request_team_stats_table','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_team_stats", 'value'),
        State('request_team_stats_fig','children'),
        #State('request_team_stats_table','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1):

    team = str(need)

    df1 = team_analysis.all_matches_played(team)
    df2 = team_analysis.all_matches_results(team)
    df3 = team_analysis.group_stage_matches_results(team)
    df4 = team_analysis.qf_results(team)
    df5 = team_analysis.sf_results(team)
    df6 = team_analysis.finals_results(team)


    if team == 'AUSTRALIA':
        colours = px.colors.sequential.turbid
    elif team == 'AFGHANISTAN':
        colours = px.colors.sequential.Plotly3
    elif team == 'BANGLADESH':
        colours = px.colors.sequential.deep
    elif team == 'ENGLAND':
        colours = px.colors.sequential.RdBu
    elif team == 'INDIA':
        colours = px.colors.sequential.Blues
    elif team == 'NETHERLANDS':
        colours = px.colors.sequential.Sunsetdark
    elif team == 'NEW ZEALAND':
        colours = px.colors.sequential.gray
    elif team == 'PAKISTAN':
        colours = px.colors.sequential.Blugrn
    elif team == 'SOUTH AFRICA':
        colours = px.colors.sequential.algae
    elif team == 'SRI LANKA':
        colours = px.colors.sequential.deep

    # Create subplots, using 'domain' type for pie charts
    specs = [
        [{'type': 'domain'}, {'type': 'domain'}],
        [{'type': 'domain'}, {'type': 'domain'}],
        [{'type': 'domain'}, {'type': 'domain'}],
    ]
    fig = make_subplots(rows=3, cols=2, specs=specs,
                        subplot_titles=('MATCHES PLAYED',
                                        'ALL MATCH RESULTS',
                                        'GROUP STAGE MATCH RESULTS',
                                        'QUARTER FINALS RESULTS',
                                        'SEMI FINALS RESULTS',
                                        'FINAL RESULTS',),
                        )

    # Define pie charts
    fig.add_trace(go.Pie(labels=df1.Result, values=df1.Count, name='', textinfo='label+percent',  # +value',
                         hole=.2, marker_colors=colours), 1, 1)
    fig.add_trace(go.Pie(labels=df2.Result, values=df2.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 1, 2)
    fig.add_trace(go.Pie(labels=df3.Result, values=df3.Count, name='', textinfo='label+percent',  # +value',
                         hole=.2, marker_colors=colours), 2, 1)
    fig.add_trace(go.Pie(labels=df4.Result, values=df4.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 2, 2)
    fig.add_trace(go.Pie(labels=df5.Result, values=df5.Count, name='', textinfo='label+percent',  # +value',
                         hole=.2, marker_colors=colours), 3, 1)
    fig.add_trace(go.Pie(labels=df6.Result, values=df6.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 3, 2)

    # fig.update_layout(annotations=[dict(text=team, x=0.5, y=0.5, font_size=50, showarrow=False)])

    fig.update_layout(width=1500, height=1500, title_text=team.upper(), title_x=0.5)


    return [
        dcc.Graph(figure=fig),
        # bat_table
    ]