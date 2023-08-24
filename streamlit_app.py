import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Mom New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale,spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')


selected_fruits= streamlit.multiselect("Picks some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show= my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruit_to_show)
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruitvice_data_normalize = pandas.json_normalize(fruityvice_response.json())
    return fruitvice_data_normalize


streamlit.header('Fruityvice Fruit Advice!')
# streamlit.dataframe(fruitvice_data_normalize)
try:
  fruit_choice= streamlit.text_input('what fruit do like information about?')
  if not fruit_choice:
    streamlit.error('please select fruit to get infromation')
  else:
    fruit_get_back=get_fruitvice_data(fruit_choice)
    streamlit.dataframe(fruit_get_back)
except URLError as e:
  streamlit.error()
# streamlit.write('User Entered',fruit_choice)
streamlit.stop()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
# my_data_rows = my_cur.fetchall()
# streamlit.header("Fruit Load List:")

add_my_fruit=streamlit.text_input('what fruit would you like to add','jackfruit')
streamlit.write('Thank you for adding ',add_my_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")


