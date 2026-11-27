def calculate_order_total(items, discount=0, tax_rate=0.18):
    subtotal = 0

    for item in items:
        subtotal += item["price"]

    subtotal = subtotal - (subtotal * discount)

    if subtotal > 500:
        shipping = 0
    else:
        shipping = 50

    total = (subtotal + shipping) * (1 + tax_rate)

    return round(total, 2)


def process_order(items, discount=0, tax_rate=0.18):
    if not items:
        return {"success": True, "total": 0}

    total = calculate_order_total(items, discount, tax_rate)

    return {
        "success": True,
        "total": total,
        "item_count": len(items),
        "message": "Order processed successfully"
    }
