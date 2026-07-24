import re
from collections import Counter
import numpy as np
from sklearn.ensemble import IsolationForest

# ✅ UPI validation
def validate_upi(upi):
    pattern = r'^[a-zA-Z0-9.\-_]+@[a-zA-Z]+$'
    return re.match(pattern, upi)

# 🤖 Name suggestion
def suggest_name(upi):
    name_part = upi.split("@")[0]
    return name_part.replace(".", " ").title()

# ⚠️ ML-based anomaly detection
def detect_anomaly(data, current_amount):
    """
    Uses Isolation Forest to flag whether the current transaction amount
    is anomalous compared to past transaction history.
    Falls back to a simple rule if not enough history exists yet.
    """
    amounts = [row[2] for row in data if row[2]]  # amount is column index 2

    if len(amounts) < 5:
        # Not enough data to train a model yet — use simple rule
        return current_amount > 50000

    X = np.array(amounts).reshape(-1, 1)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)

    prediction = model.predict([[current_amount]])
    return prediction[0] == -1  # -1 means anomaly

# 📊 AI insights
def get_insights(data):
    total = len(data)

    upi_list = [row[1] for row in data]
    most_common = Counter(upi_list).most_common(1)

    amounts = [row[2] for row in data if row[2]]
    avg_amount = round(sum(amounts) / len(amounts), 2) if amounts else 0

    return total, most_common, avg_amount
