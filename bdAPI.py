import psycopg2
from psycopg2 import sql
import json

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="northwind",
            user="faat",
            password="faat",
            host="localhost",
            port="2000"
        )
        print("Connection to database established successfully")
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None
    
def get_categories():
    connection = connect_to_db()
    if connection is None:
        return json.dumps({"error": "Failed to connect to the database"})

    try:
        cursor = connection.cursor()
        query = sql.SQL("SELECT category_id, category_name, description, picture FROM categories")
        cursor.execute(query)
        rows = cursor.fetchall()
        categories = []
        for row in rows:
            categories.append({
                "category_id": row[0],
                "category_name": row[1],
                "description": row[2],
                "picture": row[3].tobytes().hex() if row[3] else None
            })
        return json.dumps(categories)
    except Exception as error:
        print(f"Error fetching data: {error}")
        return json.dumps({"error": "Failed to fetch data"})
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    print(get_categories())