from dash import Dash, html

# Create the Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children="Hello, Dash!"),
    html.P(children="Welcome to your first Dash app."),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
