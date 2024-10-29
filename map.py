import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig = go.Figure(data=go.Choropleth(
    locations = df['code'],
    z = df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'GnBu',
    colorbar_title =  'Most to Least Visited States'
))

fig.update_layout(
    geo_scope = 'usa',
    title_text = 'Visited States'
)
fig.show()