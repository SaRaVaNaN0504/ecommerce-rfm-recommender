# app.py

import streamlit as st
import pandas as pd
import joblib

# Custom CSS for professional look
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Set page config
st.set_page_config(page_title="🛒 RFM Segmentation & Recommender", layout="wide")

# Load saved models
scaler = joblib.load("models/rfm_scaler.pkl")
kmeans = joblib.load("models/kmeans_rfm_model.pkl")
similarity_df = pd.read_pickle("models/similarity_df.pkl")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/891/891462.png", width=80)
st.sidebar.markdown("## 💼 Project Info")
st.sidebar.info("""
This app segments customers using RFM analysis
and recommends similar products based on purchase history.

Built with ❤️ by **Saravanan**
""")

# Main title
st.title("🛍️ E-Commerce Customer Intelligence Dashboard")
st.markdown("### Segment customers based on behavior and recommend products to improve sales!")

# Tabs
tab1, tab2 = st.tabs(["📦 Product Recommender", "👤 Customer Segment Predictor"])

# --- TAB 1: Product Recommender ---
with tab1:
    st.markdown("#### 🔍 Find Products Similar to a Given Product")
    
    with st.expander("ℹ️ How It Works"):
        st.markdown("""
        - Enter a valid **Product Code** from your dataset (e.g., `85123A`)
        - We'll show the top 5 most similar products using **item-based collaborative filtering**
        """)

    product_code = st.text_input("Enter a Product Code (e.g. `85123A`):")

    if st.button("🔎 Recommend Products"):
        if product_code in similarity_df.columns:
            recommendations = similarity_df[product_code].sort_values(ascending=False)[1:6]
            st.success("✅ Top 5 Similar Products:")
            st.table(
                pd.DataFrame(recommendations)
                .reset_index()
                .rename(columns={'index': '🆔 Product Code', product_code: '🔗 Similarity Score'})
            )
        else:
            st.error("❌ Product code not found. Try a code from your dataset (e.g., `85123A`).")

# --- TAB 2: Customer Segment Predictor ---
with tab2:
    st.markdown("#### 📊 Classify a Customer into a Segment Based on Their RFM Values")
    
    with st.expander("ℹ️ What's RFM?"):
        st.markdown("""
        - **Recency** = Days since last purchase  
        - **Frequency** = Number of purchases  
        - **Monetary** = Total spend amount  
        """)

    col1, col2, col3 = st.columns(3)
    with col1:
        recency = st.number_input("🕐 Recency (Days since last purchase)", min_value=0)
    with col2:
        frequency = st.number_input("🔁 Frequency (Number of Transactions)", min_value=0)
    with col3:
        monetary = st.number_input("💰 Monetary Value (Total Spend)", min_value=0.0)

    if st.button("📈 Predict Customer Segment"):
        try:
            rfm_input = scaler.transform([[recency, frequency, monetary]])
            cluster = kmeans.predict(rfm_input)[0]
            
            cluster_desc = {
                0: "🟢 High-Value Customer",
                1: "🟡 Potential Loyalist",
                2: "🔴 At Risk",
                3: "⚪ New / Occasional Buyer"
            }
            st.success(f"🎯 Predicted Segment: **Cluster {cluster}** - {cluster_desc.get(cluster, 'Segment')}")

        except Exception as e:
            st.error(f"Error: {e}")
