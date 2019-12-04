import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import map_component as mc
import utils as utils

from dash.dependencies import Input, Output
from layout import navbar, body, map_component
from activities_table import create_table
from placesdata import PlacesData

from request_processing.geolocation import Geolocation

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([navbar, body, map_component])

test_table = {"swimming": ["1", "10"], "fitness": ["2"]}

data = PlacesData()


@app.callback(
    Output("activities-output", "children"), [Input("activities-input", "value")]
)
def output_text(value):
    return create_table(value)


@app.callback(
    Output(mc.MAP_ID, 'figure'),
    [Input("activities-input", "value")]
)
def _update_map(value):
    if utils.check_activity_matches_existing(data.get_activity_list(), value):
        geo = Geolocation(False)
        lat = list()
        lon = list()
        for n, place in enumerate(data.get_places_by_activity(value)):
            la, lo = geo.get_place(place)
            lat.append(la)
            lon.append(lo)
            if n > 5:
                break

        return mc.build_figure({'lat': lat, 'lon': lon})
    else:
        return mc.build_figure()


if __name__ == "__main__":
    app.run_server()
