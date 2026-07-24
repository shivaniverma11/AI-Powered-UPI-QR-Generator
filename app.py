import streamlit as st
import os
from qr_generator import generate_qr
from database import init_db, save_payment, get_payments
from ai_features import validate_upi, suggest_name, detect_anomaly, get_insights
from receipt import generate_receipt

init_db()

st.set_page_config(page_title="AI UPI QR Generator", page_icon="🤖")

st.title("🤖 AI Smart UPI QR Generator")

menu = st.sidebar.selectbox("Menu", ["Generate QR", "Dashboard"])

# ================= GENERATE =================
if menu == "Generate QR":

    st.subheader("Enter Details")

    upi_id = st.text_input("UPI ID")
    name = st.text_input("Name (optional)")
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)
    note = st.text_input("Payment Note (optional)")

    if upi_id and not name:
        suggested = suggest_name(upi_id)
        st.info(f"🤖 Suggested Name: {suggested}")
        name = suggested

    if st.button("Generate QR"):

        if upi_id and name:

            if not validate_upi(upi_id):
                st.error("❌ Invalid UPI ID")
            else:

                data = get_payments()
                if amount and detect_anomaly(data, amount):
                    st.warning("⚠️ This transaction amount looks unusual compared to your history (ML-flagged)")

                qr_path = generate_qr(upi_id, name, amount, note)
                save_payment(name, upi_id, amount)
                receipt_path = generate_receipt(name, upi_id, amount)

                st.success("🤖 AI Generated QR Ready!")
                st.image(qr_path)

                col1, col2 = st.columns(2)
                with col1:
                    with open(qr_path, "rb") as f:
                        st.download_button("Download QR", f, file_name=qr_path)
                with col2:
                    with open(receipt_path, "rb") as f:
                        st.download_button("Download Receipt", f, file_name=receipt_path)

        else:
            st.error("Fill required fields")

# ================= DASHBOARD =================
elif menu == "Dashboard":

    st.subheader("📊 AI Insights Dashboard")

    data = get_payments()

    if data:
        total, most_common, avg_amount = get_insights(data)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Transactions", total)
        col2.metric("Avg Amount", f"₹{avg_amount}")
        if most_common:
            col3.metric("Most Used UPI", most_common[0][0])

        st.subheader("Recent Activity")
        for row in data[-5:]:
            st.write(f"👤 {row[0]} | 🆔 {row[1]} | ₹{row[2]} | 🕒 {row[3]}")

    else:
        st.info("No data yet")

# ================= AI CHAT =================
st.sidebar.title("🤖 AI Assistant")

query = st.sidebar.text_input("Ask about UPI")

if query:
    if "upi" in query.lower():
        st.sidebar.write("UPI is a real-time payment system in India.")
    elif "qr" in query.lower():
        st.sidebar.write("QR code allows instant payments.")
    elif "anomaly" in query.lower() or "suspicious" in query.lower():
        st.sidebar.write("I use an Isolation Forest ML model to flag unusual transaction amounts.")
    else:
        st.sidebar.write("I can help with payments 😊")
