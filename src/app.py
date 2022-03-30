import os
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    #
    html.H1(children='Título 1'),

    #
    html.H2('Título 2'),

    # Uma div aleatória
    html.Div(children='Dash: A web application framework for Python.'),

    # Um espaço
    html.Br(),

    # Um dropdown
    dcc.Dropdown(
        ['LA', 'NYC', 'MTL'],
        value='LA',
        id='dropdown'
    ),

    #
    html.Div(id='display-value'),

    # Um gráfico estático
    html.H2('Gráfico Estático'),
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
    ),

    # Outros
    #ddd

])


@app.callback(
    [Input('dropdown', 'value')],
    Output('display-value', 'children'),
)
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server()
