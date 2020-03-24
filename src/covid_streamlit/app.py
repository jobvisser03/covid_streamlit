import streamlit as st
import pandas as pd
import plotly.express as px

df_raw = pd.read_excel("https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-23.xlsx")

st.title('COVID-19 Exploration Dashboard')

st.write("RAW DATA")
st.write(df_raw)

## VISUALS

# Plot cases and deaths/pop per country over time (day)
df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
st.write(fig)

## PREDICTIONS

# DON't EVEN GO THERE

# Predict number of deaths 3 weeks after first infection
# y: nr. deaths
# X: smokers, demographics, air quality, income, nr. hospitals



