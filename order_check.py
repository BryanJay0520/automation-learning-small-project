orders = [
    {"id": 101, "status": "pending", "minutes_waiting": 12},
    {"id": 102, "status": "completed", "minutes_waiting": 5},
    {"id": 103, "status": "pending", "minutes_waiting": 20},
    {"id": 104, "status": "pending", "minutes_waiting": 8},
    {"id": 105, "status": "pending", "minutes_waiting": 15},
]
threshold_minutes = 15
alert_count = 0

for order in orders:
    needs_attention = (order["status"] == "pending" and order["minutes_waiting"] >= threshold_minutes)
    if needs_attention:
      print(f'CHECK ALERT: Order ID {order["id"]} has been pending for {order["minutes_waiting"]} minutes.')
      alert_count += 1
print(f"Number of pending orders exceeding {threshold_minutes} minutes: {alert_count}")