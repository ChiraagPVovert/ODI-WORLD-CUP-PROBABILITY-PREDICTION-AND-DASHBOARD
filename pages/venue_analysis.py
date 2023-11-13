import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import cv2
import plotly.graph_objects as go
import plotly.figure_factory as ff

dash.register_page(__name__, name='VENUE ANALYSIS' ,order=1000000000000000,
                   meta_tags=[{'name': 'viewport',
                               'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
                             }],
                external_scripts=["https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9935242688300411"]
                 )

stadiums = [
            'NARENDRA MODI STADIUM - AHMEDABAD','RAJIV GANDHI INTERNATIONAL STADIUM - HYDERABAD',
            'HIMACHAL PRADESH CRICKET ASSOCIATION STADIUM - DHARAMSHALA','ARUN JAITLEY STADIUM - DELHI',
            'MA CHIDAMBARAM STADIUM - CHENNAI','BHARAT RATNA SHRI ATAL BIHARI VAJPAYEE EKANA CRICKET STADIUM - LUCKNOW',
            'MAHARASTRA CRICKET ASSOCIATION STADIUM - PUNE','M CHINNASWAMY STADIUM - BENGALURU',
            'WANKHEDE STADIUM - MUMBAI','EDEN GARDENS - KOLKATA'
            ]

teams = ['INDIA','AUSTRALIA','ENGLAND','NEW ZEALAND','BANGLADESH','AFGHANISTAN','PAKISTAN','SOUTH AFRICA','SRI LANKA','NETHERLANDS']

layout = html.Div(
    [
        html.Div(
            [
            dbc.Row(
                [
                    html.Div(
                        [
                            html.Br(),
                            html.H3('VENUE STATS IN ODI'),
                            html.Br(),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Div(
                        [
                        dbc.Col(
                            [
                                dcc.Dropdown(options=stadiums,id='stadiums'),
                            ], xs=5, sm=5, md=5, lg=5, xl=5, xxl=5
                        ),],style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(
                        [
                        dbc.Col(
                            [
                                dcc.Dropdown(options=teams,id='teams')
                            ], xs=9, sm=9, md=9, lg=5, xl=5, xxl=5
                        ),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div(
                        [
                            html.Br(),
                            dbc.Button("SUBMIT", id = "inp-button", className = "data_input", n_clicks = 0),
                            html.Br(),
                        ],style={"display": "flex", "justifyContent": "center"},
                    ),
                ],
             ),
        ],
    ),
        dbc.Row(
            [
                dbc.Col(
                    [
						html.Br(),
						html.Div([],id='service_all_1_venue'),
						html.Br(),
						html.Div([], id='service_all_2_venue'),
						html.Br(),
						html.Div([], id='service_all_3_venue'),
						html.Br(),
						html.Div([], id='service_all_4_venue'),
                        html.Br(),
						html.Div([], id='service_all_6_venue',style={"display": "flex", "justifyContent": "center",'font-size':'20px','font-weight':'bold'},),
                        html.Br(),
						html.Div([], id='service_all_7_venue'),
                        html.Br(),
                        html.Div([], id='service_all_5_venue'),
                        #dcc.Graph(id='graph'),
                    ]
                )
            ]
        )
    ]
)

@dash.callback(

    [
        Output('service_all_1_venue','children'),
        Output('service_all_2_venue','children'),
        Output('service_all_3_venue','children'),
        Output('service_all_4_venue','children'),
        Output('service_all_5_venue','children'),
        Output('service_all_6_venue', 'children'),
        Output('service_all_7_venue', 'children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("stadiums", 'value'),
        State("teams", 'value'),
        State('service_all_1_venue','children'),
        State('service_all_2_venue','children'),
        State('service_all_3_venue','children'),
        State('service_all_4_venue','children'),
        State('service_all_5_venue','children'),
        State('service_all_6_venue', 'children'),
        State('service_all_7_venue', 'children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,stadium,teams,o1,o2,o3,o4,o5,o6,o7):

    df = pd.read_excel('assets/Venue_Stats/venue_analysis.xlsx')

    if stadium == 'NARENDRA MODI STADIUM - AHMEDABAD':
        location = 'Narendra_Modi_Stadium_Ahmedabad.jpg'
        view = 'NARENDRA MODI STADIUM'

    elif stadium == 'RAJIV GANDHI INTERNATIONAL STADIUM - HYDERABAD':
        location = 'Rajiv_Gandhi_International_Stadium_Hyderabad.jpg'
        view = 'RAJIV GANDHI INTERNATIONAL STADIUM'

    elif stadium == 'HIMACHAL PRADESH CRICKET ASSOCIATION STADIUM - DHARAMSHALA':
        location = 'Himahal_Pradesh_Cricket_Association_Stadium_Dharamshala.jpg'
        view = 'HIMACHAL PRADESH CRICKET ASSOCIATION STADIUM'

    elif stadium == 'ARUN JAITLEY STADIUM - DELHI':
        location = 'Arun_Jaitley_Stadium_New_Delhi.jpg'
        view = 'ARUN JAITLEY STADIUM'

    elif stadium == 'MA CHIDAMBARAM STADIUM - CHENNAI':
        location = 'MA_Chidambaram_Stadium_Chennai.jpg'
        view = 'MA CHIDAMBARAM STADIUM'

    elif stadium == 'BHARAT RATNA SHRI ATAL BIHARI VAJPAYEE EKANA CRICKET STADIUM - LUCKNOW':
        location = 'Atal_Stadium_Lucknow.jpg'
        view = 'BHARAT RATNA SHRI ATAL BIHARI VAJPAYEE EKANA CRICKET STADIUM'

    elif stadium == 'MAHARASTRA CRICKET ASSOCIATION STADIUM - PUNE':
        location = 'Maharastra_Cricket_Association_Pune.jpg'
        view = 'MAHARASTRA CRICKET ASSOCIATION STADIUM'

    elif stadium == 'M CHINNASWAMY STADIUM - BENGALURU':
        location = 'M_Chinnaswamy_Stadium.jpg'
        view = 'M CHINNASWAMY STADIUM'

    elif stadium == 'WANKHEDE STADIUM - MUMBAI':
        location = 'Wankhede_Stadium.jpg'
        view = 'WANKHEDE STADIUM'

    elif stadium == 'EDEN GARDENS - KOLKATA':
        location = 'Eden_Gardens.jpg'
        view = 'EDEN GARDENS'

    def stadium_stats(stadium):

        img = cv2.imread('assets/Images/venue_images/'+location)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        df0 = df.loc[(df['GROUND'] == view)]
        df1 = df0[['PLACE', 'GROUND', 'TOTAL MATCHES', 'MATCHES WON BATTING FIRST', 'MATCHES WON BATTING SECOND']]
        df2 = df0[['MATCHES WON WINNING TOSS', 'MATCHES WON LOSING TOSS', 'AVERAGE FIRST INNINGS SCORE',
                   'AVERAGE SECOND INNINGS SCORE', ]]
        df3 = df0[['HIGHEST TOTAL RECORDED', 'LOWEST TOTAL RECORDED', 'HIGHEST SCORE CHASED', 'LOWEST SCORE DEFENDED']]

        return \
            [html.Div
                ([
                html.H2('OVERALL STATS IN THE STADIUM',style={"display": "flex", "justifyContent": "center"}),
                html.H2(stadium, style={"display": "flex", "justifyContent": "center"}),
                html.Br(),
            ]),
                dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True, style={'text-align': 'center'}),
                dbc.Table.from_dataframe(df2, striped=True, bordered=True, hover=True, style={'text-align': 'center'}),
                dbc.Table.from_dataframe(df3, striped=True, bordered=True, hover=True, style={'text-align': 'center'}),
                html.Div(
                    [
                        dcc.Graph(figure=fig, config={'displayModeBar': True}),
                    ], style={"display": "flex", "justifyContent": "center"},
                )
            ]

    def analysis(stadium,teams):

        df = pd.read_excel('assets/Venue_Stats/'+stadium+'.xlsx')
        #df = pd.read_excel(stadium+'.xlsx')
        df0 = pd.DataFrame()
        df1 = pd.DataFrame()
        df_conc = pd.DataFrame()

        if len(df.loc[(df['TEAM 1'] == teams)]) >= 1 or len(df.loc[(df['TEAM 2'] == teams)]) >= 1:

            df0 = df.loc[(df['TEAM 1'] == teams)]
            df1 = df.loc[(df['TEAM 2'] == teams)]

            '''if len(df0) >= 1 and len(df1) <= 1:
                df_conc = df0
                df_conc.reset_index(drop=True)

            elif len(df0) <= 1 and len(df1) >= 1:
                df_conc = df1
                df_conc.reset_index(drop=True)

            elif len(df0) >= 1 and len(df1) >= 1:
                df_conc = df0.append(df1)
                df_conc.reset_index(drop=True)'''

            #df_conc = pd.DataFrame(df_conc)
            
            #df_conc = df0.append(df1)
            df_conc = pd.concat([df0,df1])
            df_conc.reset_index(drop=True)

            data_table = dbc.Table.from_dataframe(df_conc, striped=True, bordered=True, hover=True, style={'text-align': 'center'}),

            total_matches_played = len(df_conc)

            wins = len(df_conc.loc[(df_conc['WINNER'] == teams)])

            win_percentage = (wins / total_matches_played) * 100
            win_perc = 'THE WIN PERCENTAGE OF '+teams+' IN ODI AT '+stadium+' IS '+str(win_percentage)+'%'

        else:
            win_perc = teams+ ' HAS NOT PLAYED ANY GAMES AT '+stadium
            data_table = ''

        return [
            win_perc,
            #df_conc
            data_table
        ]


    if stadium == 'NARENDRA MODI STADIUM - AHMEDABAD' and (teams==teams):

        ou1,ou2,ou3,ou4,ou5 = stadium_stats(stadium)
        ou6,ou7 = analysis(stadium,teams)
        return [ou1,ou2,ou3,ou4,ou5,ou6,ou7]


    elif stadium == 'RAJIV GANDHI INTERNATIONAL STADIUM - HYDERABAD':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'HIMACHAL PRADESH CRICKET ASSOCIATION STADIUM - DHARAMSHALA':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'ARUN JAITLEY STADIUM - DELHI':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'MA CHIDAMBARAM STADIUM - CHENNAI':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'BHARAT RATNA SHRI ATAL BIHARI VAJPAYEE EKANA CRICKET STADIUM - LUCKNOW':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'MAHARASTRA CRICKET ASSOCIATION STADIUM - PUNE':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'M CHINNASWAMY STADIUM - BENGALURU':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'WANKHEDE STADIUM - MUMBAI':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]

    elif stadium == 'EDEN GARDENS - KOLKATA':

        ou1, ou2, ou3, ou4, ou5 = stadium_stats(stadium)
        ou6, ou7 = analysis(stadium, teams)
        return [ou1, ou2, ou3, ou4, ou5, ou6, ou7]