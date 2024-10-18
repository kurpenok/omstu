import streamlit as st

pg = st.navigation(
    [
        st.Page("sections/author.py", title="Author"),
        st.Page("sections/data.py", title="Data"),
        st.Page("sections/visualization.py", title="Visualization"),
        st.Page("sections/models.py", title="Models"),
    ]
)
pg.run()
