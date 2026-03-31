import random
from services.payment_service import process_payment

def process_order(order, users_db, products_db):
    user = users_db.get(order.user_id)
    if not user:
        raise Exception("User not found")

    total = 0
    items_detail = []

    for item in order.items:
        product = products_db.get(item.product_id)
        if not product:
            raise Exception(f"Product {item.product_id} not found")

        if product["stock"] < item.quantity:
            raise Exception("Insufficient stock")

        subtotal = product["price"] * item.quantity

        items_detail.append({
            "product_id": item.product_id,
            "name": product["name"],
            "quantity": item.quantity,
            "unit_price": product["price"],
            "subtotal": subtotal
        })

        total += subtotal

        # reduzir estoque
        product["stock"] -= item.quantity

    payment_status = process_payment(order.user_id, total, order.payment_method)

    return {
        "order_id": random.randint(1000, 9999),
        "user": user,
        "items": items_detail,
        "total": total,
        "payment_status": payment_status
    }
