import dash
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1('みんな、なにが好き？')
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=1991)
