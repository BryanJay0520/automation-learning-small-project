def needs_attention(status, minutes_waiting, threshold=10):  # Gumawa ng function na may default limit na 10 minutes.
    return status == "pending" and minutes_waiting >= threshold  # Return True kung pending at umabot na sa limit.

orders = [  # Simulan ang list ng sample orders.
    #{"id": 101, "status": "completed", "minutes_waiting": 15},  # Completed na, kaya hindi dapat mag-alert. false
    #{"id": 102, "status": "completed", "minutes_waiting": 15},  # Completed na, kaya hindi dapat mag-alert. false
    #{"id": 103, "status": "pending", "minutes_waiting": 4},  # Pending pero 4 minutes pa lang, kaya walang alert. false
]  # Tapusin ang list ng orders.

alert_count = 0  # Simulan sa zero ang bilang ng alerts.

for order in orders:  # Isa-isang kunin ang bawat order.
    if needs_attention(order["status"], order["minutes_waiting"]):  # Gamitin ang True o False na ibinalik ng function.
        print(f'CHECK order {order["id"]}')  # Ipakita ang alert kapag True ang result.
        alert_count += 1  # Dagdagan ng isa ang bilang ng alerts.
    else:  # Ito ang tatakbo kapag False ang result.
        print(f'No alert for order {order["id"]}')  # Ipakita na walang alert para sa order na ito.

if alert_count == 0:  # Pagkatapos ng loop, i-check kung zero ang alerts.
    print("No orders need attention.")  # Ipakita ito kung walang order na na-flag.
else:  # Ito ang tatakbo kapag hindi zero ang alerts.
    print(f"Total alerts: {alert_count}")  # Ipakita ang total na bilang ng alerts.