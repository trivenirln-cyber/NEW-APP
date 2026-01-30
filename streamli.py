import streamlit as st
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increase"):
    st.session_state.count += 1
if st.button("decrease"):
    st.session_state.count -= 1
st.header(st.session_state.count)

