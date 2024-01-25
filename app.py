import streamlit as st
import pandas as pd
import plotly.express as px

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d %H:%M:%S").dt.date

# Set up the Streamlit app
st.title("Precious Metal Prices 2018-2021")
st.markdown("The cost of precious metals between 2018 and 2021")

# Display dropdown for metal selection
metal = st.selectbox("Metal", options=data.columns[1:], index=0)

# Display date range selector
start_date = st.date_input("Start Date", value=data["DateTime"].min())
end_date = st.date_input("End Date", value=data["DateTime"].max())

# Filter the data based on the selected metal and date range
filtered_data = data.loc[(data["DateTime"] >= start_date) & (data["DateTime"] <= end_date)]

# Create a plotly plot for the filtered data
fig = px.line(
    filtered_data,
    title=f"{metal} Prices {start_date} to {end_date}",
    x="DateTime",
    y=metal,
    color_discrete_map={
        "Platinum": "#E5E4E2",
        "Gold": "gold",
        "Silver": "silver",
        "Palladium": "#CED0DD",
        "Rhodium": "#E2E7E1",
        "Iridium": "#3D3C3A",
        "Ruthenium": "#C9CBC8"
    }
)

# Update the plot layout
fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price (USD/oz)",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color="white"
    ),
)

# Display the plot
st.plotly_chart(fig)
