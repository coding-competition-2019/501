import dash_bootstrap_components as dbc
import dash_html_components as html
import utils

from typing import Tuple


def get_data() -> Tuple[dict, dict]:
    data = utils.read_json("data/places.json")
    places = utils.read_json("data/places_transformed.json")
    return data, places


def create_table(activity: str) -> dbc.Table:

    data, all_places = get_data()

    table_header = [html.Thead(html.Tr([html.Th("Activities"), html.Th("Places")]))]

    body = (
        [
            html.Tr(
                [
                    html.Td(" ".join(data["places"][value]["activities"])),
                    html.Td(data["places"][value]["name"]),
                ]
            )
            for value in all_places["places"][activity]
        ]
        if activity in all_places["activity_list"]
        else [html.Td("Activity not found"), html.Td("")]
    )

    table_body = [html.Tbody(body)]

    return dbc.Table(table_header + table_body, bordered=True)
