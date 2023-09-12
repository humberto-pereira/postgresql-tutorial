import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database (cursor is similar to an object or a 
# list)
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table. | (use single cotes 
# ('') to wrap queries and double cotes("") to specify values) or it does not 
# work properly... the postgreSQL is the other way around.

cursor.execute('SELECT * FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
    