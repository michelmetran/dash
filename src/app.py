import os
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    #
    html.H1(children='Hello World!'),

    html.H2('Hello World'),

    dcc.Dropdown(
        ['LA', 'NYC', 'MTL'],
        value='LA',
        id='dropdown'
    ),

    html.Div(children='Dash: A web application framework for Python.'),

    html.Div(id='display-value'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


@app.callback(
    Output('display-value', 'children'),
    [Input('dropdown', 'value')]
)
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server()
