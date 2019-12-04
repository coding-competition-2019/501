import dash_bootstrap_components as dbc
import dash_html_components as html

inputs = html.Div(
    [
        dbc.Input(
            placeholder="Please fill in an activity...",
            # valid=True,
            type="text",
            className="mb-3",
            id="activities-input",
        ),
        html.Div(id="activities-output"),
    ]
)
