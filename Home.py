import streamlit as st
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

# Define sidebar contents
with st.sidebar:
    # Add profile icon1fNx44o_jGdQ_WALqYjo_nylaH02yrPx8
    st.markdown("<div style='text-align: center'><img src='https://drive.google.com/uc?export=view&id=1fNx44o_jGdQ_WALqYjo_nylaH02yrPx8' width='100'></div>", unsafe_allow_html=True)
    # Add text
    st.markdown("## Hello!, Welcome to Diamond Rush")
    st.markdown("Here you can solve the exciting treasure hunt")




# Define the CSS style
style = """
<style>
    .columnImage {
        box-sizing: border-box;
        float: left;
        width: 107%;
    }
</style>
"""

# Add the CSS style to the page
st.markdown(style, unsafe_allow_html=True)

# Define the columns
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)

# Add content to each column
with col1:
    st.markdown(f"""<a href="pages/page1.py"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1z59GvMgWiFOSJGRF9wP_qL9urclIuv9o"></a>""",unsafe_allow_html=True)
with col2:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1iDPB9zJWc_jFErSQV6eFXp4JRU47t1vu"></a>""",unsafe_allow_html=True)
with col3:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=13JqXqmJGadtkASS8oKkRpncxyCXnl9XU"></a>""",unsafe_allow_html=True)
with col4:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1HmIbxSlXSCit8qJ9VGvLpmbKgutqmZ8F"></a>""",unsafe_allow_html=True)
with col5:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1gdakk6gwfVa-0Qw_f-Sitp4zLB8BoiiX"></a>""",unsafe_allow_html=True)
with col6:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1Z_bX1lyfaB4JraiUQ9vX8lh4-ao8_Qki"></a>""",unsafe_allow_html=True)
with col7:
    st.markdown(f"""<a href=""><img class="columnImage" src="https://drive.google.com/uc?export=view&id=11bUMmqlRJRDsWbfjkwqaD3--jv-DwkKo"></a>""",unsafe_allow_html=True)
with col8:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=12dSWYJO9didCNBMOAoTZkCUlHNFqffB3"></a>""",unsafe_allow_html=True)
with col9:
    st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=13UvmRI3tpKTF0B8KKvYJE7nLmGwSYbn2"></a>""",unsafe_allow_html=True)