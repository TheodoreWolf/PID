"""streamlit dashboard for the project"""
import time

import numpy as np
import plotly.express as px
import streamlit as st

import pid_utils

st.title("Introduction to PID Control")
st.write("Simple dashboard to demonstrate PID control")

st.sidebar.title("Settings")
kp = st.sidebar.slider(
    "Kp",
    0.0,
    1.0,
    0.4,
    0.01,
)
ki = st.sidebar.slider("Ki", 0.0, 1.0, 0.2, 0.01)
kd = st.sidebar.slider("Kd", 0.0, 1.0, 0.01, 0.01)
control_freq = st.sidebar.slider("Control frequency (s)", 0.01, 1.0, 0.1)
system_target = st.sidebar.slider("System target", 0.0, 10.0, 2.0)
noise = st.sidebar.slider("System noise", 0.0, 1.0, 0.1)
init_state = st.sidebar.slider("Initial state", 0.0, 10.0, 5.0)

# init vars
integral = 0.0
prev_error = 0.0
time_axis = [0.0]
states = [init_state]
errors = [prev_error]

# Create plot placeholder
plot_placeholder = st.empty()

while True:
    # need to update state properly
    state, integral, prev_error = pid_utils.run_pid(
        kp,
        ki,
        kd,
        noise,
        target=system_target,
        dt=control_freq,
        init_state=init_state,
        integral=integral,
        prev_error=prev_error,
    )
    # update the data
    time_axis.append(time_axis[-1] + control_freq)
    states.append(state)
    errors.append(prev_error)

    # plot the data
    fig = px.line(
        x=time_axis,
        y=states,
        title="Error: {:.3f}".format(np.mean(np.array(errors) ** 2)),
    )
    fig.update_layout(yaxis_title="State", xaxis_title="Time")
    fig.add_hline(y=system_target, line_dash="dot", line_color="blue")
    plot_placeholder.plotly_chart(fig)

    # update the state
    init_state = state
    states = states[-100:]
    time_axis = time_axis[-100:]

    # Pause for a short duration
    time.sleep(0.05)

    states = states[-100:]
    time_axis = time_axis[-100:]
    errors = errors[-100:]

    # Pause for a short duration
    time.sleep(0.001)
