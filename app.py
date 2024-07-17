import streamlit as st


@st.cache_data
def get_data():
    "get data from csv files"
    
    # to do

    return


def main():
    st.set_page_config(
        page_title="Chess Visualizations", 
        page_icon=":chess_pawn:", 
        layout="wide",
        menu_items={
            'About': "This app is made for a Data Visualization class in Ateneo de Manila University."
        }
    )

    st.title("Chess Visualizations :chess_pawn:")
    st.write("By Bryan Francisco, Ivan Mostajo, and Robin Vicente")

    st.divider()

    # Filters
    st.write("Filters")
    col1, col2, col3 = st.columns(3)
    with col1:
        time_control = option = st.selectbox(
            "Time Control",
            ("All", "A", "B", "C")
        )
    with col2:
        start_elo, end_elo = st.select_slider(
            "Select a range of elo rating",
            options=range(2300, 3001),
            value=(2300, 3000)
        )
    with col3:
        opening = option = st.selectbox(
            "Select an opening",
            ("All", "A", "B", "C")
        )


if __name__ == '__main__':
    main()