import streamlit as st
import random
import getHeatmap, getGamesNum

random.seed(121415)


@st.cache_data
def get_data():
    "get data from csv files"
    
    # to do

    return


def show_checkmate_heatmap(start_elo, end_elo):
    import plotly.express as px
    
    st.subheader("Where do pieces move to checkmate?")
    st.write("insert description here.")
    col1, col2, col3 = st.columns(3)

    with col1:
        filter_piece = st.selectbox(
                "Filter a piece",
                ("No Filter", "Pawn", "Knight", "Bishop", "Rook", "Queen", "King")
            )
        

    # data = [[random.randint(1, 1000) for _ in range(8)] for _ in range(8)]
    data = getHeatmap.getHeatmapData(filter_piece, start_elo, end_elo)

    fig = px.imshow(data,
                    labels=dict(color="# of checkmates"),
                    x=list("abcdefgh"),
                    y=list("87654321"),
                    color_continuous_scale = "mint"
                   )

    fig.update_layout(margin=dict(t=0, b=0), height=600, yaxis=dict(type='category'))


    st.plotly_chart(fig, theme="streamlit")


def show_big_number(start_elo, end_elo):
    game_num = getGamesNum.getGamesNum(start_elo, end_elo)
    st.metric("Number of games being analyzed", game_num)

def main():
    st.set_page_config(
        page_title="Chess Visualizations", 
        page_icon=":chess_pawn:", 
        layout="centered",
        menu_items={
            'About': "This app is made for a Data Visualization class in Ateneo de Manila University."
        }
    )

    st.title("2023 Lichess Visualizations :chess_pawn:")
    st.caption("By Bryan Francisco, James Mostajo, and Robin Vicente")

    st.divider()

    # Filters
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        start_elo, end_elo = st.select_slider(
            "Select range of game elo rating",
            options=range(2300, 4001),
            value=(2300, 4000)
        )
    with col2:
        show_big_number(start_elo, end_elo)

    
    show_checkmate_heatmap(start_elo, end_elo)


if __name__ == '__main__':
    main()
