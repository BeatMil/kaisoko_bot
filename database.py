import sqlite3

sqliteConnection = None

def connect_to_database():
    # Connect to database
    try:
        # Connect to DB and create a cursor
        global sqliteConnection
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')
     
        # Write a query and execute it with cursor
        query = 'select sqlite_version();'
        cursor.execute(query)
     
        # Fetch and output result
        result = cursor.fetchall()
        print('SQLite Version is {}'.format(result))
     
        # Close the cursor
        cursor.close()
     
    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred - ', error)
     

def disconnect_from_database():
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')


# def create_a_table():
#     global sqliteConnection
#     sqliteConnection.execute('''
#     CREATE TABLE asmr (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL UNIQUE,
#         nation TEXT NOT NULL 
#     );
#     ''')
#     print("==Table asmr created!==")


def print_from_a_table():
    global sqliteConnection
    cursor = sqliteConnection.execute("SELECT * from asmr ")
    for row in cursor:
        print(row)
    print("==Printed from asmr table==")


def list_all_tables():
    global sqliteConnection
    cursor = sqliteConnection.execute(".tables")
    print("==List all tables==")


def insert_into_asmr(name, nation):
    global sqliteConnection
    cursor = sqliteConnection.execute(
            f"INSERT INTO asmr (name, nation) VALUES ('{name}', '{nation}');")
    print("==New asmrtist inserted!==")
