import pydeck as pdk
import os 
import pandas as pd

# HEXAGON_LAYER_DATA = one_crime_choose_year(2022, "robbery") # noqa
path = os.path.expanduser("~/Downloads/map_Full_Data_data.csv") 

df = pd.read_csv(path, encoding = "utf-16", sep = '\t')

print(df.head)

view = pdk.data_utils.compute_view(df[["Longitude", "Latitude"]])
view.pitch = 45
view.bearing = 0
view.zoom = 4

column_layer = pdk.Layer(
    "ColumnLayer",
    data=df,
    get_position=["Longitude", "Latitude"],
    get_elevation="Value",
    elevation_scale=.1,
    radius=5000,
    get_fill_color=[180, 0, 200, 140],
    pickable=True,
    auto_highlight=True,
)

tooltip = {
    "html": "There were <b>{Value}</b> riders in 2019 at the <b>{Station}</b> Amtrak station.",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

r = pdk.Deck(
    column_layer,
    initial_view_state=view,
    tooltip=tooltip,
    map_provider="carto",
    map_style=pdk.map_styles.DARK,
)

r.to_html("column_layer.html")