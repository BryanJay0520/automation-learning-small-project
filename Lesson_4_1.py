def needs_attention(status, minutes_waiting, threshold=10):  # Gumawa ng function na may default limit na 10 minutes.
    return status == "pending" and minutes_waiting >= threshold  # Return True kung pending at umabot na sa limit.

orders = [
    {"id": 101, "status": "pending", "minutes_waiting": 15},  # Completed na, kaya hindi dapat mag-alert. false
    {"id": 102, "status": "completed", "minutes_waiting": 15},  # Completed na, kaya hindi dapat mag-alert. false
    {"id": 103, "status": "pending", "minutes_waiting": 4}   # Pending pero 4 minutes pa lang, kaya walang alert. false
]  

alert_count = 0  # Simulan sa zero ang bilang ng alerts.

if len(orders) == 0:  # I-check kung walang orders sa list.
    print("No orders to check.")  # Ipakita ito kung walang order na na-flag.
else:  # Ito ang tatakbo kapag may orders sa list.
    for order in orders:  # Isa-isang kunin ang bawat order.
        if needs_attention(order["status"], order["minutes_waiting"]):  # Gamitin ang True o False na ibinalik ng function.
            print(f'CHECK order {order["id"]}')  # Ipakita ang alert kapag True ang result.
            alert_count += 1  # Dagdagan ng isa ang bilang ng alerts.
    if alert_count == 0:  # Pagkatapos ng loop, i-check kung zero ang alerts.
        print("No orders need attention.")  # Ipakita ito kung walang order na na-flag.
    else:  # Ito ang tatakbo kapag hindi zero ang alerts.
        print(f"Total alerts: {alert_count}")  # Ipakita ang total na bilang ng alerts.