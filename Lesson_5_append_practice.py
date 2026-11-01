orders = [  
    {"id": 301, "status": "pending"},  
    {"id": 302, "status": "completed"},  
    {"id": 303, "status": "completed"}, 
    {"id": 304, "status": "pending"}, 
]  

pending_ids = []  

for order in orders:  
    if order["status"] == "pending":  
        print(f'Pending order: {order["id"]}')  
        pending_ids.append(order["id"])  

print(f"Collected IDs: {pending_ids}")  