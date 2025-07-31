import streamlit as st


# Page settings
st.set_page_config(
    page_title="GO - Concorrente",
    page_icon="assets/go-icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)

# Set up main page
col1, col2 = st.columns((6, 1))
col1.title("GO Concorrente")
col2.image("assets/golang-goper-logo.png", width=1000)
st.sidebar.image("assets/GOLANG.png")
action = st.sidebar.radio("Quer aprender a usar GO com concorrência?", ("Porque usar o GO para concorrência?",
                                                                  "Goroutines",
                                                                  "Channels",
                                                                  "Runtime do GO"))