import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🎲"
)


image = Image.open('tec.jpg')
st.sidebar.image( image, width=120)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('# Fastested Delivery in Town')
st.sidebar.markdown("""---""")


st.sidebar.markdown('### Powered by Comunidade DS: Luigi Silva Ferrari')

st.markdown(
    """
        Explicação de uso do Dashboard


    """
)