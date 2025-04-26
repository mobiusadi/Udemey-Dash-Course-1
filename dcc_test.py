import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='SF'
    )
])

if __name__ == '__main__':
    app.run(debug=True)