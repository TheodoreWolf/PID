import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Function to generate new data
def get_new_data():
    return np.random.rand()

# Initialize the data
x = [0]
y = [get_new_data()]

# Streamlit application
st.title('Real-Time Data Plotting')

# Create a placeholder for the plot
plot_placeholder = st.empty()

# Start the real-time plotting
while True:
    # Get new data
    x.append(x[-1] + 1)
    y.append(get_new_data())

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Update the plot in the placeholder
    plot_placeholder.pyplot(fig)

    