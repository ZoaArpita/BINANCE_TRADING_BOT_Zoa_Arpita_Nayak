import argparse

def validate_side(value):
    val = value.upper()

    if val not in ["BUY","SELL"]:
        raise argparse.ArgumentTypeError(f"Invalid side. Must be BUY or SELL.")
    return val

def validate_order_type(value):
    val = value.upper()
    if val not in ["MARKET", "LIMIT"]:
        raise argparse.ArgumentTypeError(f"Invalid type. Must be MARKET or LIMIT.")
    return val

def validate_quantity(value):
    try:
        val = float(value)
        if val <= 0:
            raise ValueError
        return val
    except ValueError:
        raise argparse.ArgumentTypeError("Quantity must be a positive number.")