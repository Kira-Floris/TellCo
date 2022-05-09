import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px


# project description
def description_function():
	pass

# data analysis
def analysis_function():
	pass

# model prediction testing
def ai_function():
	pass

# sidebar menu
with st.sidebar:
	selected = option_menu(
			menu_title = 'Menu',
			options = ['Project Description','Analysis', 'AI', 'About Me']
		)

if selected == 'Project Description':
	st.title('Project Description')
	description_function()

if selected == 'Analysis':
	st.title('Analysis')
	analysis_function()

if selected == 'AI':
	ai_function()

if selected == 'About Me':
	st.title('About Me')