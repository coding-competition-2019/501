import dash_bootstrap_components as dbc
import dash_html_components as html
import utils

from typing import Tuple
from placesdata import Place


def create_table(places, activity: str) -> dbc.Table:
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
    if len(places) != 0:

        for index, place in enumerate(places):
            activities = place.activities

            ###
            # coordinates = coordinates['']
            # distance = geolocation.get_distance(coordinates)
            distance = 10000
            ###

            table_data.append(
                html.Tr(
                    [
                        html.Td(", ".join(activities)),
                        html.Td(place.name),
                        html.Td(", ".join([place.street, place.city])),
                        html.Td(place.url),
                        html.Td(f"{round(distance / 1000, 2)}km"),
                    ]
                )
            )
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
