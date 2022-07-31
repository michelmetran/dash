#!/usr/bin/env python
# coding: utf-8


from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


import pandas as pd

import plotly.graph_objects as go



quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude, radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()




app = Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter



# app = Dash(__name__)
# df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
# print(df.columns)
# print(df.head())

# app.layout = html.Div([
#     html.Div([
#         html.Div([
#             dcc.Dropdown(
#                 df['Indicator Name'].unique(),
#                 value='Fertility rate, total (births per woman)',
#                 id='xaxis-column'
#             ),
#             dcc.RadioItems(
#                 ['Linear', 'Log'],
#                 'Linear',
#                 id='xaxis-type',
#                 inline=True
#             )
#         ], style={'width': '48%', 'display': 'inline-block'}),

#         html.Div([
#             dcc.Dropdown(
#                 df['Indicator Name'].unique(),
#                 'Life expectancy at birth, total (years)',
#                 id='yaxis-column'
#             ),
#             dcc.RadioItems(
#                 ['Linear', 'Log'],
#                 'Linear',
#                 id='yaxis-type',
#                 inline=True
#             )
#         ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
#     ]),

#     dcc.Graph(id='indicator-graphic'),

#     dcc.Slider(
#         df['Year'].min(),
#         df['Year'].max(),
#         step=None,
#         id='year--slider',
#         value=df['Year'].max(),
#         marks={str(year): str(year) for year in df['Year'].unique()},

#     )
# ])


# @app.callback(
#     Output('indicator-graphic', 'figure'),
#     Input('xaxis-column', 'value'),
#     Input('yaxis-column', 'value'),
#     Input('xaxis-type', 'value'),
#     Input('yaxis-type', 'value'),
#     Input('year--slider', 'value'))
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type,
#                  year_value):
#     dff = df[df['Year'] == year_value]

#     fig = px.scatter(
#         x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
#         y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
#         hover_name=dff[dff['Indicator Name'] ==
#                        yaxis_column_name]['Country Name']
#     )

#     fig.update_layout(
#         margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
#         hovermode='closest'
#     )
#     fig.update_xaxes(
#         title=xaxis_column_name,
#         type='linear' if xaxis_type == 'Linear' else 'log'
#     )
#     fig.update_yaxes(
#         title=yaxis_column_name,
#         type='linear' if yaxis_type == 'Linear' else 'log'
#     )
#     return fig


# if __name__ == '__main__':
#     app.run_server(debug=True, port=8055)
