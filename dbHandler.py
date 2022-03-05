import sqlite3
conn=sqlite3.connect('Info.db')

def initDB():
    global conn
    conn.execute("create table if not exists Teams(TeamName text,TeamNum int)")
    conn.execute("create table if not exists Matchs(MatchNumber int,Compitions )")
    conn.execute("create table if not exists Compitions(Name text,)")