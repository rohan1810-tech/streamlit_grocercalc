import streamlit as st

st.title("🛒 The Smart Grocer Calculator")

# 1. User Input
rice_qty = st.number_input("Enter rice quantity (kg):", min_value=0.0, step=0.5)
sugar_qty = st.number_input("Enter sugar quantity (kg):", min_value=0.0, step=0.5)
oil_qty = st.number_input("Enter oil quantity (litres):", min_value=0.0, step=0.5)

# Prices
rice_price = 60
sugar_price = 45
oil_price = 120

# 2. Total before discount
total_before = (rice_qty * rice_price) + (sugar_qty * sugar_price) + (oil_qty * oil_price)

# 3. Apply discount if > 500
discount = 0
if total_before > 500:
    discount = total_before * 0.10

final_amount = total_before - discount

# 4. Display the bill
st.subheader("🧾 Bill Summary")
st.write("**Total Before Discount:** ₹", total_before)
st.write("**Discount Applied:** ₹", discount)
st.write("**Final Amount to Pay:** ₹", final_amount)

