"""
Na tentativa de obter o animated frame, descobri qu enão existe call back que retorne o número do frame...

Contornaram isando interval....
https://stackoverflow.com/questions/68645115/is-there-a-way-to-extract-the-current-frame-from-a-plotly-figure/68653582#68653582
"""

import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

# Build App
app = Dash(__name__)

# CConstruct a figure with frames
frames = [go.Frame(name=n, data=go.Scatter(y=np.random.uniform(1, 5, 50))) for n
          in range(8)]
fig = go.Figure(data=frames[0].data, frames=frames)

app.layout = html.Div(
    [
        dcc.Graph(id="graph", figure=fig),
        html.Button(
            "Play",
            id="dashPlay",
            n_clicks=0
        ),
        dcc.Slider(
            id="dashSlider",
            min=0,
            max=len(frames) - 1,
            value=0,
            marks={i: {"label": str(i)} for i in range(len(frames))}
        ),
        dcc.Interval(
            id="animateInterval",
            interval=400,
            n_intervals=0,
            disabled=True
        ),
        html.Div(id="whichframe", children=[])
    ],
)


# core update of figure on change of dash slider
@app.callback(
    Output("whichframe", "children"),
    Output("graph", "figure"),
    Input("dashSlider", "value"),
)
def set_frame(frame):
    if frame:
        tfig = go.Figure(
            fig.frames[frame].data,
            frames=fig.frames,
            layout=fig.layout
        )
        try:
            tfig.layout['sliders'][0]['active'] = frame
        except IndexError:
            pass
        return frame, tfig
    else:
        return 0, fig


# start / stop Interval to move through frames
@app.callback(
    Output("animateInterval", "disabled"),
    Input("dashPlay", "n_clicks"),
    State("animateInterval", "disabled"),
)
def play(n_clicks, disabled):
    return not disabled


@app.callback(
    Output("dashSlider", "value"),
    Input("animateInterval", "n_intervals"),
    State("dashSlider", "value")
)
def do_animate(i, frame):
    if frame < (len(frames) - 1):
        frame += 1
    else:
        frame = 0
    return frame


if __name__ == '__main__':
    app.run_server(debug=True)
