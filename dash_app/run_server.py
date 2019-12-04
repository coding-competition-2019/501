import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from layout import navbar, body, dropdown
from inputs import inputs
from activities_table import create_table

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, inputs, dropdown, body])


test_table = {"swimming": ["1", "10"], "fitness": ["2"]}


@app.callback(Output("item-clicks", "children"), [Input("dropdown-button", "n_clicks")])
def count_clicks(n):
    if n:
        return f"Button clicked {n} times."
    return "Button not clicked yet."


@app.callback(
    Output("activities-output", "children"), [Input("activities-input", "value")]
)
def output_text(value):
    return create_table(value)


if __name__ == "__main__":
    app.run_server()
