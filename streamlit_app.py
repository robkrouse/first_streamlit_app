import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('ð¥£ wow')
streamlit.text('ðlook what i did')

streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
