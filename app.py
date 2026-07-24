import streamlit as st
import os
from qr_generator import generate_qr
from database import init_db, save_payment, get_payments
from ai_features import validate_upi, suggest_name, is_suspicious, get_insights

init_db()

st.set_page_config(page_title="AI UPI QR Generator", page_icon="🤖")

st.title("🤖 AI Smart UPI QR Generator")

menu = st.sidebar.selectbox("Menu", ["Generate QR", "Dashboard"])

# ================= GENERATE =================
if menu == "Generate QR":

    st.subheader("Enter Details")

    upi_id = st.text_input("UPI ID")
    name = st.text_input("Name (optional)")

    # 🤖 Auto name suggestion
    if upi_id and not name:
        suggested = suggest_name(upi_id)
        st.info(f"🤖 Suggested Name: {suggested}")
        name = suggested

    if st.button("Generate QR"):

        if upi_id and name:

            # ✅ validation
            if not validate_upi(upi_id):
                st.error("❌ Invalid UPI ID")
            else:

                # ⚠️ suspicious check
                if is_suspicious(upi_id):
                    st.warning("⚠️ Suspicious UPI ID detected")

                qr_path = generate_qr(upi_id, name)
                save_payment(name, upi_id)

                st.success("🤖 AI Generated QR Ready!")
                st.image(qr_path)

                with open(qr_path, "rb") as f:
                    st.download_button("Download QR", f)

        else:
            st.error("Fill required fields")

# ================= DASHBOARD =================
elif menu == "Dashboard":

    st.subheader("📊 AI Insights Dashboard")

    data = get_payments()

    if data:
        total, most_common = get_insights(data)

        st.write(f"👥 Total Users: {total}")

        if most_common:
            st.write(f"🔥 Most Used UPI: {most_common[0][0]}")

        st.subheader("Recent Activity")
        for row in data[-5:]:
            st.write(f"👤 {row[0]} | 🆔 {row[1]}")

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
    else:
        st.sidebar.write("I can help with payments 😊")