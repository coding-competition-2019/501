import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import request_processing as rp

MAPBOX_KEY_NAME = 'mapbox-api-key'
MAP_ID = 'geo-map'
api_key = rp.load_key(MAPBOX_KEY_NAME)
DEF_LAT = 50.103642
DEF_LON = 14.390632
DEF_ZOOM = 15


def _get_current_coords():
    lat = DEF_LAT
    lon = DEF_LON
    return lat, lon


def create_map_component():
    fig = build_figure()
    graph = html.Div(dcc.Graph(id='geo-map', figure=fig), id='map-conent')
    return graph


def build_figure(coords=None):
    c_lat, c_lon = _get_current_coords()
    layout = go.Layout(
        title='Title',
        autosize=True,
        hovermode='closest',
        height=750,
        margin=go.Margin(l=0, r=0, t=45, b=10),
        mapbox=dict(
            accesstoken=api_key,
            bearing=0,
            center=dict(
                lat=c_lat,
                lon=c_lon,
            ),
            pitch=0,
            zoom=DEF_ZOOM,
        ),
        showlegend=False
    )
    center_point = go.Scattermapbox(
        lat=[c_lat],
        lon=[c_lon],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=14,
            color='rgb(242, 177, 172)'
        ),
        text=['NTK'],
    )

    if coords is not None:
        points = go.Scattermapbox(
            lat=coords['lat'],
            lon=coords['lon'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=14
            ),
            text=['NTK'],
        )
        data = [center_point, points]
    else:
        data = [center_point]

    return go.Figure(data=data, layout=layout)