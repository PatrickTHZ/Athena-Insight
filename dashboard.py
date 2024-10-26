import dash
from dash import dcc, html, Output, Input
import plotly.io as pio

# Initialize the Dash app
app = dash.Dash(__name__)

# Load Goanna Test Flight Figures from JSON files
goanna_velocity_fig = pio.read_json("DashboardGraphs/goanna_velocity_fig.json")
goanna_acceleration_fig = pio.read_json("DashboardGraphs/goanna_acceleration_fig.json")
goanna_altitude_fig = pio.read_json("DashboardGraphs/goanna_altitude_fig.json")
goanna_3d_flight_fig = pio.read_json("DashboardGraphs/goanna_3d_flight_fig.json")

# Load Mullaley Test Flight Figures from JSON files
mullaley_velocity_fig = pio.read_json("DashboardGraphs/mullaley_velocity_fig.json")
mullaley_acceleration_fig = pio.read_json("DashboardGraphs/mullaley_acceleration_fig.json")
mullaley_altitude_fig = pio.read_json("DashboardGraphs/mullaley_altitude_fig.json")
mullaley_3d_flight_fig = pio.read_json("DashboardGraphs/mullaley_3d_flight_fig.json")

# Mapping each test flight to its corresponding figures
figures = {
    "goanna": {
        "velocity": goanna_velocity_fig,
        "acceleration": goanna_acceleration_fig,
        "altitude": goanna_altitude_fig,
        "3d_flight": goanna_3d_flight_fig,
    },
    "mullaley": {
        "velocity": mullaley_velocity_fig,
        "acceleration": mullaley_acceleration_fig,
        "altitude": mullaley_altitude_fig,
        "3d_flight": mullaley_3d_flight_fig,
    }
}

# Adjust figure layout
def update_figure_layout(fig):
    fig.update_layout(
        autosize=True,
        margin=dict(l=30, r=20, t=40, b=20),
        height = 150
         
    )
    return fig

# APP LAYOUT
app.layout = html.Div([
    # html.H1("UTS Rocketry Flight Path Analysis Dashboard", className="header"),
     html.Div([
        html.Img(src='/assets/Rocketry_Logo.png', className="logo"), 
        html.H1("UTS Rocketry Flight Path Analysis Dashboard", className="header")
    ], className="header-container"),
    
    # Dropdown for selecting the test flight
    html.Div([
        html.Label("Select Test Flight:", className="dropdown-label"),
        dcc.Dropdown(
            id='flight-dropdown',
            options=[
                {'label': 'Goanna Test Flight', 'value': 'goanna'},
                {'label': 'Mullaley Test Flight', 'value': 'mullaley'}
            ],
            value='goanna',
            className="dropdown"
        )
    ], className="dropdown-container"),

    # Graph containers
    html.Div([
        html.Div([
            html.H3("Velocity over Time", className="graph-title"),
            dcc.Graph(id='velocity-graph')
        ], className="graph-container"),

        html.Div([
            html.H3("Acceleration over Time", className="graph-title"),
            dcc.Graph(id='acceleration-graph')
        ], className="graph-container"),
    ], className="graph-row"),

    html.Div([
        html.Div([
            html.H3("Altitude over Time", className="graph-title"),
            dcc.Graph(id='altitude-graph')
        ], className="graph-container"),

        html.Div([
            html.H3("3D Flight Path", className="graph-title"),
            dcc.Graph(id='flight-3d-graph')
        ], className="graph-container"),
    ], className="graph-row"),
])

# Update graphs based on dropdown selection
@app.callback(
    [Output('velocity-graph', 'figure'),
     Output('acceleration-graph', 'figure'),
     Output('altitude-graph', 'figure'),
     Output('flight-3d-graph', 'figure')],
    [Input('flight-dropdown', 'value')]
)
def update_graphs(selected_flight):
    # Retrieve the relevant figures based on the selected flight
    selected_figures = figures[selected_flight]
    
    return (selected_figures['velocity'],
            selected_figures['acceleration'],
            selected_figures['altitude'],
            selected_figures['3d_flight'])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

