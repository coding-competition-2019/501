import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import map_component as mc

from inputs import inputs

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "501 team GitHub", href="https://github.com/coding-competition-2019/501"
            )
        ),
    ],
    brand="501 Activities APP",
    brand_href="#",
    sticky="top",
)

body = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.H2("There is always time for sport..."), html.P(""),], md=3,
                ),
            ]
        ),
        dbc.Row(
            [dbc.Col(html.Div(inputs)), dbc.Col(html.Div(mc.create_map_component()))]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("3 ML engineers and one web app"),
                        html.P(
                            " Thank you McKinsey coding competition for giving us an opprotunity to participate in this contest!"
                        ),
                        html.H4(
                            "Short story about our participation:"
                        ),
                        html.P(
                            "- Hey, do you want to participate in a hackathon?"
                        ),
                        html.P(
                            "- Yeah, why not?"
                        ),
                        html.P(
                            "- It's something related to web apps, though."
                        ),
                        html.P(
                            "- But none of us has ever done that! "
                            "*(thinks)* "
                            "Ok, let's go."
                        )
                    ],
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Vladislav Belov", className="card-title"),
                                html.H6("ML Engineer", className="card-subtitle"),
                                html.P("", className="card-text",),
                                dbc.CardLink(
                                    "GitHub link",
                                    href="https://github.com/salisaresama",
                                ),
                            ]
                        ),
                        style={"width": "18rem"},
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Marko Sahan", className="card-title"),
                                html.H6("ML Engineer", className="card-subtitle"),
                                html.P("", className="card-text",),
                                dbc.CardLink(
                                    "GitHub link", href="https://github.com/sahanmar",
                                ),
                            ]
                        ),
                        style={"width": "18rem"},
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Andrii Zakharchenko", className="card-title"),
                                html.H6("ML Engineer", className="card-subtitle"),
                                html.P("", className="card-text",),
                                dbc.CardLink(
                                    "GitHub link", href="https://github.com/ABlack-git",
                                ),
                            ]
                        ),
                        style={"width": "18rem"},
                    )
                ),
            ]
        ),
    ],
    className="mt-4",
)

# dropdown = html.Div(
#     [
#         dbc.DropdownMenu(
#             [
#                 dbc.DropdownMenuItem("A button", id="dropdown-button"),
#                 dbc.DropdownMenuItem(
#                     "Internal link", href="/l/components/dropdown_menu"
#                 ),
#                 dbc.DropdownMenuItem("External Link", href="https://github.com"),
#                 dbc.DropdownMenuItem(
#                     "External relative",
#                     href="/l/components/dropdown_menu",
#                     external_link=True,
#                 ),
#             ],
#             label="Menu",
#         ),
#         html.P(id="item-clicks", className="mt-3"),
#     ]
# )
# map_component = mc.create_map_component()
