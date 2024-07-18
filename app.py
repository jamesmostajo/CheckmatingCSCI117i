import streamlit as st
import getHeatmap, getGamesNum, getWaffle, getPieceTakes, getPie, getPieGameResults, getEloHistogram


def show_checkmate_heatmap(start_elo, end_elo):
    import plotly.express as px
    
    st.subheader("Where do Pieces move to Checkmate?")
    st.write("Below is a heatmap displaying any given chess pieces’ most common position on the board whenever they get a checkmate.")
    col1, col2, col3 = st.columns(3)

    with col1:
        filter_piece = st.selectbox(
                "Select piece",
                ("Select All", "Pawn", "Knight", "Bishop", "Rook", "Queen", "King")
        )
    with col2:
        filter_winner = st.selectbox(
                "Select winning side",
                ("Select Both", "Black", "White")
        )
        
    data = getHeatmap.getHeatmapData(filter_piece, start_elo, end_elo, filter_winner)

    fig = px.imshow(data,
                    labels=dict(color="# of checkmates"),
                    x=list("abcdefgh"),
                    y=list("87654321"),
                    color_continuous_scale = "mint"
                   )

    fig.update_layout(margin=dict(t=0, b=0), height=600, yaxis=dict(type='category'))


    st.plotly_chart(fig, theme="streamlit")

def show_waffle(start_elo, end_elo):
    import plotly.graph_objects as go

    st.subheader("How much checkmates does each piece have compared to others")
    data = getWaffle.getWaffleData(start_elo, end_elo)
    if data == -1 :
        st.write("There are no checkmates in this elo range")
        return
    else:
        st.write("insert description here.")
    gap = 0.25
    
    unique_values = [0, 1, 2, 3, 4, 5]
    labels = ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]

    colors = ['#0015FF', '#FF00A1', '#90FE00', '#8400FF', '#00FFF7', '#FF7300']
    color_scale = [[i / (len(colors) - 1), color] for i, color in enumerate(colors)]


    fig = go.Figure(data=go.Heatmap(
        z=data,
        colorscale=color_scale,
        showscale=False,
        # hoverinfo='none',
        xgap=gap, ygap=gap,
        zmin=0,zmax=5 
    ))

    for i, (color, label) in enumerate(zip(colors, labels)):
        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode='markers',
            marker=dict(size=10, color=color),
            legendgroup=str(i),
            showlegend=True,
            name=label
        ))

    fig.update_layout(
        height=700, margin=dict(t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, ticks=''),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, ticks=''),
        legend=dict(
            title="Legend",
            orientation="v",
            yanchor="top",
            xanchor="right",
            y=1, x=1.15,
        )
    )

    st.plotly_chart(fig, theme="streamlit")

def show_pie_graph(start_elo, end_elo):
    import plotly.express as px
    data = getPie.getPieData(start_elo, end_elo)

    st.subheader("What Piece is used the most to Checkmate?")
    st.write("insert description here.")
    if data == -1 :
        st.write("There are no checkmates in this elo range")
        return

    custom_colors = ['#330036', '#A3001E', '#125D63', '#0D7296', '#F5B841', '#EC6F9B']
    
    fig = px.pie(names=data['piece'], values = data['pieceCount'], color_discrete_sequence=custom_colors)

    fig.update_layout(margin=dict(t=0, b=0))
    st.plotly_chart(fig, theme="streamlit")

def show_big_number(start_elo, end_elo):
    game_num = getGamesNum.getGamesNum(start_elo, end_elo)
    st.metric("Number of games being analyzed", game_num)

def show_piece_takes(start_elo, end_elo):
    import plotly.graph_objects as go

    st.subheader("How many captures does each Piece make?")
    st.write("This bar graph depicts which piece has the highest number of takes among the others")

    is_divided = st.toggle("Divide by number of type of piece")

    x = ['Pawn', 'Rook', 'Knight', 'Bishop', 'Queen', 'King']
    y = getPieceTakes.getPieceTakesData(start_elo, end_elo)

    if is_divided:
        div = [16, 4, 4, 4, 2, 2]
        y = [y[i]//div[i] for i in range(6)]

    y_text = [f'{val:,}' for val in y]

    # Use textposition='auto' for direct text
    fig = go.Figure(data=[go.Bar(
                x=x, y=y,
                text=y_text,
                textposition='auto',
                marker=dict(color='#125D63')
            )])

    fig.update_layout(margin=dict(t=0, b=0))

    st.plotly_chart(fig, theme="streamlit")

def show_pie_result(start_elo, end_elo):
    import plotly.graph_objects as go

    st.subheader("How frequent do Checkmates occur?")
    st.write("insert description here.")

    labels = ['Checkmates','Draws','Others']
    values = getPieGameResults.getPieGameresults(start_elo, end_elo)

    custom_colors = ['#330036', '#A3001E', '#125D63']
    hover_text = [
        "",
        "",
        "Resignations, time forfeit, and other game results"
    ]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, 
                                    marker=dict(colors=custom_colors),
                                    hoverinfo='label+percent+text',
                                    hovertext=hover_text
                                    )])

    fig.update_layout(margin=dict(t=0, b=0))

    st.plotly_chart(fig, theme="streamlit")

def show_histogram():
    import plotly.express as px
    st.subheader("Number of Games played by Game Elo")
    data = getEloHistogram.getHistogramData()
    custom_colors = ['#125D63']
    fig = px.histogram(
        x=data['elo_ranges'], 
        y=data['values'], 
        nbins=len(data['elo_ranges']),
        color_discrete_sequence=custom_colors
    )
    
    fig.update_layout(
        margin=dict(t=0, b=0),
        xaxis_title='Elo Rating',
        yaxis_title='Number of Games',
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

    st.title("2023 Lichess Visualizations :chess_pawn:")
    st.caption("By Bryan Francisco, James Mostajo, and Robin Vicente")

    # st.divider()

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        start_elo, end_elo = st.select_slider(
            "Select range of game elo rating",
            options=range(2300, 3201),
            value=(2300, 3200)
        )
    with col2:
        show_big_number(start_elo, end_elo)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Games Played?",
        "Move to Checkmate?",
        "Piece Captures?",
        "Number of Games played",
        "Number of Games played",
    ])

    with tab1:
        show_histogram()
    with tab2:
        show_checkmate_heatmap(start_elo, end_elo)  
    with tab3:
        show_piece_takes(start_elo, end_elo)
    with tab4:
        show_pie_result(start_elo, end_elo)
    with tab5:
        show_pie_graph(start_elo, end_elo)


if __name__ == '__main__':
    main()
