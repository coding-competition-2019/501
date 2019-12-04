import dash_table
import dash_bootstrap_components as dbc
import dash_html_components as html
import utils
import pandas as pd

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

    if activity:
        first_col = f"{activity.upper()} and other activities"
    else:
        first_col = "Activities"

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th(first_col),
                    html.Th("Places"),
                    html.Th("Address"),
                    html.Th("Url"),
                ]
            )
        )
    ]

    table_data: list = []
    if activity in all_places["activity_list"]:
        for index, value in enumerate(all_places["places"][activity]):
            ###
            # Vlad Function here (returns coordinates and distance from us. Takes html.Td(data[value][1] <- This is a place)
            ###
            table_data.append(
                html.Tr(
                    [
                        html.Td(", ".join(data[value][0])),
                        html.Td(data[value][1].name),
                        html.Td(data[value][1].street),
                        html.Td(data[value][1].url),
                    ]
                )
            )
            # table_data.append(
            #     [
            #         ", ".join(data[value][0]),
            #         data[value][1].name,
            #         data[value][1].street,
            #         data[value][1].url,
            #     ]
            # )
            if index == 100:
                break
    else:
        table_data.extend([html.Td(""), html.Td("")])
        # table_data.append([""])

    # table_data = pd.DataFrame.from_records(
    #     table_data, columns=[first_col, "Places", "Address", "Url"]
    # )
    table_body = [html.Tbody(table_data)]

    # return dash_table.DataTable(
    #     data=table_data,
    #     columns=[{"id": c, "name": c} for c in table_data.columns],
    #     style_table={"maxHeight": "300px", "overflowY": "scroll"},
    # )

    return dbc.Table(
        table_header + table_body,
        bordered=True,
        dark=True,
        hover=True,
        responsive="sm",
        striped=True,
    )
