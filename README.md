# 🛍️ E-commerce RFM & Product Recommendation System

This project combines **Customer Segmentation** and **Product Recommendation** techniques to help e-commerce businesses understand their customers better and suggest relevant products.  

It uses:
- **RFM Analysis** for customer segmentation
  
- **Item-Based Collaborative Filtering** for product recommendations  

---

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Workflow](#project-workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Screenshots](#screenshots)
- [License](#license)

---

## 📖 Project Overview

The goal of this project is to:
1. Segment customers into meaningful groups using **RFM (Recency, Frequency, Monetary) Analysis**
2. Recommend products to customers using **Item-Based Collaborative Filtering**

This system can help:
- Marketing teams target specific customer groups
- Increase customer engagement
- Boost sales through personalized recommendations

---

## 📂 Dataset

The dataset used is the **Online Retail Dataset**, containing transaction records of a UK-based online store between **2010–2011**.

**Dataset Columns:**
- `InvoiceNo` – Unique invoice number
- `StockCode` – Product code
- `Description` – Product name
- `Quantity` – Number of products purchased
- `InvoiceDate` – Date of purchase
- `UnitPrice` – Price per unit
- `CustomerID` – Unique customer ID
- `Country` – Country of customer

---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `pandas` – Data manipulation
  - `numpy` – Numerical calculations
  - `matplotlib`, `seaborn` – Data visualization
  - `scikit-learn` – Clustering and scaling
  - `joblib` – Model saving/loading
  - `streamlit` – Web app deployment

---

## ✨ Features

- **Customer Segmentation**
  - Segments customers into groups (e.g., loyal, at risk, new) using RFM metrics.
- **Product Recommendation**
  - Suggests similar products using **cosine similarity** between items.
- **Interactive Web App**
  - Built with Streamlit for easy use and visualization.

---

## 🔄 Project Workflow

1. **Data Cleaning**
   - Remove null values, duplicates, and invalid transactions.
2. **RFM Analysis**
   - Calculate Recency, Frequency, and Monetary values for each customer.
   - Apply scaling and clustering (KMeans) to segment customers.
3. **Collaborative Filtering**
   - Create a pivot table of customers vs products.
   - Compute similarity using cosine similarity.
4. **Web App**
   - Allow users to enter a product name and get recommendations.
   - Display RFM segments and insights.

---

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ecommerce-rfm-recommender.git
   cd ecommerce-rfm-recommender
2 .Create a virtual environment :
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

3. Install dependencies:
   pip install -r requirements.txt


---

## Results
-Customers are segmented into X groups using KMeans.

-Recommendations are based on item similarity.

-Example: If a user likes WHITE HANGING HEART T-LIGHT HOLDER, similar products are suggested.

---

## 🔮 Future Improvements
-Implement User-Based Collaborative Filtering

-Add Deep Learning-based Recommendation Models

-Real-time data integration from an e-commerce platform

-Deploy on cloud (AWS/GCP) with continuous data updates

---

## Author: Saravanan
## Contact: saro.05.11.04@gmail.com
## GitHub: https://github.com/SaRaVaNaN0504/



