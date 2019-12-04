import dash_bootstrap_components as dbc
import dash_html_components as html


def create_table(data: dict, activity: str) -> dbc.Table:
    table_header = [html.Thead(html.Tr([html.Th("Activity")]))]

    body = (
        [html.Tr([html.Td(value)]) for value in data[activity]]
        if activity in data
        else [html.Td("Activity not found")]
    )

    table_body = [html.Tbody(body)]

    return dbc.Table(table_header + table_body, bordered=True)
