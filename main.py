import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import pickle as pkl

# Sample data for demonstration
data = pd.DataFrame({
    'x': np.arange(10),
    'y1': np.random.rand(10),
    'y2': np.random.rand(10)
})

data2 = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 5, 8, 2, 7]
})

chart = alt.Chart(data2).mark_bar().encode(
    x='x:O',
    y='y:Q'
)
# fig_open = pkl.load(open('sinus.pickle','rb'))

# Streamlit app
st.title('Tata Motor Stock analysis')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.header("Tata Motors Stock Price")
# plt.plot(data['x'],data['y1'])
fig_open = pkl.load(open('sinus.pickle','rb'))
st.pyplot()
# st.vega_lite_chart(chart, use_container_width=True)
# Create two graphs side by side
col11, col12 = st.columns(2)

# Plot the first graph
with col11:
    st.subheader('After Training Graph')
    # plt.plot(data['x'], data['y1'])
    fig_open = pkl.load(open('trained.pickle','rb'))
    st.pyplot()

values = np.random.randint(1, 100, 5)  # Replace with your actual data
# Plot the second graph
with col12:
    st.subheader('LSTM Prediction')
    st.text(f"********************************")
    st.text(f"Day_1: {values[0]}")
    st.text(f"Day_1: {values[0]}")
    st.text(f"Day_1: {values[0]}")
    st.text(f"Day_1: {values[0]}")
    st.text(f"Day_1: {values[0]}")
    st.text(f"********************************")

# st.header('ARIMA')
# st.text('''
# Results of Dickey Fuller Test:
# Test Statistic                    0.471829
# p-value                           0.983991
# #Lags Used                       17.000000
# Number of Observations Used    7039.000000
# Critical Value (1%)              -3.431279
# Critical Value (5%)              -2.861951
# Critical Value (10%)             -2.566989
# ''')
# st.text("*******************************************************************************")
# st.header('Analysis')
# col21, col22 = st.columns(2)

# # Plot the first graph
# with col21:
#     st.subheader('Graph 1')
#     fig_open = pkl.load(open('mumean.pickle','rb'))
#     # plt.plot(data['x'], data['y1'])
#     st.pyplot()

# # values = np.random.randint(1, 100, 5)  # Replace with your actual data
# # Plot the second graph
# with col22:
#     st.subheader('Graph 1')
#     plt.plot(data['x'], data['y1'])
    
#     st.pyplot()
# st.text("*******************************************************************************")
# st.header("Prediction")
# col31, col32 = st.columns(2)

# # Plot the first graph
# with col31:
#     st.subheader('Graph 3')
#     plt.plot(data['x'], data['y1'])
#     st.pyplot()

# # values = np.random.randint(1, 100, 5)  # Replace with your actual data
# # Plot the second graph
# with col32:
#     st.subheader('Graph 4')
#     plt.plot(data['x'], data['y1'])
#     st.pyplot()
# st.text("*******************************************************************************")
# Display values in the same row with spaces
# st.text(f'Value 1: {values[0]} | Value 2: {values[1]} | Value 3: {values[2]} | Value 4: {values[3]} | Value 5: {values[4]}')    