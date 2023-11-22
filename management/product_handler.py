from menu import products


def add_product(original_products, **kwargs):

    current_id = 0
    if not original_products:
        next_id = 1
    else:
        for product in original_products:
            if (product["_id"] > current_id):
                current_id = product["_id"]
        next_id = current_id + 1

    new_product = {
        "_id": next_id,
        "title": kwargs['title'],
        "price": kwargs['price'],
        "rating": kwargs['rating'],
        "description": kwargs['description'],
        "type": kwargs['type']
    }    
            
    original_products.append(new_product)
    return new_product


def get_product_by_id(product_id: int):
    if isinstance(product_id, int):
        for product in products:
            if (product['_id'] == product_id):
                return product
        return {}
    else:
        raise TypeError("product id must be an int")


def get_products_by_type(product_type: str):
    if isinstance(product_type, str):
        try:
            product = [p for p in products if p['type'] == product_type]
            return product
        except IndexError:
            return {}
    else: 
        raise TypeError("product type must be a str")
    

def menu_report():
    price = 0
    product_count = len(products)
    common_type = {}
    for p in products:
        price += p['price'] / product_count
        average_price = round(price, 2)

        type = p["type"]
        if type in common_type:
            common_type[type] += 1
        else:
            common_type[type] = 1
    most_common_type = max(common_type, key=common_type.get)
    formatted_text = "Products Count: " + str(product_count) + " - Average Price: " "$" + str(average_price) + " - Most Common Type: " + str(most_common_type)
    return formatted_text