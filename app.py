import argparse
        "--symbol",
        required=True,
        help="Trading symbol, e.g., BTCUSDT"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=VALID_SIDES,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--order_type",
        required=True,
        choices=VALID_ORDER_TYPES,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required only for LIMIT orders"
    )

    args = parser.parse_args()

    try:
        validate_inputs(args)

        print_order_summary(args)

        client = BinanceFuturesClient()

        response = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price,
        )

        print_order_response(response)

        print("SUCCESS: Order placed successfully.")

    except ValueError as value_error:
        logger.error(value_error)
        print(f"INPUT ERROR: {value_error}")

    except BinanceAPIException as api_error:
        logger.error(api_error)
        print(f"BINANCE API ERROR: {api_error}")

    except Exception as error:
        logger.error(error)
        print(f"UNEXPECTED ERROR: {error}")


if __name__ == "__main__":
    main()