import streamlit as st

# Page setup
st.set_page_config(page_title="Welcome!", page_icon="👋", layout="wide")

# --- Custom CSS for style ---
st.markdown(
    """
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #fceabb, #f8b500, #ff6f61);
        color: #333333;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    /* Title animation */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .title {
        font-size: 3em;
        font-weight: bold;
        color: #fff;
        text-align: center;
        padding: 20px;
        animation: fadeIn 1.5s ease-in-out;
        text-shadow: 2px 2px 4px #00000066;
    }
    .subtitle {
        font-size: 1.3em;
        color: #fff;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Card style */
    .card {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        text-align: center;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown("<div class='title'>👋 Welcome to Learn to Code!</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>An exciting Python journey for kids age 10+</div>", unsafe_allow_html=True)

# --- Layout with 3 cards ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>🐍 <br> Learn Python step by step</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>✨ <br> Fun examples and interactive demos</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>🚀 <br> Build your own mini projects</div>", unsafe_allow_html=True)

# --- Footer call to action ---
st.markdown(
    """
    <br><br>
    <div style="text-align:center; font-size:1.2em; color:white;">
        👉 Use the sidebar to pick a module and begin your adventure!
    </div>
    """,
    unsafe_allow_html=True
)
