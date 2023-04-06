import sqlite3

try:
    # SQLite = sqlite3
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
    # Write a query and execute it with cursor
    query = 'select sqlite_version()'
    cursor.execute(query)
    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
    # drop the impact table if already exists
    cursor.execute('DROP TABLE IF EXISTS Impact')
    # creating table
    table = """ CREATE TABLE Impact (
                Email VARCHAR(255) NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25)); """

    # Queries to INSERT records.
    cursor.execute('''INSERT INTO Impact VALUES ('Emaill1', 'Anne', 'Watson')''')
    cursor.execute('''INSERT INTO Impact VALUES ('Emaill2', 'Marianne', 'Joe')''')
    cursor.execute('''INSERT INTO Impact VALUES ('Emaill3', 'Enny', 'Swift')''')
    # Display data inserted
    print('Data Inserted in the table: ')
    data = cursor.execute('''SELECT * FROM Impact''')
    for row in data:
        print(row)
    # Commit your changes in the database
    sqliteConnection.commit()
    print('Table is ready')
    # Close the cursor
    cursor.close()
# Handle errors
except sqlite3.Error as error:
    print('Error occured - ', error)
#Close DB Connection iresspective of succes or failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')

    request = 'sql-'