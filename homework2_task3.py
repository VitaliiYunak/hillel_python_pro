discount = 0.1


def create_order(price):
    final_price = price*(1-discount)
    final_discount = discount

    def apply_additional_discount(add_discount):
        nonlocal final_price
        nonlocal final_discount
        final_price = price*(1-(discount + add_discount))
        final_discount = (discount + add_discount) * 100

    apply_additional_discount(0.1)
    print(f"Початкова ціна: {price}, кінцева ціна зі знижкою {final_discount:.0f}%: {final_price:.0f}")


create_order(1000)
