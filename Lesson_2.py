def needs_attention(status, minutes_waiting, threshold = 10):
    return status == "pending" and minutes_waiting >= threshold

order_101 = needs_attention("pending", 12) #true
order_102 = needs_attention("completed", 18) #false
order_103 = needs_attention("pending", 4) #false

print(f"Order 101 needs attention: {order_101}")
print(f"Order 102 needs attention: {order_102}")
print(f"Order 103 needs attention: {order_103}")    

custom_result = needs_attention("pending", 12, threshold=15)
print(f"Custom result for order with 12 minutes waiting and threshold of 15: {custom_result}") #false
