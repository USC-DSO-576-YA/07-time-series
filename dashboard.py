"""Monthly California wildfire dashboard from the Module 7 notebook output."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("California wildfire reports over time")
st.caption("USDA FPA FOD, 1992–2024. Counts are reported records, not all fires.")

monthly_path = Path(__file__).resolve().parent / "outputs" / "monthly_wildfire.csv"
monthly = pd.read_csv(monthly_path, parse_dates=["month"])
required = {"fires", "known_acres", "average_3m", "change", "running"}
missing = sorted(required.difference(monthly.columns))
if missing:
    st.error(f"Finish the notebook columns and save the monthly file: {', '.join(missing)}")
    st.stop()

years = sorted(monthly["month"].dt.year.unique())
year = st.selectbox("Year", years, index=len(years) - 1)
shown = monthly.loc[monthly["month"].dt.year == year]

st.metric("Reported fires", f"{shown['fires'].sum():,}")
st.metric("Known reported acres", f"{shown['known_acres'].sum():,.0f}")

trend = shown.melt(
    id_vars="month", value_vars=["fires", "average_3m"],
    var_name="series", value_name="reported fires",
)
st.plotly_chart(px.line(trend, x="month", y="reported fires", color="series"),
                use_container_width=True)
st.plotly_chart(px.bar(shown, x="month", y="change",
                       title="Change from previous month in reported fires"),
                use_container_width=True)
st.plotly_chart(px.line(shown, x="month", y="running",
                        title="Running reported fires since first available month"),
                use_container_width=True)
st.plotly_chart(px.bar(shown, x="month", y="known_acres",
                       labels={"known_acres": "Known reported acres"}),
                use_container_width=True)

st.caption("The three-month average uses the selected month and two earlier calendar months, including months in the previous year. The running count starts at the first available month and does not reset each year. Acres are final reported sizes for fires discovered that month, not distinct land burned during that month.")
