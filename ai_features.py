import re
from collections import Counter

# ✅ UPI validation
def validate_upi(upi):
    pattern = r'^[a-zA-Z0-9.\-_]+@[a-zA-Z]+$'
    return re.match(pattern, upi)

# 🤖 Name suggestion
def suggest_name(upi):
    name_part = upi.split("@")[0]
    return name_part.replace(".", " ").title()

# ⚠️ Suspicious detection
def is_suspicious(upi):
    return len(upi) < 5 or "test" in upi.lower()

# 📊 AI insights
def get_insights(data):
    total = len(data)
    
    upi_list = [row[1] for row in data]
    most_common = Counter(upi_list).most_common(1)

    return total, most_common