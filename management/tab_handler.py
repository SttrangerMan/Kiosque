from management.product_handler import get_product_by_id


def calculate_tab(table):
    subtotal = 0
    for t in table:
        product = get_product_by_id(t['_id'])
        subtotal += product['price'] * t['amount']
        formatted_text = {'subtotal': '$' + str(round(subtotal, 2))}
    return formatted_text
