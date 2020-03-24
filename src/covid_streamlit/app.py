import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df_raw = pd.read_excel("https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-23.xlsx")
df_raw.rename(columns={"Countries and territories": 'country'}, inplace=True)

st.title('COVID-19 Exploration Dashboard')

if st.checkbox('Show raw data'):
    st.write(df_raw)

## VISUALS

# Plot cases and deaths/pop per country over time (day)
df_plot = df_raw.loc[(df_raw['country'].isin(['Netherlands', 'Germany', 'Italy', 'China'])) & \
                    (df_raw['Cases'] >= 0) & \
                    (df_raw['Month'] == 3)].sort_values('Day', ascending=True)

fig = px.scatter(df_plot, x="Cases", y="Deaths", animation_frame="Day", animation_group="country",
           size="Cases", color="country", hover_name="country", facet_col="country",
           log_x=False, size_max=45, range_x=[0,10000], range_y=[0,1000])

st.write(fig)

## PREDICTIONS

# DON't EVEN GO THERE

# Predict number of deaths 3 weeks after first infection
# y: nr. deaths
# X: smokers, demographics, air quality, income, nr. hospitals



