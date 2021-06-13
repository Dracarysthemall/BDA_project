import sqlite3
from math import cos, asin, sqrt, pi



def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) #2*R*asin...


conn = sqlite3.connect('iot_database.db')
c = conn.cursor()

def minOfDistancesByClient(id):
    min=10000
    c.execute('SELECT lat, lon FROM Client where id=?',[id])
    data = c.fetchone()
    latClt=data[0]
    lonClt=data[1]
    c.execute('SELECT lat, lon, id FROM Taxi')
    data = c.fetchall()
    f = open("Distances_for_client_"+str(id)+".txt", "w")
    for row in data:
        dist=distance(latClt, lonClt, row[0], row[1])
        if(dist<min):
            min=dist
        f.write("id:"+str(row[2])+", distance:"+str(dist)+"\n")
    f.close()    
    return min
print(str(minOfDistancesByClient(3)))

