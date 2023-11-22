from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report
from management.tab_handler import calculate_tab
from menu import products

if __name__ == "__main__":
#     table = [
#         {"_id": 10, "amount": 3},
#         {"_id": 20, "amount": 2},
#         {"_id": 21, "amount": 5},
#     ]
#     print(calculate_tab(table))
    # print(get_product_by_id("abc"))
    # print(add_product(products, title="abc", price=12, rating=3, description="Raw asparagus", type="vegetable"))
    # print(get_products_by_type(1))
    print(menu_report())