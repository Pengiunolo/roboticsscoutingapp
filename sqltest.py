import sqlite3

conn = sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE Teams(
#    teamid int
#);''')
conn.execute("Insert into teams(teamid) Values(1)")
conn.execute("Insert into teams(teamid) Values(2)")
conn.execute("Insert into teams(teamid) Values(3)")
conn.execute("Insert into teams(teamid) Values(4)")
c = conn.cursor()
myquery = ("select distinct teamid from Teams;")
c.execute(myquery)
templist=list(c.fetchall())
conn.commit()
conn.close()
print(templist)