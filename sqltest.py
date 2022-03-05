import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE Teams(
    
);''')
conn.commit()
conn.close()