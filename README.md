# 👗 Women's Clothing Store – Streamlit E-commerce Demo

Welcome to the **Women's Clothing Store**, a sleek and interactive e-commerce demo built with **Streamlit**! This project simulates a basic online shopping experience, allowing users to browse products, filter by category, and manage a shopping cart—all powered by Python 🐍.

---

## ✨ Features

- 🔍 **Category Filter** – Browse items by Dresses, Jackets, Tops, or view all  
- 🖼️ **Product Display** – See product images, names, categories, and prices  
- 🛒 **Add to Cart** – Add items to a session-based cart with instant feedback  
- 📦 **Cart Summary** – View selected items in the sidebar  

---

## 🧵 Tech Stack

- **Streamlit** – For building the interactive web UI  
- **Pandas** – For handling product data  
- **Pillow (PIL)** – For image rendering  

---

## 📂 Project Structure

├── app.py # Main Streamlit app ├── products.csv # Product data (name, category, price, image path, id) ├── images/ # Folder containing product images

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/indhumaha/Ecommerce_Streamlit_Python.git
cd womens-clothing-store

2️⃣ Install dependencies
Make sure you have Python 3.7+ installed, then run:

bash
pip install streamlit pandas pillow

3️⃣ Launch the app
bash
streamlit run app.py

📊 Sample products.csv
csv
id,name,category,price,image
1,Floral Dress,Dresses,49.99,images/floral_dress.jpg
2,Denim Jacket,Jackets,59.99,images/denim_jacket.jpg
3,Silk Blouse,Tops,39.99,images/silk_blouse.jpg
📝 Make sure the image paths match the actual files in your images/ folder.

🎯 Purpose
This project is perfect for:

Learning Streamlit for frontend prototyping

Exploring session state and dynamic UI updates

Building e-commerce dashboards with Python

📸 Screenshot
Add a screenshot of your app here to showcase the UI:
<img width="1516" height="995" alt="image" src="https://github.com/user-attachments/assets/cde41b9c-42a5-4a1e-b6db-5b6a3b86aa63" />

🌱 Future Enhancements
🧮 Quantity selector and total price calculation

💳 Checkout simulation

🗂️ Persistent cart using local storage or database

📱 Responsive design improvements



