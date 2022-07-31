import os
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    # Componentes HTML
    html.H1(children='Título 1', style={'text-align': 'center'}),
    html.H2(children='Título 2'),
    html.Br(),

    # ddd
    dcc.Markdown("""### Markdown"""),
    dcc.Markdown('*Teste*'),
    dcc.Markdown('ssss'),

    # Uma div aleatória
    html.Div(children='Dash: A web application framework for Python.'),


    # Dropdowns
    dcc.Dropdown(
        options=['LA', 'NYC', 'MTL'],
        value='LA',
        id='dropdown',
    ),
    dcc.Dropdown(
        id='dropdown2',
        multi=True,
        options=[
            {'label': '15', 'value': 2015},
            {'label': '16', 'value': 2016},
            {'label': '17', 'value': 2017},
            {'label': '18', 'value': 2018},
        ],
        value=2015,
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
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
        }
    ),

    # Outros
    # ddd
])


@app.callback(
    Output('display-value', 'children'),
    [Input('dropdown', 'value')],
)
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(
        debug=True
    )
