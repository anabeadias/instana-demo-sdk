import time
import random

def process_payment(user_id, amount, method):
    time.sleep(0.5)  # simula latência externa
    
    if random.choice([True, True, True, False]):
        return "approved"
    else:
        raise Exception("Payment failed")