import sqlite3

DB_Name = "iot_database.db"
TableSchema = """
drop table if exists Taxi ;
create table Taxi(
    id integer primary key autoincrement,
    SensorID text,
    Date_Time text,  lat decimal(7,3),  
    lon decimal(7,3),  alt decimal(7,3));

drop table if exists Client ;
create table Client(
    id integer primary key autoincrement,
    SensorID text,
    Date_Time text,  lat decimal(7,3),  
    lon decimal(7,3),  alt decimal(7,3));


"""

# Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

# Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

# Close DB
curs.close()
conn.close()
