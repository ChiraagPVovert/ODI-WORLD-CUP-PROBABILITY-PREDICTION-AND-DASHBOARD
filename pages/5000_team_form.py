import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .sidebar_5000 import sidebar
import form_analysis
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly


dash.register_page(__name__, name='FORM ANALYSIS' ,order=1110000000000000)

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
                    html.H3('FORM ANALYSIS OF TEAMS AFTER 2019 ODI WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['Afghanistan','Australia','Bangladesh','England',
                                                    'India','Netherlands','New Zealand','Pakistan',
                                                    'South Africa','Sri Lanka'
                                            ], id='request_all_form')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([],id='service_all_1_form'),
                    html.Br(),
                    html.Div([], id='service_all_2_form'),
                    html.Br(),
                    html.P('* form analysis is done on the matches played after 2019 odi world cup', style={'textAlign':'center'}),
                ],xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_all_1_form','children'),
        Output('service_all_2_form','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_all_form", 'value'),
        State('service_all_1_form','children'),
        State('service_all_2_form','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    team = str(need)

    df1 = form_analysis.team_results(team)
    df2 = form_analysis.toss_wins(team)
    df3 = form_analysis.results_batting_first(team)
    df4 = form_analysis.results_bowling_first(team)
    df5 = form_analysis.results_winning_toss_and_chasing(team)
    df6 = form_analysis.results_winning_toss_and_defending(team)
    df7 = form_analysis.results_losing_toss_and_chasing(team)
    df8 = form_analysis.results_losing_toss_and_defending(team)
    df9 = form_analysis.action_after_toss_won(team)
    df10 = form_analysis.action_after_toss_lost(team)
    df11 = form_analysis.toss_won_result(team)
    df12 = form_analysis.toss_lost_result(team)

    df13 = form_analysis.runs_batting_first(team)
    df14 = form_analysis.runs_batting_second(team)
    df15 = form_analysis.wickets_taken_bowling_first(team)
    df16 = form_analysis.wickets_taken_bowling_second(team)

    if team == 'Australia':
        colours = px.colors.sequential.turbid
    elif team == 'Afghanistan':
        colours = px.colors.sequential.Plotly3
    elif team == 'Bangladesh':
        colours = px.colors.sequential.deep
    elif team == 'England':
        colours = px.colors.sequential.RdBu
    elif team == 'India':
        colours = px.colors.sequential.Blues
    elif team == 'Netherlands':
        colours = px.colors.sequential.Sunsetdark
    elif team == 'New Zealand':
        colours = px.colors.sequential.gray
    elif team == 'Pakistan':
        colours = px.colors.sequential.Blugrn
    elif team == 'South Africa':
        colours = px.colors.sequential.algae
    elif team == 'Sri Lanka':
        colours = px.colors.sequential.haline


    # Create subplots, using 'domain' type for pie charts
    specs = [
                [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
                [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
                [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
                [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]
            ]
    fig = make_subplots(rows=4, cols=3, specs=specs ,
                        subplot_titles=("MATCH RESULTS",
                                        "TOSS RESULTS",
                                        "RESULTS BATTING FIRST",
                                        'RESULTS CHASING',
                                        'RESULTS WINNING TOSS AND CHASING',
                                        'RESULTS WINNING TOSS AND DEFENDING ',
                                        "RESULTS LOSING TOSS AND CHASING",
                                        'RESULTS LOSING TOSS AND DEFENDING',
                                        'CHOICE AFTER WINNING THE TOSS',
                                        'CHOICE AFTER LOSING THE TOSS',
                                        'RESULTS AFTER WINNING THE TOSS',
                                        'RESULTS AFTER LOSING THE TOSS'),
                        )

    # Define pie charts
    fig.add_trace(go.Pie(labels=df1.Result, values=df1.Count, name='', textinfo='label+percent',#+value',
                         hole=.2, marker_colors=colours), 1, 1)
    fig.add_trace(go.Pie(labels=df2.Result, values=df2.Count, name='', textinfo='label+percent',#value',
                         hole=.2, marker_colors=colours), 1, 2)
    fig.add_trace(go.Pie(labels=df3.Result, values=df3.Count, name='', textinfo='label+percent',  # +value',
                         hole=.2, marker_colors=colours), 1, 3)
    fig.add_trace(go.Pie(labels=df4.Result, values=df4.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 2, 1)
    fig.add_trace(go.Pie(labels=df5.Result, values=df5.Count, name='', textinfo='label+percent',  # +value',
                         hole=.2, marker_colors=colours), 2, 2)
    fig.add_trace(go.Pie(labels=df6.Result, values=df6.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 2, 3)
    fig.add_trace(go.Pie(labels=df7.Result, values=df7.Count, name='', textinfo='label+percent',  # +value',
                         hole=.2, marker_colors=colours), 3, 1)
    fig.add_trace(go.Pie(labels=df8.Result, values=df8.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 3, 2)
    fig.add_trace(go.Pie(labels=df9.Action, values=df9.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 3, 3)
    fig.add_trace(go.Pie(labels=df10.Action, values=df10.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 4, 1)
    fig.add_trace(go.Pie(labels=df11.Result, values=df11.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 4, 2)
    fig.add_trace(go.Pie(labels=df12.Result, values=df12.Count, name='', textinfo='label+percent',  # value',
                         hole=.2, marker_colors=colours), 4, 3)

    #fig.update_layout(annotations=[dict(text=team, x=0.5, y=0.5, font_size=50, showarrow=False)])

    fig.update_layout(width=1300, height=1500,title_text=team.upper(),title_x=0.5)

    fig_1 = make_subplots(rows=2, cols=2,
                          subplot_titles=("RUNS SCORED BATTING FIRST",
                                          "RUNS SCORED BATTING SECOND",
                                          "WICKETS TAKEN BOWLING FIRST",
                                          'WICKETS TAKEN BOWLING SECOND',
                                          )#, shared_yaxes=True)
                          )

    fig_1.add_trace(go.Bar(x=df13['Versus'], y=df13['Runs Scored'],
                           text = df13['Runs Scored'],
                           hovertext=df13['Team'],
                           marker=dict(color=colours)
                           ,name=""),#, coloraxis="coloraxis")),
                    1, 1)

    fig_1.add_trace(go.Bar(x=df14['Versus'], y=df14['Runs Scored'],
                           text=df14['Runs Scored'],
                           hovertext=df14['Team'],
                           marker=dict(color=colours)
                           ,name=""),#, coloraxis="coloraxis")),
                    1, 2)

    fig_1.add_trace(go.Bar(x=df15['Versus'], y=df15['Wickets Taken'],
                           text=df15['Wickets Taken'],
                           hovertext=df15['Team'],
                           marker=dict(color=colours)
                           ,name=""),#, coloraxis="coloraxis")),
                    2, 1)

    fig_1.add_trace(go.Bar(x=df16['Versus'], y=df16['Wickets Taken'],
                           text=df16['Wickets Taken'],
                           hovertext=df16['Team'],
                           marker=dict(color=colours)
                           ,name=""),#, coloraxis="coloraxis")),
                    2, 2)

    #fig_1.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False)
    fig_1.update_layout(showlegend=False)
    # fig_1.update_xaxes(visible=False)
    fig_1.update_yaxes(visible=False)
    fig_1.update_layout(barmode='group')
    fig_1.update_layout(width=1300, height=1000, title_text=team.upper(), title_x=0.5)

    return [
        dcc.Graph(figure=fig),
        dcc.Graph(figure=fig_1),
        #bat_table
    ]

