import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_5000 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import odi_world_cup_analysis_2023
import average_scores
from plotly.subplots import make_subplots

dash.register_page(__name__,name = 'ODI WORLD CUP 2023')

df1 = odi_world_cup_analysis_2023.most_toss_won()
df2 = odi_world_cup_analysis_2023.most_toss_lost()
df3 = odi_world_cup_analysis_2023.most_matches_won()
df4 = odi_world_cup_analysis_2023.most_matches_lost()
df5 = odi_world_cup_analysis_2023.most_won_toss_choose_chase()
df6 = odi_world_cup_analysis_2023.most_lost_toss_option_chase()
df7 = odi_world_cup_analysis_2023.most_won_toss_choose_set_target()
df8 = odi_world_cup_analysis_2023.most_lost_toss_option_set_target()
df9 = odi_world_cup_analysis_2023.most_matches_won_after_winning_the_toss()
df10 = odi_world_cup_analysis_2023.most_matches_won_after_losing_the_toss()
df11 = odi_world_cup_analysis_2023.most_matches_lost_after_winning_the_toss()
df12 = odi_world_cup_analysis_2023.most_matches_lost_after_losing_the_toss()
df13 = odi_world_cup_analysis_2023.most_matches_won_after_winning_the_toss_and_chasing()
df14 = odi_world_cup_analysis_2023.most_matches_won_after_winning_the_toss_and_set_target()
df15 = odi_world_cup_analysis_2023.most_matches_won_after_losing_the_toss_and_chasing()
df16 = odi_world_cup_analysis_2023.most_matches_won_after_losing_the_toss_and_set_target()
df17 = odi_world_cup_analysis_2023.most_matches_lost_after_winning_the_toss_and_chasing()
df18 = odi_world_cup_analysis_2023.most_matches_lost_after_winning_the_toss_and_set_target()
df19 = odi_world_cup_analysis_2023.most_matches_lost_after_losing_the_toss_and_chasing()
df20 = odi_world_cup_analysis_2023.most_matches_lost_after_losing_the_toss_and_set_target()
df21 = odi_world_cup_analysis_2023.most_runs_scored_batting_first()
df22 = odi_world_cup_analysis_2023.most_runs_scored_batting_second()
df23 = odi_world_cup_analysis_2023.most_runs_scored_winning_toss_batting_first()
df24 = odi_world_cup_analysis_2023.most_runs_scored_winning_toss_batting_second()
df25 = odi_world_cup_analysis_2023.most_runs_scored_losing_toss_batting_first()
df26 = odi_world_cup_analysis_2023.most_runs_scored_losing_toss_batting_second()
df27 = odi_world_cup_analysis_2023.most_wickets_taken_bowling_first()
df28 = odi_world_cup_analysis_2023.most_wickets_taken_bowling_second()
df29 = odi_world_cup_analysis_2023.most_wickets_taken_wining_toss_bowling_first()
df30 = odi_world_cup_analysis_2023.most_wickets_taken_wining_toss_bowling_second()
df31 = odi_world_cup_analysis_2023.most_wickets_taken_losing_toss_bowling_first()
df32 = odi_world_cup_analysis_2023.most_wickets_taken_losing_toss_bowling_second()
df33 = odi_world_cup_analysis_2023.avg_runs_bat_first()
df34 = odi_world_cup_analysis_2023.avg_runs_bat_second()
df35 = odi_world_cup_analysis_2023.avg_runs_win_toss_bat_first()
df36 = odi_world_cup_analysis_2023.avg_runs_win_toss_bat_second()
df37 = odi_world_cup_analysis_2023.avg_runs_loss_toss_bat_first()
df38 = odi_world_cup_analysis_2023.avg_runs_loss_toss_bat_second()
df39 = odi_world_cup_analysis_2023.avg_wickets_bowl_first()
df40 = odi_world_cup_analysis_2023.avg_wickets_bowl_second()
df41 = odi_world_cup_analysis_2023.avg_wickets_win_toss_bowl_first()
df42 = odi_world_cup_analysis_2023.avg_wickets_win_toss_bowl_second()
df43 = odi_world_cup_analysis_2023.avg_wickets_loss_toss_bowl_first()
df44 = odi_world_cup_analysis_2023.avg_wickets_loss_toss_bowl_second()

fig_1 = make_subplots(rows=22, cols=2, shared_yaxes=True,subplot_titles=("TEAMS THAT HAS WON THE TOSS MOST TIMES",
                                                                         "TEAMS THAT HAS LOST THE TOSS MOST TIMES",
                                                                         'TEAMS THAT HAS WON MOST MATCHES',
                                                                         'TEAMS THAT HAS LOST MOST MATCHES',
                                                                        'TOTAL TIMES TEAMS CHASING AFTER WINNING THE TOSS',
                                                                        'TOTAL TIMES TEAMS CHASING AFTER LOSING THE TOSS',
                                                                        'TOTAL TIMES TEAMS DEFENDING AFTER WINNING THE TOSS',
                                                                        'TOTAL TIMES TEAMS DEFENDING AFTER LOSING THE TOSS',
                                                                        'MOST MATCHES WON AFTER WINNING THE TOSS',
                                                                        'MOST MATCHES WON AFTER LOSING THE TOSS',
                                                                        'MOST MATCHES LOST AFTER WINNING THE TOSS',
                                                                        'MOST MATCHES LOST AFTER LOSING THE TOSS',
                                                                        'MOST MATCHES WON WINNING TOSS AND CHASING',
                                                                        'MOST MATCHES WON WINNING TOSS AND DEFENDING',
                                                                        'MOST MATCHES WON LOSING TOSS AND CHASING',
                                                                        'MOST MATCHES WON LOSING TOSS AND DEFENDING',
                                                                        'MOST MATCHES LOST WINNING TOSS AND CHASING',
                                                                        'MOST MATCHES LOST WINNING TOSS AND DEFENDING',
                                                                        'MOST MATCHES LOST LOSING TOSS AND CHASING',
                                                                        'MOST MATCHES LOST LOSING TOSS AND DEFENDING',
                                                                        'MOST RUNS SCORED BATTING FIRST',
                                                                        'MOST RUNS SCORED BATTING SECOND',
                                                                        'MOST RUNS SCORED WINNING TOSS BATTING FIRST',
                                                                        'MOST RUNS SCORED WINNING TOSS BATTING SECOND',
                                                                        'MOST RUNS SCORED LOSING TOSS BATTING FIRST',
                                                                        'MOST RUNS SCORED LOSING TOSS BATTING SECOND',
                                                                        'MOST WICKETS TAKEN BOWLING FIRST',
                                                                        'MOST WICKETS TAKEN BOWLING SECOND',
                                                                        'MOST WICKETS TAKEN WINNING TOSS BOWLING FIRST',
                                                                        'MOST WICKETS TAKEN WINNING TOSS BOWLING SECOND',
                                                                        'MOST WICKETS TAKEN LOSING TOSS BOWLING FIRST',
                                                                        'MOST WICKETS TAKEN LOSING TOSS BOWLING SECOND',
                                                                        'AVERAGE RUNS SCORED BATTING FIRST',
                                                                         'AVERAGE RUNS SCORED BATTING SECOND',
                                                                         'AVERAGE RUNS SCORED WINNING TOSS BATTING FIRST',
                                                                         'AVERAGE RUNS SCORED WINNING TOSS BATTING SECOND',
                                                                         'AVERAGE RUNS SCORED LOSING TOSS BATTING FIRST',
                                                                         'AVERAGE RUNS SCORED LOSING TOSS BATTING SECOND',
                                                                         'AVERAGE WICKETS BOWLING FIRST',
                                                                         'AVERAGE WICKETS BOWLING SECOND',
                                                                         'AVERAGE WICKETS WINNING TOSS BOWLING FIRST',
                                                                         'AVERAGE WICKETS WINNING TOSS BOWLING SECOND',
                                                                         'AVERAGE WICKETS LOSING TOSS BOWLING FIRST',
                                                                         'AVERAGE WICKETS LOSING TOSS BOWLING SECOND',
																		 ))

fig_1.add_trace(go.Bar(x=df1['Team'], y=df1['Most Toss Won'],name='',text=df1['Most Toss Won'] ,textposition='auto',
                    marker=dict(color=df1['Most Toss Won'], coloraxis="coloraxis")),
              1, 1)
fig_1.add_trace(go.Bar(x=df2['Team'], y=df2['Most Toss Lost'],name='',text=df2['Most Toss Lost'] ,textposition='auto',
                    marker=dict(color=df2['Most Toss Lost'], coloraxis="coloraxis")),
              1, 2)
fig_1.add_trace(go.Bar(x=df3['Team'], y=df3['Most Matches Won'],name='',text=df3['Most Matches Won'] ,textposition='auto',
                    marker=dict(color=df3['Most Matches Won'], coloraxis="coloraxis")),
              2, 1)
fig_1.add_trace(go.Bar(x = df4['Team'], y=df4['Most Matches Lost'],name='',text=df4['Most Matches Lost'] ,textposition='auto',
                    marker=dict(color=df4['Most Matches Lost'], coloraxis="coloraxis")),
              2, 2)
fig_1.add_trace(go.Bar(x = df5['Team'], y=df5['Total times choose to chase winning the toss'],name='',text=df5['Total times choose to chase winning the toss'],textposition='auto',
                    marker=dict(color=df5['Total times choose to chase winning the toss'], coloraxis="coloraxis")),
              3, 1)
fig_1.add_trace(go.Bar(x = df6['Team'], y=df6['Total times set to chase losing the toss'],name='',text=df6['Total times set to chase losing the toss'],textposition='auto',
                    marker=dict(color=df6['Total times set to chase losing the toss'], coloraxis="coloraxis")),
              3, 2)
fig_1.add_trace(go.Bar(x = df7['Team'], y=df7['Total times choose to set target winning the toss'],name='',text=df7['Total times choose to set target winning the toss'] ,textposition='auto',
                    marker=dict(color=df7['Total times choose to set target winning the toss'], coloraxis="coloraxis")),
              4, 1)
fig_1.add_trace(go.Bar(x = df8['Team'], y=df8['Total times set to set target losing the toss'],name='',text=df8['Total times set to set target losing the toss'] ,textposition='auto',
                    marker=dict(color=df8['Total times set to set target losing the toss'], coloraxis="coloraxis")),
              4, 2)
fig_1.add_trace(go.Bar(x = df9['Team'], y=df9['Most matches won after winning the toss'],name='',text=df9['Most matches won after winning the toss'] ,textposition='auto',
                    marker=dict(color=df9['Most matches won after winning the toss'], coloraxis="coloraxis")),
              5, 1)
fig_1.add_trace(go.Bar(x = df10['Team'], y=df10['Most matches won after losing the toss'],name='',text=df10['Most matches won after losing the toss'] ,textposition='auto',
                    marker=dict(color=df10['Most matches won after losing the toss'], coloraxis="coloraxis")),
              5, 2)
fig_1.add_trace(go.Bar(x = df11['Team'], y=df11['Most matches lost after winnnig the toss'],name='',text=df11['Most matches lost after winnnig the toss'] ,textposition='auto',
                    marker=dict(color=df11['Most matches lost after winnnig the toss'], coloraxis="coloraxis")),
              6, 1)
fig_1.add_trace(go.Bar(x = df12['Team'], y=df12['Most matches lost after losing the toss'],name='',text=df12['Most matches lost after losing the toss'] ,textposition='auto',
                    marker=dict(color=df12['Most matches lost after losing the toss'], coloraxis="coloraxis")),
              6, 2)
fig_1.add_trace(go.Bar(x = df13['Team'], y=df13['Most matches won after winning the toss and chasing'],name='',text=df13['Most matches won after winning the toss and chasing'] ,textposition='auto',
                    marker=dict(color=df13['Most matches won after winning the toss and chasing'], coloraxis="coloraxis")),
              7, 1)
fig_1.add_trace(go.Bar(x = df14['Team'], y=df14['Most matches won after winning the toss and setting target'],name='',text=df14['Most matches won after winning the toss and setting target'] ,textposition='auto',
                    marker=dict(color=df14['Most matches won after winning the toss and setting target'], coloraxis="coloraxis")),
              7, 2)
fig_1.add_trace(go.Bar(x = df15['Team'], y=df15['Most matches won after losing the toss and chasing'],name='',text=df15['Most matches won after losing the toss and chasing'] ,textposition='auto',
                    marker=dict(color=df15['Most matches won after losing the toss and chasing'], coloraxis="coloraxis")),
              8, 1)
fig_1.add_trace(go.Bar(x = df16['Team'], y=df16['Most matches won after losing the toss and setting target'],name='',text=df16['Most matches won after losing the toss and setting target'] ,textposition='auto',
                    marker=dict(color=df16['Most matches won after losing the toss and setting target'], coloraxis="coloraxis")),
              8, 2)
fig_1.add_trace(go.Bar(x = df17['Team'], y=df17['Most matches lost after winning the toss and chasing'],name='',text=df17['Most matches lost after winning the toss and chasing'] ,textposition='auto',
                    marker=dict(color=df17['Most matches lost after winning the toss and chasing'], coloraxis="coloraxis")),
              9, 1)
fig_1.add_trace(go.Bar(x = df18['Team'], y=df18['Most matches lost after winning the toss and setting target'],name='',text=df18['Most matches lost after winning the toss and setting target'] ,textposition='auto',
                    marker=dict(color=df18['Most matches lost after winning the toss and setting target'], coloraxis="coloraxis")),
              9, 2)
fig_1.add_trace(go.Bar(x = df19['Team'], y=df19['Most matches lost after losing the toss and chasing'],name='',text=df19['Most matches lost after losing the toss and chasing'] ,textposition='auto',
                    marker=dict(color=df19['Most matches lost after losing the toss and chasing'], coloraxis="coloraxis")),
              10, 1)
fig_1.add_trace(go.Bar(x = df20['Team'], y=df20['Most matches lost after losing the toss and setting target'],name='',text=df20['Most matches lost after losing the toss and setting target'] ,textposition='auto',
                    marker=dict(color=df20['Most matches lost after losing the toss and setting target'], coloraxis="coloraxis")),
              10, 2)
fig_1.add_trace(go.Bar(x = df21['Team'], y=df21['Runs Scored'],hovertext=df21['Match'],name='',text=df21['Runs Scored'] ,#textposition='auto',
                    marker=dict(color=df21['Runs Scored'], coloraxis="coloraxis")),
              11, 1)
fig_1.add_trace(go.Bar(x = df22['Team'], y=df22['Runs Scored'],hovertext=df22['Match'],name='',text=df22['Runs Scored'] ,#textposition='auto',
                    marker=dict(color=df22['Runs Scored'], coloraxis="coloraxis")),
              11, 2)
fig_1.add_trace(go.Bar(x = df23['Team'], y=df23['Runs Scored'],hovertext=df23['Match'],name='',text=df23['Runs Scored'] ,#textposition='auto',
                    marker=dict(color=df23['Runs Scored'], coloraxis="coloraxis")),
              12, 1)
fig_1.add_trace(go.Bar(x = df24['Team'], y=df24['Runs Scored'],hovertext=df24['Match'],name='',text=df24['Runs Scored'] ,#textposition='auto',
                    marker=dict(color=df24['Runs Scored'], coloraxis="coloraxis")),
              12, 2)
fig_1.add_trace(go.Bar(x = df25['Team'], y=df25['Runs Scored'],hovertext=df25['Match'],name='',text=df25['Runs Scored'] ,#textposition='auto',
                    marker=dict(color=df25['Runs Scored'], coloraxis="coloraxis")),
              13, 1)
fig_1.add_trace(go.Bar(x = df26['Team'], y=df26['Runs Scored'],hovertext=df26['Match'],name='',text=df26['Runs Scored'] ,#textposition='auto',
                    marker=dict(color=df26['Runs Scored'], coloraxis="coloraxis")),
              13, 2)
fig_1.add_trace(go.Bar(x = df27['Team'], y=df27['Wickets Taken'],hovertext=df27['Match'],name='',text=df27['Wickets Taken'] ,#textposition='auto',
                    marker=dict(color=df27['Wickets Taken'], coloraxis="coloraxis")),
              14, 1)
fig_1.add_trace(go.Bar(x = df28['Team'], y=df28['Wickets Taken'],hovertext=df28['Match'],name='',text=df28['Wickets Taken'] ,#textposition='auto',
                    marker=dict(color=df28['Wickets Taken'], coloraxis="coloraxis")),
              14, 2)
fig_1.add_trace(go.Bar(x = df29['Team'], y=df29['Wickets Taken'],hovertext=df29['Match'],name='',text=df29['Wickets Taken'] ,#textposition='auto',
                    marker=dict(color=df29['Wickets Taken'], coloraxis="coloraxis")),
              15, 1)
fig_1.add_trace(go.Bar(x = df30['Team'], y=df30['Wickets Taken'],hovertext=df30['Match'],name='',text=df30['Wickets Taken'] ,#textposition='auto',
                    marker=dict(color=df30['Wickets Taken'], coloraxis="coloraxis")),
              15, 2)
fig_1.add_trace(go.Bar(x = df31['Team'], y=df31['Wickets Taken'],hovertext=df31['Match'],name='',text=df31['Wickets Taken'] ,#textposition='auto',
                    marker=dict(color=df31['Wickets Taken'], coloraxis="coloraxis")),
              16, 1)
fig_1.add_trace(go.Bar(x = df32['Team'], y=df32['Wickets Taken'],hovertext=df32['Match'],name='',text=df32['Wickets Taken'] ,#textposition='auto',
                    marker=dict(color=df32['Wickets Taken'], coloraxis="coloraxis")),
              16, 2)
fig_1.add_trace(go.Bar(x=df33['Team'], y=df33['Average Runs'],text=df33['Average Runs'],name='',textposition='auto',
                    marker=dict(color=df33['Average Runs'], coloraxis="coloraxis")),
              17, 1)
fig_1.add_trace(go.Bar(x=df34['Team'], y=df34['Average Runs'],text=df34['Average Runs'],name='',textposition='auto',
                    marker=dict(color=df34['Average Runs'], coloraxis="coloraxis")),
              17, 2)
fig_1.add_trace(go.Bar(x=df35['Team'], y=df35['Average Runs'],text=df35['Average Runs'],name='',textposition='auto',
                    marker=dict(color=df35['Average Runs'], coloraxis="coloraxis")),
              18, 1)
fig_1.add_trace(go.Bar(x=df36['Team'], y=df36['Average Runs'],text=df36['Average Runs'],name='',textposition='auto',
                    marker=dict(color=df36['Average Runs'], coloraxis="coloraxis")),
              18, 2)
fig_1.add_trace(go.Bar(x=df37['Team'], y=df37['Average Runs'],text=df37['Average Runs'],name='',textposition='auto',
                    marker=dict(color=df37['Average Runs'], coloraxis="coloraxis")),
              19, 1)
fig_1.add_trace(go.Bar(x=df38['Team'], y=df38['Average Runs'],text=df38['Average Runs'],name='',textposition='auto',
                    marker=dict(color=df38['Average Runs'], coloraxis="coloraxis")),
              19, 2)
fig_1.add_trace(go.Bar(x=df39['Team'], y=df39['Average Wickets'],text=df39['Average Wickets'],name='',textposition='auto',
                    marker=dict(color=df39['Average Wickets'], coloraxis="coloraxis")),
              20, 1)
fig_1.add_trace(go.Bar(x=df40['Team'], y=df40['Average Wickets'],text=df40['Average Wickets'],name='',textposition='auto',
                    marker=dict(color=df40['Average Wickets'], coloraxis="coloraxis")),
              20, 2)
fig_1.add_trace(go.Bar(x=df41['Team'], y=df41['Average Wickets'],text=df41['Average Wickets'],name='',textposition='auto',
                    marker=dict(color=df39['Average Wickets'], coloraxis="coloraxis")),
              21, 1)
fig_1.add_trace(go.Bar(x=df42['Team'], y=df42['Average Wickets'],text=df42['Average Wickets'],name='',textposition='auto',
                    marker=dict(color=df42['Average Wickets'], coloraxis="coloraxis")),
              21, 2)
fig_1.add_trace(go.Bar(x=df43['Team'], y=df43['Average Wickets'],text=df43['Average Wickets'],name='',textposition='auto',
                    marker=dict(color=df43['Average Wickets'], coloraxis="coloraxis")),
              22, 1)
fig_1.add_trace(go.Bar(x=df44['Team'], y=df44['Average Wickets'],text=df44['Average Wickets'],name='',textposition='auto',
                    marker=dict(color=df44['Average Wickets'], coloraxis="coloraxis")),
              22, 2)

fig_1['layout']['xaxis']['title']='Team'
#fig_1['layout']['yaxis']['title']='Most Toss Won'

fig_1['layout']['xaxis2']['title']='Team'
#fig_1['layout']['yaxis2']['title']='Most Toss Lost'

fig_1['layout']['xaxis3']['title']='Team'
#fig_1['layout']['yaxis3']['title']='Most Matches Won'

fig_1['layout']['xaxis4']['title']='Team'
#fig_1['layout']['yaxis4']['title']='Most Matches Lost'

fig_1['layout']['xaxis5']['title']='Team'
#fig_1['layout']['yaxis5']['title']='Total times choose to chase winning the toss'

fig_1['layout']['xaxis6']['title']='Team'
#fig_1['layout']['yaxis6']['title']='Total times set to chase losing the toss'

fig_1['layout']['xaxis7']['title']='Team'
#fig_1['layout']['yaxis7']['title']='Total times choose to set target winning the toss'

fig_1['layout']['xaxis8']['title']='Team'
#fig_1['layout']['yaxis8']['title']='Total times set to set target losing the toss'

fig_1['layout']['xaxis9']['title']='Team'
#fig_1['layout']['yaxis9']['title']='Most matches won after winning the toss'

fig_1['layout']['xaxis10']['title']='Team'
#fig_1['layout']['yaxis10']['title']='Most matches won after losing the toss'

fig_1['layout']['xaxis11']['title']='Team'
#fig_1['layout']['yaxis11']['title']='Most matches lost after winnnig the toss'

fig_1['layout']['xaxis12']['title']='Team'
#fig_1['layout']['yaxis12']['title']='Most matches lost after losing the toss'

fig_1['layout']['xaxis13']['title']='Team'
#fig_1['layout']['yaxis13']['title']='Most matches won after winning the toss and chasing'

fig_1['layout']['xaxis14']['title']='Team'
#fig_1['layout']['yaxis14']['title']='Most matches won after winning the toss and setting target'

fig_1['layout']['xaxis15']['title']='Team'
#fig_1['layout']['yaxis15']['title']='Most matches won after losing the toss and chasing'

fig_1['layout']['xaxis16']['title']='Team'
#fig_1['layout']['yaxis16']['title']='Most matches won after losing the toss and setting target'

fig_1['layout']['xaxis17']['title']='Team'
#fig_1['layout']['yaxis17']['title']='Most matches lost after winning the toss and chasing'

fig_1['layout']['xaxis18']['title']='Team'
#fig_1['layout']['yaxis18']['title']='Most matches lost after winning the toss and setting target'

fig_1['layout']['xaxis19']['title']='Team'
#fig_1['layout']['yaxis19']['title']='Most matches lost after losing the toss and chasing'

fig_1['layout']['xaxis20']['title']='Team'
#fig_1['layout']['yaxis20']['title']='Most matches lost after losing the toss and setting target'

fig_1['layout']['xaxis21']['title']='Team'
#fig_1['layout']['yaxis21']['title']='Runs Scored'

fig_1['layout']['xaxis22']['title']='Team'
#fig_1['layout']['yaxis22']['title']='Runs Scored'

fig_1['layout']['xaxis23']['title']='Team'
#fig_1['layout']['yaxis23']['title']='Runs Scored'

fig_1['layout']['xaxis24']['title']='Team'
#fig_1['layout']['yaxis24']['title']='Runs Scored'

fig_1['layout']['xaxis25']['title']='Team'
#fig_1['layout']['yaxis25']['title']='Runs Scored'

fig_1['layout']['xaxis26']['title']='Team'
#fig_1['layout']['yaxis26']['title']='Runs Scored'

fig_1['layout']['xaxis27']['title']='Team'
#fig_1['layout']['yaxis27']['title']='Wickets Taken'

fig_1['layout']['xaxis28']['title']='Team'
#fig_1['layout']['yaxis28']['title']='Wickets Taken'

fig_1['layout']['xaxis29']['title']='Team'
#fig_1['layout']['yaxis29']['title']='Wickets Taken'

fig_1['layout']['xaxis30']['title']='Team'
#fig_1['layout']['yaxis30']['title']='Wickets Taken'

fig_1['layout']['xaxis31']['title']='Team'
#fig_1['layout']['yaxis31']['title']='Wickets Taken'

fig_1['layout']['xaxis32']['title']='Team'
#fig_1['layout']['yaxis32']['title']='Wickets Taken'

fig_1['layout']['xaxis33']['title']='Team'
fig_1['layout']['xaxis34']['title']='Team'
fig_1['layout']['xaxis35']['title']='Team'
fig_1['layout']['xaxis36']['title']='Team'
fig_1['layout']['xaxis37']['title']='Team'
fig_1['layout']['xaxis38']['title']='Team'
fig_1['layout']['xaxis39']['title']='Team'
fig_1['layout']['xaxis40']['title']='Team'
fig_1['layout']['xaxis41']['title']='Team'
fig_1['layout']['xaxis42']['title']='Team'
fig_1['layout']['xaxis43']['title']='Team'
fig_1['layout']['xaxis44']['title']='Team'


fig_1.update_layout(width=1300, height=9000)
fig_1.update_layout(coloraxis=dict(colorscale='Agsunset'))#, showlegend=False)
fig_1.update_coloraxes(showscale=False)
fig_1.update_layout(showlegend=False)
#fig_1.update_xaxes(visible=False)
#fig_1.update_yaxes(visible=False)
#fig_1.show()


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
                    html.H3('ODI WORLD CUP 2023 ANALYSIS', style={'textAlign': 'center'}),
                    html.Br(),
                    dcc.Graph(figure=fig_1)
                ],xs=10, sm=10, md=10, lg=10, xl=10, xxl=10),
    ])
    ])
