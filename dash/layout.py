import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """\
Donec id elit non mi porta gravida at eget metus.
Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

dropdown = html.Div(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("A button", id="dropdown-button"),
                dbc.DropdownMenuItem(
                    "Internal link", href="/l/components/dropdown_menu"
                ),
                dbc.DropdownMenuItem("External Link", href="https://github.com"),
                dbc.DropdownMenuItem(
                    "External relative",
                    href="/l/components/dropdown_menu",
                    external_link=True,
                ),
            ],
            label="Menu",
        ),
        html.P(id="item-clicks", className="mt-3"),
    ]
)
