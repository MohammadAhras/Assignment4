import streamlit as st

st.set_page_config(page_title="Streamlit Website", page_icon="🌐", layout="centered")
st.title("Welcome to the My First Python Website")

st.sidebar.title("Naviation")
page= st.sidebar.radio("Go to", ["Home","About","Contact"])

if page == "Home":
    st.header("Home Page 🏠")
    st.write("This is simple Home Page Website build with python and streamlit.")
    name= st.text_input("What\'s your name?")
    if name:
        st.success(f"Hello {name}! Thanks for Visiting.")
    

elif page == "About":
    st.header("This is About Page")
    st.write("THis Website is build entirely using python and streamlit is under 15 minutes.")

elif page == "Contact":
    st.header("Contact Us")
    email = st.text_input("Your Email.")
    message = st.text_input("Your message.")
    if st.button("Submit"):
        st.success("Thank You! We Have received your message.")