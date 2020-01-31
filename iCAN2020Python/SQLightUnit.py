import sqlite3

# Create database in memory
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

# Create a table
curs.execute("CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")

# Insert a row of data
curs.execute("INSERT INTO persons(name) values('Mike')")
curs.execute("INSERT INTO persons(name) values('John')")
curs.execute("INSERT INTO persons(name) values('Will')")

# Update data
curs.execute("UPDATE persons SET name = 'Michael' WHERE name = 'Mike'")

# Delete data
curs.execute("DELETE FROM persons WHERE name = 'Michael'")

# Save (commit) the changes
conn.commit()

# Browse inserted data
curs.execute("SELECT * FROM persons")
print(curs.fetchall())

curs.close()
conn.close()
