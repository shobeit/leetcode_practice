def should_serve_customer(customer_age, on_break, time):
    if customer_age < 21:
        return False
    elif on_break:
        return False
    elif 5 > time or time > 10:
        return False
    else:
        return True
    