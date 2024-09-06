import mysql.connector
from mysql.connector import Error

def connect_to_azure_mysql():
    try:
        # Create a connection object
        connection = mysql.connector.connect(
            host='glamifydb.mysql.database.azure.com',  # Azure MySQL hostname
            user='admin123',            # MySQL username (format: username@server-name)
            password='Glamify123',                  # MySQL user password
            database='glamify-records',              # The database you want to connect to
            port=3306,                                 # Default MySQL port
        )
        
        if connection.is_connected():
            print("Connected to Azure MySQL database!")
            # Optionally, you can fetch and print server details:
            db_info = connection.get_server_info()
            print(f"Server version: {db_info}")
            
            # Sample query to test the connection
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function to connect
connect_to_azure_mysql()
