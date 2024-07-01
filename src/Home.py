import streamlit as st

st.title("Introduction to PID Control")
st.write("Simple dashboard to demonstrate PID control")

st.markdown("## Equations")
st.latex(r'u(t) = K_p e(t) + K_i \int_0^t e(t) dt + K_d \frac{d}{dt} e(t)')
st.latex(r'\text{Where: } e(t) = r(t) - x(t), \text{is the error signal, the reference or target minus the current state}.')
st.latex(r'u(t) \text{is the control signal.}')
