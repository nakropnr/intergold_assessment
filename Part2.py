import sqlite3

def get_customer_info(customer_id: str, db_path: str = 'customer_data.db') -> list:
    """
    This function retrieves customer information from SQLite database with the customer ID.
    
    Problem1
    db_path is connection string by making it argument with a default value, it's easy to configure without changing the code
    """
    #initialize an empty list
    customer_data = []
    
    #Problem3
    #try-except block is the error handling mechanism
    try:
        # 'With' statement handle closing the connection automatically
        with sqlite3.connect(db_path) as conn:   
        
            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()
            #problem2
            #this is the placeholder for customer_id that prevent SQL injection
            sql_query = "SELECT * FROM Customer WHERE id = ?"

            cursor.execute(sql_query, (customer_id,))

            rows = cursor.fetchall()

            for row in rows:
                customer_data.append(dict(row))
            return customer_data
    
    except sqlite3.Error as e:
        # Catch SQLite database errors
        print(f"Database error occured: {e}")
        return []
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occured: {e}")
        return []

    