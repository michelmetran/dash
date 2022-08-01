import geopandas as gpd
import plotly.express as px
from dash import Dash, dcc, html
from dotenv import dotenv_values, find_dotenv

# fig.show()
# https://plotly.com/python/scattermapbox/


config = dotenv_values(find_dotenv(usecwd=True))
MAPBOX_TOKEN = config['MAPBOX_TOKEN']

px.set_mapbox_access_token(MAPBOX_TOKEN)

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

fig = px.scatter_mapbox(
    geo_df,
    lat=geo_df.geometry.y,
    lon=geo_df.geometry.x,
    hover_name="name",
    zoom=1
)

app = Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
