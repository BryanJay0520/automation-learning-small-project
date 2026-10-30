def needs_attention(status, minutes_waiting, threshold=10): # Gumawa ng function na may default limit na 10 minutes.
    return status == "pending" and minutes_waiting >= threshold  # Return True kung pending at umabot na sa limit.

orders = [
    {"id": 101, "status": "pending", "minutes_waiting": 15},  # Pending at 15 minutes, kaya dapat mag-alert. true
    {"id": 102, "status": "completed", "minutes_waiting": 15},  # Completed na, kaya hindi dapat mag-alert. false
    {"id": 103, "status": "pending", "minutes_waiting": 12},   # Pending for 12 minutes , kaya dapat mag-alert. true
    {"id": 104, "status": "pending", "minutes_waiting": 4},  # Pending pero 4 minutes pa lang, kaya walang alert. false
    {"id": 105, "status": "pending", "minutes_waiting": 8},   # Pending pero 8 minutes pa lang, kaya walang alert. false   
]  # list ng orders.

alert_ids = []  # Gumawa ng empty list para sa mga order IDs that need attention.

for order in orders:  # Isa-isang kunin ang bawat order.
    if needs_attention(order["status"], order["minutes_waiting"],):  # ito nag-check kung kailangan ng attention gamit ang function na needs_attention.
        alert_ids.append(order["id"])  # Idagdag ang order ID sa list ng alerts.

print(f"Orders needing attention: {alert_ids}")  # Ipakita ang mga order IDs na nangangailangan ng attention.   
print(f"Total alerts: {len(alert_ids)}")  # Ipakita ang total na bilang ng alerts