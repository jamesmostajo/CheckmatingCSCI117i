import streamlit as st
import random
# import pyfile

random.seed(121415)


@st.cache_data
def get_data():
    "get data from csv files"
    
    # to do

    return

def show_checkmate_heatmap():
    import plotly.express as px
    
    st.subheader("Where do pieces move to checkmate?")

    data = [[random.randint(1, 1000) for _ in range(8)] for _ in range(8)]
    # data = pyfile.func()

    fig = px.imshow(data,
                    labels=dict(color="Checkmates"),
                    x=list("abcdefgh"),
                    y=list("12345678"),
                    height = 690
                   )


    st.plotly_chart(fig, theme="streamlit")


def main():
    st.set_page_config(
        page_title="Chess Visualizations", 
        page_icon=":chess_pawn:", 
        layout="centered",
        menu_items={
            'About': "This app is made for a Data Visualization class in Ateneo de Manila University."
        }
    )

    st.title("Chess Visualizations :chess_pawn:")
    st.write("By Bryan Francisco, Ivan Mostajo, and Robin Vicente")

    st.divider()

    # Filters
    st.write("Filters")
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        time_control = option = st.selectbox(
            "Time Control",
            ("All", "A", "B", "C")
        )
    with col2:
        start_elo, end_elo = st.select_slider(
            "Select a range of elo rating",
            options=range(2300, 3532),
            value=(2300, 3531)
        )
    with col3:
        opening = option = st.selectbox(
            "Select an opening",
            ("All", "A", "B", "C")
        )

    show_checkmate_heatmap()


if __name__ == '__main__':
    main()
