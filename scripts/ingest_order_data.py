import duckdb
import json
from datetime import datetime

# Connect to DuckDB 
conn = duckdb.connect('/Users/rasagna/ingest_data_with_python/data/first_database.duckdb')

# Retrieve the last used orderId sequence number
last_order_id = conn.execute("SELECT MAX(CAST(SUBSTR(orderId, 2) AS INTEGER)) FROM orders").fetchone()[0]

# If there are no existing orders, start with 0
if last_order_id is None:
    last_order_id = 0

# Generate the new orderId by incrementing the last orderId and adding the prefix 'O'
new_order_id = f'O{last_order_id + 1:05d}'

# Prepare the order data with deadlines
order_data = {
    'orderId': new_order_id,  # Use the generated orderId
    'sourceOrderId': 'S12345',
    'deliveryDate': datetime(2024, 12, 14).date(),
    'orderItems': [
        {'itemName': 'iPhone 15', 'itemId': 1, 'quantity': 1.0},
        {'itemName': 'iPhone Case', 'itemId': 2, 'quantity': 1.0}
    ],
    'shippingFromAddress': {
        'street': '123 Shipping Ave',
        'city': 'Shipped City',
        'state': 'SC',
        'zipcode': '5666678',
        'country': 'Country A'
    },
    'shippingToAddress': {
        'street': '456 Delivery Rd',
        'city': 'Delivered City',
        'state': 'DC',
        'zipcode': '5666789',
        'country': 'Country B'
    },
    # Add the deadlines
    'pickingDeadline': datetime(2024, 12, 11, 18, 0),  # Example picking deadline
    'packingDeadline': datetime(2024, 12, 11, 20, 0),  # Example packing deadline
    'shippingDeadline': datetime(2024, 12, 12, 18, 0)  # Example shipping deadline
}

# Convert JSON data to strings for insertion
order_items_json = json.dumps(order_data['orderItems'])
shipping_from_address_json = json.dumps(order_data['shippingFromAddress'])
shipping_to_address_json = json.dumps(order_data['shippingToAddress'])

# Insert into the 'orders' table with the generated orderId and deadlines
conn.execute("""
    INSERT INTO orders (orderId, sourceOrderId, deliveryDate, orderItems, shippingFromAddress, shippingToAddress, 
                        pickingDeadline, packingDeadline, shippingDeadline) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (order_data['orderId'], order_data['sourceOrderId'], order_data['deliveryDate'], 
      order_items_json, shipping_from_address_json, shipping_to_address_json, 
      order_data['pickingDeadline'], order_data['packingDeadline'], order_data['shippingDeadline']))

# After insertion, confirm by printing the inserted orderId
print(f"Order data inserted with custom orderId: {new_order_id}")

# Close the connection
conn.close()
