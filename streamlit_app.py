import streamlit
import requests

streamlit.title('My Mom New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale,spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')


selected_fruits= streamlit.multiselect("Picks some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show= my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruit_to_show)
streamlit.header('Fruityvice Fruit Advice!')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())



fruitvice_data_normalize = pandas.json_normalize(fruityvice_response.json())

import snowfalke.connector

streamlit.dataframe(fruitvice_data_normalize)

fruit_choice= streamlit.text_input('what fruit do like information about?','kiwi')
streamlit.write('User Entered',fruit_choice)
