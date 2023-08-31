import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Frutas": ["Apple", "Oranges", "Banana", "Apple", "Oranges", "Banana"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    }
)

fig = px.bar(df, x="Frutas", y="Amount", color="City")

# ==================================
# LAyout

app.layout = html.Div(id="div1",
                      children=[
                          html.H1("Hello my Dash", id="h1"),
                          html.Div("Dash : Um FrameWord web para Python"),
                          dcc.Graph(figure=fig, id="graph")
                    ])
if __name__ == '__main__':
    app.run(debug=True)


