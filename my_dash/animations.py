import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.gapminder()
animations = {
    'Scatter': px.scatter(
        df, x="gdpPercap", y="lifeExp", animation_frame="year",
        animation_group="country", size="pop", color="continent",
        hover_name="country", log_x=True, size_max=55,
        range_x=[100,100000], range_y=[25,90]),
    'Bar': px.bar(
        df, x="continent", y="pop", color="continent",
        animation_frame="year", animation_group="country",
        range_y=[0,4000000000]),
}

app = dash.Dash(__name__)

app.layout = dbc.Container([
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=[{'label': x, 'value': x} for x in animations],
        value='Scatter'
    ),
    dcc.Graph(id="graph"),
    html.Div(id='info')
])

@app.callback(
    Output("graph", "figure"),
    [Input("selection", "value")])
def display_animated_graph(s):
    return animations[s]

@app.callback(
    Output("info", "children"),
    [Input("graph", "clickData"),
     Input('graph', 'hoverData')])
def display_animated_graph(clickdata, hoverdata):
    x1 = y1 = x2 = y2 = 'None'
    if clickdata is not None:
        x1 = clickdata['points'][0]['x']
        y1 = clickdata['points'][0]['y']
    if hoverdata is not None:
        x2 = hoverdata['points'][0]['x']
        y2 = hoverdata['points'][0]['y']
    content = dbc.Row([
            dbc.Col([
                html.H3('Clicked Data'),
                html.H5('x : ' + str(x1)),
                html.H5('y : ' + str(y1)),
            ],width=6),
            dbc.Col([
                html.H3('Hover Data'),
                html.H5('x : ' + str(x2)),
                html.H5('y : ' + str(y2)),
            ],width=6),
        ])
    return content

app.run_server(debug=True)
