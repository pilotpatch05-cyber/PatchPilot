from app.services.payment import calculate_total


def process_payment():
    return calculate_total(100, 0.18)
