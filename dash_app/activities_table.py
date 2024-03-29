import dash_bootstrap_components as dbc
import dash_html_components as html
import utils

from request_processing.geolocation import Geolocation
from typing import Tuple
from placesdata import Place


def create_card(name, address, distance, route_link):
    return dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4(name, className="card-title"),
                        html.P(address),
                        html.H6(f"Distance: {distance} km"),
                        dbc.CardLink('Directions',
                                     href=route_link)
                    ]
                )
            ))])


def creat_empty_card():
    return dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                )
            ))])


def create_cards(places, activity, coordinates):
    cards = list()
    geolocation = Geolocation(find_me=True)
    if len(places) != 0:
        for index, place in enumerate(places):
            coordinate = (coordinates["lat"][index], coordinates["lon"][index])
            distance = geolocation.get_distance(coordinate)
            route_link = geolocation.get_navigations(coordinate)
            distance = round(distance / 1000, 2)
            cards.append(create_card(place.name, place.get_address(), distance,
                                     route_link=route_link))
        return html.Div(cards)
    else:
        return html.Div([creat_empty_card()])


def create_table(places, activity: str, coordinates) -> dbc.Table:
    geolocation = Geolocation(find_me=True)

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
            coordinate = (coordinates["lat"][index], coordinates["lon"][index])
            distance = geolocation.get_distance(coordinate)
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
