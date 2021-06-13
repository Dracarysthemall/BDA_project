import json
import sqlite3

# SQLite DB Name
DB_Name = "iot_database.db"


# ===============================================================
# Database Manager Class

class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return

    def __del__(self):
        self.cur.close()
        self.conn.close()

def Taxis_GPS_Data_Handler(jsonData):
    # Parse Data
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Data_and_Time = json_Dict['Date']
    lat = json_Dict['lat']
    lon = json_Dict['lon']
    alt = json_Dict['alt']

    # Push into DB Table
    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into Taxi (SensorID, Date_Time,lat, lon, alt) values (?,?,?,?,?)",
                                   [SensorID, Data_and_Time, lat, lon, alt])
    del dbObj
    print("\nInserted Taxi GPS_Data_Handler Data into Database.\n")

def Clients_GPS_Data_Handler(jsonData):
    # Parse Data
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Data_and_Time = json_Dict['Date']
    lat = json_Dict['lat']
    lon = json_Dict['lon']
    alt = json_Dict['alt']

    # Push into DB Table
    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into Client (SensorID, Date_Time,lat, lon, alt) values (?,?,?,?,?)",
                                   [SensorID, Data_and_Time, lat, lon, alt])
    del dbObj
    print("\nInserted Client GPS_Data_Handler Data into Database.\n")
# ===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
    if Topic == "Home/BedRoom/Topics/GPS":
        Clients_GPS_Data_Handler(jsonData)
    elif Topic == "Home/BedRoom/Topics/GPS":
        Taxis_GPS_Data_Handler(jsonData)

# ===============================================================