#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:36:23 2024

@author: bikramgahley
"""

pip install streamlit matplotlib pandas

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Sidebar for user input
st.sidebar.header('Select a Feature to Visualize')
selected_feature = st.sidebar.selectbox('Feature', df.columns)

# Main Dashboard
st.title('Data Visualization Dashboard')

# Display dataset
st.write('## Dataset Preview')
st.dataframe(df.head())

# Plot
st.write(f'## {selected_feature} Distribution')
fig, ax = plt.subplots()
ax.hist(df[selected_feature], bins=20)
st.pyplot(fig)
