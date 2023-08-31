import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
#Primeiro Grafico
# fig1 = go.Figure(
#     data=[go.Bar(x=[1, 2, 3, 4, 5], y=[1, 3, 2, 1, 2])],
#     layout=go.Layout(
#         title=go.layout.Title(text="Vai mostrar algo na tela")
#     )
# )
#
# fig1.show()

#Segundp Grafico
# fig2 = make_subplots(rows=1, cols=2)
# fig2.add_trace(go.Bar(y=[1, 4, 5], x=[6, 5, 2], marker_color="green"), row=1, col=1)
# fig2.add_trace(go.Scatter(y=[8, 2, 4, 5], x=[6, 5, 2, 7], marker_color="red", mode="lines"), row=1, col=2)
#
# fig2.show()

# criando pontos
t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode="markers"))
fig.show()
