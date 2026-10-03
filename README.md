# Module 7 — Wildfire time series and dashboard

The cleaned California wildfire file, `fires_clean.parquet`, is included beside
the Module 7 notebook. Keep the Module 7 folder in `~/dso576/07-time-series`.
The notebook reads the bundled file without editing it. It is a copy of the
Module 6 clean table.

The clean table retains `DISCOVERY_DATE` and `FIRE_SIZE`. One row represents one
reported wildfire occurrence.

1. Run `uv sync --frozen` in this folder and select its `.venv` as the notebook kernel.
2. Open `module07_wildfire_timeseries.ipynb`. The short example cells show
   calendar months and ordered operations on verified California source counts,
   plus `transform()` on a clearly labeled practice county table.
   In class, write the cells that build the monthly table and add `previous`,
   `change`, `running`, and `average_3m`. Then run the supplied plot cells and
   complete the four small-input function exercises. Save
   `outputs/monthly_wildfire.csv`.
3. Run `uv run streamlit run dashboard.py` in this folder to open the dashboard.
   Its plots use the columns you made in the notebook.
4. Check one selected year's count against the notebook before sharing a screenshot.

For quiz practice, ask your coding agent to **“Read tutor.md and tutor me for
Module 7.”** It will give you fresh, one-at-a-time questions and feedback on
your attempts.

You can also ask your coding agent to build or revise the Streamlit dashboard
and any HTML/CSS presentation. It can write substantial code for that work;
the one-question-at-a-time approach is for quiz practice.

The notebook and dashboard use the same pandas, Plotly, and Streamlit packages
as Module 6. The source is [USDA FPA FOD, seventh edition](https://doi.org/10.2737/RDS-2013-0009.7).
The original records are reports, so trends can reflect reporting practices as
well as fire activity. There is no forecasting task.
