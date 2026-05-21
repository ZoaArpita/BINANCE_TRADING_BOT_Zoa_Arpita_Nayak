import argparse
import sys
from bot.orders import OrderManager
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_configure import logger

def print_summary(args):
    print("\n" + "=" * 30)
    print("ORDER REQUEST SUMMARY")
    print("=" * 30)
    print(f"Symbol:   {args.symbol.upper()}")
    print(f"Side:     {args.side}")
    print(f"Type:     {args.order_type}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price:    {args.price}")
    print("=" * 30 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    # Define the required CLI flags
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=validate_side, required=True, help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", type=validate_order_type, required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=validate_quantity, required=True, help="Amount to trade")
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)", default=None)

    args = parser.parse_args()

    # Rule verification: Limit orders MUST have a price
    if args.order_type == "LIMIT" and args.price is None:
        logger.error("Missing price for LIMIT order.")
        print("Error: --price is required when --type is LIMIT")
        sys.exit(1)

    print_summary(args)

    try:
        manager = OrderManager()
        response = manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )

        # Clear success output parsing
        print("ORDER PLACED SUCCESSFULLY!")
        print("-" * 30)
        print(f"Order ID:      {response.get('orderId')}")
        print(f"Status:        {response.get('status')}")
        print(f"Executed Qty:  {response.get('executedQty')}")
        avg_price = response.get('avgPrice')
        if avg_price and float(avg_price) > 0:
            print(f"Average Price: {avg_price}")
        print("-" * 30 + "\n")

    except Exception as e:
        print(f"ORDER FAILED: {e}\n")


if __name__ == "__main__":
    main()