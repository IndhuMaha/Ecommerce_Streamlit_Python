import streamlit as st
import pandas as pd
from PIL import Image

# Load product data
df = pd.read_csv("products.csv")

# Session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sidebar filters
st.sidebar.title("Filter by Category")
categories = df["category"].unique()
selected_category = st.sidebar.selectbox("Choose a category", ["All"] + list(categories))

# Title
st.title("👗 Women's Clothing Store")

# Filter products
filtered_df = df if selected_category == "All" else df[df["category"] == selected_category]

# Display products
for _, row in filtered_df.iterrows():
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            image = Image.open(row["image"])
            st.image(image, width=150)
        with cols[1]:
            st.subheader(row["name"])
            st.write(f"Category: {row['category']}")
            st.write(f"Price: ₹{row['price']}")
            if st.button(f"Add to Cart - {row['id']}"):
                st.session_state.cart.append(row["name"])
                st.success(f"{row['name']} added to cart!")

# Show cart
st.sidebar.title("🛒 Your Cart")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.sidebar.write(f"- {item}")
else:
    st.sidebar.write("Your cart is empty.")
