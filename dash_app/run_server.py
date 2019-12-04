import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

import map_component as mc
import utils as utils

from dash.dependencies import Input, Output
from layout import navbar, body
from activities_table import create_table, create_cards
from placesdata import PlacesData

from request_processing.geolocation import Geolocation

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([navbar, body])

test_table = {"swimming": ["1", "10"], "fitness": ["2"]}

data = PlacesData()


@app.callback(
    [Output("activities-output", "children"), Output(mc.MAP_ID, "figure")],
    [Input("activities-input", "value")],
)
def update_by_input(value):
    if utils.check_activity_matches_existing(data.get_activity_list(), value):
        geo = Geolocation(False)
        lat = list()
        lon = list()
        places = list()
        for n, place in enumerate(data.get_places_by_activity(value, limit=5)):
            la, lo = geo.get_place(place)
            lat.append(la)
            lon.append(lo)
            places.append(place)

        return (
            create_cards(places, value, {"lat": lat, "lon": lon}),
            mc.build_figure(
                {"lat": lat, "lon": lon, 'names': [p.name for p in places]}),
        )
    else:
        places = []
        return create_cards(places, value, None), mc.build_figure()


if __name__ == "__main__":
    app.run_server()
