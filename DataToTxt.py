import sqlite3
from math import cos, asin, sqrt, pi

conn = sqlite3.connect('iot_database.db')
c = conn.cursor()


def TaxisToTxt():
    c.execute('SELECT lat, lon FROM Taxi')
    data = c.fetchall()

    for row in data:
        f = open("taxis.txt", "a")
        f.write(str(row[0])+"\t")
        f.write(str(row[1])+"\n")
        f.close()


def ClientsToTxt():
    c.execute('SELECT lat, lon FROM Client')
    data = c.fetchall()

    for row in data:
        f = open("clients.txt", "a")
        f.write(str(row[0])+"\t")
        f.write(str(row[1])+"\n")
        f.close()


        
ClientsToTxt()
TaxisToTxt()
# for i in range(0,lat.count,2): 
#     f = open("distancesData.txt", "a")
#     f.write(str(distance(lat[i], lon[i], lat[i+1], lon[i+1])))
#     f.close()
    
