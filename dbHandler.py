import sqlite3
conn=sqlite3.connect('Info.db')
def initDB():
    global conn
    conn.execute("create table if not exists Teams(TeamName text,TeamNum int)")
    conn.execute("create table if not exists Matchs(MatchNumber int,Compitions )")
    conn.execute("create table if not exists Compitions(Name text, Date int)")
    conn.execute("create table if not exists MatchScoring(MatchId int, TeamNum1 int, TeamNum2 int, Allince text,Team1_BoxToHub int, Team2_BoxToHub int, Team1_BoxToLevel int, Team2_boxToLevel int,Team1_Duck int, Team2_duck int, Team1_Park int, Team2_park int, Team1_ExtraCubes int, Team2_ExtraCubes int)")

def TeamDropDown():
    global conn
    c = conn.cursor()
    c.execute("select distinct TeamName From Teams;")
    return list(c.fetchall())

