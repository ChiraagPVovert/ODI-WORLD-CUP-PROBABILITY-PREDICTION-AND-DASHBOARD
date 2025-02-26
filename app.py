import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
import pandas as pd
pd.set_option('future.no_silent_downcasting', True)


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MATERIA],
		        meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}],
                external_scripts=["https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9935242688300411"],
                #serve_locally=False
                )

theme_switch = ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.MATERIA, dbc.themes.CYBORG])

adsense_code_001 = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9935242688300411"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-9935242688300411"
     data-ad-slot="4837649939"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

adsense_code_002 = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9935242688300411"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-9935242688300411"
     data-ad-slot="7085468933"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>"""

adsense_code_003 = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9935242688300411"
     crossorigin="anonymous"></script>
<!-- displayad1 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9935242688300411"
     data-ad-slot="1993473091"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""


PLOTLY_LOGO = 'https://overtideasandsolutions.in/img/overt-logo.png'

SIDEBAR = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.Col
                            ([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/app")
                            ])
                    ])
            ])
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
)

#app.layout = dbc.Container([header, dash.page_container], fluid=False)


app.layout = dbc.Container([
    dbc.Row(
        [
            #dbc.Col(html.Div(html.H2("CRIC-OVERT | ODI WORLD CUP")),align='center'),
            #dbc.Col(html.Div(html.Img(src=PLOTLY_LOGO)),align='center'),
            #dbc.Col(html.Iframe(srcDoc=adsense_code, width="100%", height="250")),
            dbc.Col(html.Script(adsense_code_001, type='text/javascript')),
            dbc.Col(html.Div([html.A([html.Img(src=PLOTLY_LOGO)], href='http://www.overtideasandsolutions.in/#:~:text=Overt%20ideas%20and%20solutions%20refer,in%20their%20presentation%20and%20execution.',target='_blank')]),align='center'),
            dbc.Col(html.Script(adsense_code_002, type='text/javascript')),
            #html.Script(ad_unit_code),
            #dbc.Col(html.Div(theme_switch), align='center')
        ],style={'textAlign':'center','height':'8rem'}
    ),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(html.Div([dbc.Button("FIXTURES AND RESULTS", color="primary", size="lg", href="https://www.cricketworldcup.com/fixtures",target='_blank'),]),align='center'),
            dbc.Col(html.Div([dbc.Button("POINTS TABLE", color="primary", size="lg", href="https://www.cricketworldcup.com/standings",target='_blank'),]),align='center'),
            dbc.Col(html.Div([dbc.Button("VENUES", color="primary", size="lg", href="https://www.cricketworldcup.com/venues",target='_blank'),]),align='center'),
            dbc.Col(html.Div([dbc.Button("LATEST NEWS", color="primary", size="lg", href="https://www.cricketworldcup.com/news",target='_blank'),]),align='center'),
            dbc.Col(html.Div([dbc.Button("PLAYER RANKINGS", color="primary", size="lg", href="https://www.icc-cricket.com/rankings/mens/player-rankings/odi",target='_blank'),]),align='center'),
            dbc.Col(html.Div([dbc.Button("TEAM RANKINGS", color="primary", size="lg", href="https://www.icc-cricket.com/rankings/mens/team-rankings/odi",target='_blank'),]),align='center'),
        ],style={'textAlign':'center'}
    ),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    SIDEBAR
                ], #xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
                   ),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                   )
        ]
    ),
    
    html.Hr(),

    dbc.Row(
        [
            dbc.Col(html.Script(adsense_code_003, type='text/javascript')),
        ],style={'textAlign':'center','height':'8rem'}
    ),


],fluid=True)


if __name__ == '__main__':
	#app.run_server(debug=True,port = 8501)# host = "0.0.0.0")
    app.run_server(debug=False, port=8501, host='0.0.0.0')
    #app.run_server(port = 8501)# host = "0.0.0.0")
