# 🤖 AI-Powered UPI QR Generator

A smart UPI payment QR code generator built with **Python** and **Streamlit**, enhanced with ML-based transaction anomaly detection and automated receipt generation.

## ✨ Features

- **Instant QR Generation** — Create UPI payment QR codes using UPI ID, name, amount, and payment note
- **Smart Validation** — Automatic UPI ID format validation with error handling
- **Auto Name Suggestion** — Suggests a recipient name automatically from the UPI ID if left blank
- **ML-Based Anomaly Detection** — Uses an Isolation Forest model to flag unusual transaction amounts compared to past history
- **Automated Receipt Generation** — Download a text receipt alongside every generated QR code
- **Transaction Dashboard** — View total transactions, average amount, most-used UPI ID, and recent activity
- **Database Tracking** — All transactions are stored locally using SQLite with timestamps
- **AI Assistant (Sidebar)** — Quick answers to basic UPI/QR-related queries
- **Download Options** — Download both the QR code image and the payment receipt

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — Web app interface
- **qrcode / Pillow** — QR code generation
- **SQLite** — Local transaction database
- **scikit-learn** — Isolation Forest model for anomaly detection
- **Plotly / Pandas** — Data handling and visualization

## 📸 Screenshots

### Generate QR Page
![Generate QR](screenshots_upigen/generate_qr.png)

### Sample Generated QR
![QR Output](screenshots_upigen/qr_output.png)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Powered-UPI-QR-Generator.git
cd AI-Powered-UPI-QR-Generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 📂 Project Structure
├── app.py # Main Streamlit application
├── qr_generator.py # QR code generation logic
├── database.py # SQLite database operations
├── ai_features.py # UPI validation, name suggestion, ML anomaly detection
├── receipt.py # Receipt generation
├── requirements.txt # Project dependencies
## 🔮 Future Improvements

- OCR-based UPI ID extraction from screenshots
- LLM-powered AI assistant for open-ended queries
- CSV/Excel export of transaction history
- User authentication for multi-user support

## 📄 License

This project is open source and available under the MIT License.
