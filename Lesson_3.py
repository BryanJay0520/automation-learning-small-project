def needs_attention(status, minutes_waiting, threshold=10):
    return status == "pending" and minutes_waiting >= threshold

orders = [
    {"id": 101, "status": "pending", "minutes_waiting": 12}, #true
    {"id": 102, "status": "completed", "minutes_waiting": 18}, #false
    {"id": 103, "status": "pending", "minutes_waiting": 4}, #false
    {"id": 104, "status": "pending", "minutes_waiting": 9}, #false
    ]
alert_count = 0

for order in orders:  # Isa-isang kunin ang orders mula sa list.
    if needs_attention(order["status"], order["minutes_waiting"]):  # I-check ang order gamit ang function.
        print(f"Order {order['id']} has been waiting for {order['minutes_waiting']} minutes and needs attention.")
        alert_count += 1

print(f"Number of pending orders exceeding threshold: {alert_count}")


  