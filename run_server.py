import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from layout import navbar, body, dropdown

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, dropdown, body])


@app.callback(Output("item-clicks", "children"), [Input("dropdown-button", "n_clicks")])
def count_clicks(n):
    if n:
        return f"Button clicked {n} times."
    return "Button not clicked yet."


if __name__ == "__main__":
    app.run_server()
