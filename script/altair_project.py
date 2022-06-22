import altair as alt
from vega_datasets import data

def main():
    df = data.movies.url
    pts = alt.selection(type="single", encodings=['x'])
    <!-- brush = alt.selection(type="interval") -->

    rect = alt.Chart(df).mark_bar().encode(
        alt.X('IMDB_Rating:Q', bin=True),
        alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
        color=alt.condition(pts, 'Rotten_Tomatoes_Rating:Q', alt.value('lightgray'))
    )

    circ = rect.mark_point().encode(
        alt.ColorValue('lightgray'),
        alt.Size(
            'count()',
            legend=alt.Legend(title='Number of Movies Selected')
        )
    ).transform_filter(
        pts
    )

    text = alt.Chart(df).mark_text().encode(
        y=alt.Y('row_number:O', axis=None),
    ).transform_window(
        row_number='row_number()'
    ).transform_filter(
        pts
    ).transform_window(
        rank='rank(row_number)'
    ).transform_filter(
        alt.datum.rank < 20
    )

    ratings = text.encode(
        text='Rotten_Tomatoes_Rating:Q'
    )
    moviename = text.encode(
        text="Title:N"
    )

    line = alt.Chart(df).mark_line().encode(
        x="Major_Genre:N",
        y="count()"
    )

    bar = alt.Chart(df).mark_bar().encode(
        x="Major_Genre:N",
        y="count()"
    ).properties(
        width=700,
        height=250
    ).add_selection(
        pts
    )


    alt.vconcat(
        (rect + circ | ratings | moviename | line),
        bar
    ).resolve_legend(
        color="independent",
        size="independent"
    )
    return
    
main()
  