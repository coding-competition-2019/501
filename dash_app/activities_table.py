import dash_bootstrap_components as dbc
import dash_html_components as html
import utils

from typing import Tuple
from placesdata import Place


def get_data() -> Tuple[dict, dict]:
    data = utils.read_json("data/places.json")
    data = [
        (
            val["activities"],
            Place(
                val["name"],
                val["url"],
                val["address"]["street"],
                val["address"]["zipCode"],
                val["address"]["city"],
            ),
        )
        for val in data["places"]
    ]
    places = utils.read_json("data/places_transformed.json")
    return data, places


def create_table(activity: str) -> dbc.Table:

    data, all_places = get_data()

    table_header = [html.Thead(html.Tr([html.Th("All Activities"), html.Th("Places")]))]

    table_data: list = []
    if activity in all_places["activity_list"]:
        for index, value in enumerate(all_places["places"][activity]):
            ###
            # Vlad Function here (returns coordinates and distance from us. Takes html.Td(data[value][1] <- This is a place)
            ###
            table_data.append(
                html.Tr(
                    [html.Td(", ".join(data[value][0])), html.Td(data[value][1].name),]
                )
            )
            if index == 5:
                break
    else:
        table_data.extend([html.Td("Activity not found"), html.Td("")])

    table_body = [html.Tbody(table_data)]

    return dbc.Table(
        table_header + table_body,
        bordered=True,
        style={"maxHeight": "300px", "overflowY": "scroll"},
    )
