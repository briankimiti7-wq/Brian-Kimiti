"""Run with: python -m streamlit run app.py."""

import streamlit as st
from sqlalchemy.exc import SQLAlchemyError

from dashboard.views import ROLE_VIEW, alerts_view, assets_view, overview, records_view
from database.connection import database_engine, sample_data
from modules.monitoring import ROLES, dashboard_data, timestamp

st.set_page_config(page_title="TECM | Condition Monitoring", layout="wide")

with st.sidebar:
    st.title("TECM")
    st.caption("Transformer & Equipment Condition Monitoring")
    role = st.selectbox("Role view", list(ROLES), format_func=ROLES.get, key="role")
    page = st.radio("Workspace", ["Overview", "Alerts", "Assets", "Condition records"], key="page")

stations = list(dict.fromkeys(asset["station"] for asset in sample_data()["assets"]))
with st.sidebar:
    station = st.selectbox("Station", ["All stations", *stations], key="station")
    st.divider()
    st.caption("Demonstration data · East Africa Time")

try:
    engine = database_engine()
    data = dashboard_data(engine, None if station == "All stations" else station)
except (OSError, SQLAlchemyError):
    st.error("The dashboard database could not be opened. Check that the database folder is writable.")
    st.stop()

title, description = ROLE_VIEW[role] if page == "Overview" else (page, {
    "Alerts": "Review alert evidence and track follow-up.",
    "Assets": "Browse transformers and associated equipment.",
    "Condition records": "Browse sensor readings, oil tests, inspections, relay events, and maintenance logs.",
}[page])
st.title(title)
st.write(description)
st.caption(f'Sample snapshot · {timestamp(sample_data()["snapshot"])} · {station}')

if notice := st.session_state.pop("workflow_notice", ""):
    st.success(notice)

if page == "Overview":
    overview(engine, role, data)
elif page == "Alerts":
    alerts_view(engine, role, data)
elif page == "Assets":
    assets_view(data)
else:
    records_view(data)
