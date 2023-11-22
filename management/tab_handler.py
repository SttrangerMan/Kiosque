from management.product_handler import get_product_by_id


def calculate_tab(table):
    subtotal = 0
    for t in table:
        product = get_product_by_id(t['_id'])
        subtotal += product['price'] * t['amount']
        Formatted_text = {'subtotal': '$' + str(round(subtotal, 2))}
    return Formatted_text