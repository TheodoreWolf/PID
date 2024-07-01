"""streamlit dashboard for the project"""
import streamlit as st
import plotly.express as px
import numpy as np
import pid_utils
import time

# Comibine with first running decorator
@st.cache_data(persist=True)
def run_on_startup():
    return [], []


# Ensure the startup function is run
states, targets = run_on_startup()

st.title("Welcome to the Streamlit Dashboard for the project")
st.write(
    "This is a dashboard for the project. You can use this dashboard to interact with the project and see the results."
)
system_select = st.selectbox("System", ["System 1", "System 2"])
# reset = st.button("Reset", on_click=reset_vals)

st.sidebar.title("Settings")
kp = st.sidebar.slider(
    "Kp",
    0.0,
    10.0,
    0.4,
    0.01,
)
ki = st.sidebar.slider("Ki", 0.0, 10.0, 0.2, 0.01)
kd = st.sidebar.slider("Kd", 0.0, 10.0, 0.01, 0.01)
control_freq = st.sidebar.slider("Control frequency (s)", 0.1, 1.0, 0.1, 0.01)
system_target = st.sidebar.slider("System target", 0.0, 10.0, 2.0)
noise = st.sidebar.slider("System noise", 0.0, 1.0, 0.01)

plot_placeholder = st.empty()
init_state = 1.0
# need to cache current states and targets somehow
while True:
    # need to update state properly
    state, controls = pid_utils.run_pid(
        kp, ki, kd, noise, target=system_target, dt=control_freq, init_state=init_state
    )
    targets.append(system_target)
    states.append(state)
    fig = px.line(y=states, title="System state")
    plot_placeholder.plotly_chart(fig)
    init_state = state
    # Pause for a short duration
    time.sleep(1)


# fig.add_hline(y=system_target, line_dash="dot", line_color="blue")
