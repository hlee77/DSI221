import streamlit as st
import pandas as pd
import pickle



st.title("Austen or Poe?")
st.subheader("Who do you write like?")

page = st.sidebar.selectbox(
    'Page',
    ('About', 'Dallae', 'EDA', 'Predicting')
)

if page == 'About':
    st.subheader('About this project')
    st.write("""This is a streamlit app.

It will tell you who you write like, etc.""")

elif page =='Dallae':
    st.subheader("Dallae's Daily Schedule")
    st.title('What is Dallae going to do today?')
    model_1, model_2 = st.tabs(["Food", "Walk"])
    with model_1:
        st.write("Hello Dallae, it's time to eat.")
        number = st.slider("How many times do you wanna eat? Choose a number", 0,3)

        st.metric("Number of times to eat", number)


    with model_2:
        st.write("Hello Dallae, it's time to walk.")
        number = st.slider("How long do you wanna walk?", 30,100)

        st.metric("Walking minutes", number)

elif page =='EDA':
    st.subheader('Exploration Nation!')

elif page == 'Predicting':
    st.title('Who do you write like?')
    model_1, model_2 = st.tabs(["Model 1", "Model 2"])
    with model_1:
        st.write("Hello Model 1!")
    with model_2:
        st.write("Hello Model 2!")
        number = st.slider("Choose a number", 0,100)

        st.metric("My number", number)

