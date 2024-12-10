import duckdb
from datetime import datetime


# Connect to DuckDB
conn = duckdb.connect('/Users/rasagna/ingest_data_with_python/data/first_database.duckdb')

# Insert data into the 'order_states' table (without deadlines)
order_states_data = [
    {
        'orderId': 'O00001',
        'orderStatus': 'CREATED',
        'statusExecutedDttm': datetime(2024, 12, 10, 18, 0)
    },
    {
        'orderId': 'O00001',
        'orderStatus': 'PICKED',
        'statusExecutedDttm': datetime(2024, 12, 11, 15, 0)
    },
    {
        'orderId': 'O00001',
        'orderStatus': 'PACKED',
        'statusExecutedDttm': datetime(2024, 12, 11, 18, 0)
    },
    {
        'orderId': 'O00001',
        'orderStatus': 'SHIPPED',
        'statusExecutedDttm': datetime(2024, 12, 11, 15, 0)
    },
    {
        'orderId': 'O00001',
        'orderStatus': 'IN_TRANSIT',
        'statusExecutedDttm': datetime(2024, 12, 13, 10, 0)
    },
    {
        'orderId': 'O00001',
        'orderStatus': 'DELIVERED',
        'statusExecutedDttm': datetime(2024, 12, 15, 19, 0)
    },
]

# Insert into 'order_states' table, stateId is generated dynamically
for state in order_states_data:
    conn.execute("""
        INSERT INTO order_states (orderId, orderStatus, statusExecutedDttm) 
        VALUES (?, ?, ?)
    """, (state['orderId'], state['orderStatus'], state['statusExecutedDttm']))

# Fetch and display all the rows added to the 'order_states' table
added_rows = conn.execute("SELECT * FROM order_states WHERE orderId = 'O00001'").fetchall()

# Print the added rows
print(f"Order states data inserted")
for row in added_rows:
    print(row)

# Close the connection
conn.close()
