import sqlite3
from typing import Optional, List, Dict, Any
def get_customer_info(
        customer_id: str, 
        db_path: str = 'customer_data.db', 
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
        ) -> List[Dict[str, Any]]:
    """
    This function retrieves customer information from SQLite database with the customer ID.
    
    Problem1
    db_path is connection string by making it argument with a default value, it's easy to configure without changing the code
    """
    # Base query and parameters
    sql_query = "SELECT * FROM Customer WHERE id = ?"
    params = [customer_id]
    
    # Check if a date range is provided, extend the query and paramenters
    if start_date and end_date:
        sql_query += " And created_at BETWEEN ? AND ?"
        params.extend([start_date, end_date])


    try:
        # 'With' statement handle closing the connection automatically
        with sqlite3.connect(db_path) as conn:        
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
    
            cursor.execute(sql_query, tuple(params))

            customer_data = [dict(row) for  row in cursor.fetchall()]
            return customer_data
    
    except sqlite3.Error as e:
        # Catch SQLite database errors
        print(f"Database error occured: {e}")
        return []
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occured: {e}")
        return []
