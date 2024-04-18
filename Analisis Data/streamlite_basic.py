import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Judul Utama
st.title("Selamat Datang di Aplikasi Analisis Data")

# Unique key for slider
slider_key = "unique_slider_key"

# Toggle untuk Basic Syntax
with st.expander("Basic Syntax"):

    # Kode Python
    code = """def hello():
    print("Halo, Streamlit!")"""
    st.code(code, language="python")

    # Teks
    st.text("Halo, calon praktisi data masa depan.")

    # Formula Matematika
    st.latex(
        r"""
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
    """
    )

    # Pengembangan Dashboard
    st.subheader("Pengembangan Dashboard")
    # Kode Python
    code = """def hello():
    print("Halo, Streamlit!")"""
    st.code(code, language="python")

    # Teks
    st.text("Halo, calon praktisi data masa depan.")

    # Formula Matematika
    st.latex(
        r"""
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
    """
    )

    # DataFrame
    st.subheader("DataFrame")
    # Dataframe
    df = pd.DataFrame(
        {
            "Kolom 1": [1, 2, 3, 4],
            "Kolom 2": [10, 20, 30, 40],
        }
    )
    st.write(df)

    # Metrik
    st.subheader("Metrik")
    # Metrik
    st.metric(label="Temperatur", value="28 °C", delta="1.2 °C")

    # JSON
    st.subheader("JSON")
    # JSON
    st.json(
        {
            "Kolom 1": [1, 2, 3, 4],
            "Kolom 2": [10, 20, 30, 40],
        }
    )

    # Chart
    st.subheader("Chart")
    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig=fig)

with st.expander("Basic Widget"):
    # Text Input
    st.subheader("Text Input")

    name = st.text_input(label="Nama Lengkap", value="")
    st.write("Nama: ", name)

    # Text-area
    st.subheader("Text Area")

    text = st.text_area("Feedback")
    st.write("Feedback: ", text)

    # number input
    st.subheader("Number Input")

    number = st.number_input(label="Umur")
    st.write("Umur: ", int(number), " tahun")

    # date input
    st.subheader("Date Input")

    date = st.date_input(label="Tanggal lahir", min_value=datetime.date(1900, 1, 1))
    st.write("Tanggal lahir:", date)

    # File Uploader
    st.subheader("File uploader")

    uploaded_file = st.file_uploader("Choose a CSV file")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    # Camera Input
    st.subheader("Camera Input")

    # picture = st.camera_input("Take a picture")
    # if picture:
    #     st.image(picture)

    # Button
    st.subheader("Button")

    if st.button("Say hello"):
        st.write("Hello there")

    # Checkbox
    st.subheader("Checkbox")

    agree = st.checkbox("I agree")

    if agree:
        st.write("Welcome to MyApp")

    # Radiobutton
    st.subheader("Radio button")

    genre = st.radio(
        label="What's your favorite movie genre",
        options=("Comedy", "Drama", "Documentary"),
        horizontal=False,
    )

    # Select Box
    st.subheader("Select Box")

    genre = st.selectbox(
        label="What's your favorite movie genre",
        options=("Comedy", "Drama", "Documentary"),
    )

    # Multi select
    st.subheader("Multi select")

    genre = st.multiselect(
        label="What's your favorite movie genre",
        options=("Comedy", "Drama", "Documentary"),
    )

    # Slider
    st.subheader("Slider")

    values = st.slider(
        label="Select a range of values", min_value=0, max_value=100, value=(0, 100)
    )
    st.write("Values:", values)

# Sidebar
with st.sidebar:
    st.text("Ini merupakan sidebar")
    values = st.slider(
        label="Select a range of values",
        min_value=0,
        max_value=100,
        value=(0, 100),
        key=slider_key,
    )
    st.write("Values:", values)

# Columns
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Container
with st.container():
    st.write("Inside the Container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

st.write("Outside the container")

# Keterangan
st.caption("Hak Cipta (c) 2023")
