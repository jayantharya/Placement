from db_connection import connect_db

try:
    conn = connect_db()
    
    # Check if 'conn' exists BEFORE checking if it is connected
    if conn and conn.is_connected():
        print("Connection to the database was successful")
        conn.close() # Safely close it only if it was open
    else:
        print("Could not establish a connection to the database.")
        
except Exception as e:
    print(f"An unexpected error occurred: {e}")