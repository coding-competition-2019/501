import dash_table
import dash_bootstrap_components as dbc
import dash_html_components as html
import utils
import pandas as pd

from typing import Tuple
from placesdata import Place

from request_processing.geolocation import Geolocation


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
    # geolocation = Geolocation(find_me=True)

    if activity:
        first_col = f"{activity.upper()} and other activities"
    else:
        first_col = "Activities"

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th(first_col),
                    html.Th("Place"),
                    html.Th("Address"),
                    html.Th("Url"),
                    html.Th("Distance from you"),
                ]
            )
        )
    ]

    table_data: list = []
    if activity in all_places["activity_list"]:

        for index, value in enumerate(all_places["places"][activity]):
            ###
            # coordinates = geolocation.get_place(data[value][1])
            # distance = geolocation.get_distance(coordinates)
            distance = 10000
            ###
            table_data.append(
                html.Tr(
                    [
                        html.Td(", ".join(data[value][0])),
                        html.Td(data[value][1].name),
                        html.Td(data[value][1].street),
                        html.Td(data[value][1].url),
                        html.Td(f"{round(distance/1000,2)}km"),
                    ]
                )
            )
            if index == 1:
                break
    else:
        table_data.extend([html.Td("") for _ in range(5)])

    table_body = [html.Tbody(table_data)]

    return dbc.Table(
        table_header + table_body,
        bordered=True,
        dark=True,
        hover=True,
        responsive="sm",
        striped=True,
    )
