import streamlit as st
import plotly.express as px
from agent import run_campaign_agent
from simulated_feedback import simulate_campaign_feedback
from execution import (
    get_all_campaigns,
    get_performance,
    agent_optimize,
    get_time_series_data,
    get_mock_post_engagements,
    launch_ad,
    launch_email_campaign
)

st.set_page_config(page_title="Autonomous Campaign Planner", layout="wide")

# Sidebar Inputs
st.sidebar.header("Campaign Inputs")
company_name = st.sidebar.text_input("Company Name")
product_idea = st.sidebar.text_area("Product Idea")
time_frame = st.sidebar.selectbox("Time Frame", ["1 week", "2 weeks", "1 month", "3 months", "6 months"])
campaign_goal = st.sidebar.selectbox("Campaign Goal", [
    "New Markets", "Increase Sales", "Conversion", "Retention", "Brand Awareness", "Boost Engagement"
])

if "campaign_generated" not in st.session_state:
    st.session_state["campaign_generated"] = False

st.title("Autonomous Campaign Planner")

if st.sidebar.button("Run Campaign Planner"):
    if not all([company_name, product_idea, campaign_goal]):
        st.warning("Please complete all inputs.")
    else:
        with st.spinner("Running autonomous campaign agent..."):
            parsed_output = run_campaign_agent(company_name, product_idea, campaign_goal, time_frame)

            # Simulate launching campaigns for graphable metrics
            launch_ad("Email", "Main Campaign Message")
            launch_ad("Instagram", "Main Campaign Message")
            launch_ad("LinkedIn", "Main Campaign Message")

            st.session_state["campaign_output"] = parsed_output
            st.session_state["campaign_generated"] = True

        st.success("Campaign strategy generated!")

# Display Campaign Results
if st.session_state["campaign_generated"]:
    parsed_output = st.session_state["campaign_output"]

    for section, content in parsed_output.items():
        if section == "Automation Tools":
            st.subheader(section)
            for tip in content:
                st.markdown(f"- {tip}")

        elif section == "A/B Test Variants":
            st.subheader(section)
            st.markdown(content)

        elif section == "Feedback Loop":
            st.subheader(section)
            st.markdown(content)

        elif section and content:
            with st.expander(section):
                st.markdown(content, unsafe_allow_html=True)

    # Visualizations
    st.subheader("Live Campaign Performance")
    performance = get_performance()
    for entry in performance:
        st.markdown(f"**{entry['platform']} – {entry['message']}**")
        st.markdown(f"CTR: `{entry['CTR']}`  ")
        st.markdown(f"ROI: `{entry['ROI']}`  ")
        st.markdown(f"Optimized: `{entry['optimized']}`")

    st.button("Run Optimizing Agent", on_click=agent_optimize)

    st.subheader("Performance Over Time (Simulated)")
    time_series = get_time_series_data()
    for series in time_series:
        fig_ctr = px.line(
            x=list(range(1, 5)),
            y=series["CTR_series"],
            labels={"x": "Week", "y": "CTR"},
            title=f"{series['platform']} – CTR Over Time"
        )
        st.plotly_chart(fig_ctr, use_container_width=True)

        fig_roi = px.line(
            x=list(range(1, 5)),
            y=series["ROI_series"],
            labels={"x": "Week", "y": "ROI"},
            title=f"{series['platform']} – ROI Over Time"
        )
        st.plotly_chart(fig_roi, use_container_width=True)

    st.subheader("Prototype Post Engagement (Mocked)")
    engagements = get_mock_post_engagements()
    for item in engagements:
        platform = item.pop("platform")
        st.markdown(f"**{platform}**")
        for k, v in item.items():
            st.markdown(f"{k.capitalize()}: {v}")

    # Real Email Campaign (demo purpose)
    st.button("Launch Email Campaign", on_click=launch_email_campaign)
