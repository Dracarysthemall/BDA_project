import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

fig, axes= plt.subplots(3, 2, figsize=(15, 10))
fig.suptitle('IoT Sensors Data Visualisation', fontsize=20)

conn = sqlite3.connect('iot_database.db')
c = conn.cursor()


# Temperature Data Visalisation

c.execute('SELECT id, Temperature FROM Tem')
data = c.fetchall()

id = []
Temperature = []

for row in data:
    id.append(row[0])
    Temperature.append(row[1])


axes[0,0].plot(id, Temperature, 'tab:red')
axes[0,0].set_title('Temperature Data')
axes[0,0].set_ylabel('Temperature Cº')


# Humidity Data Visalisation

c.execute('SELECT id, Humidity FROM Hum')
data = c.fetchall()

id = []
Humidity = []

for row in data:
    id.append(row[0])
    Humidity.append(row[1])

axes[0, 1].plot(id, Humidity, 'tab:blue')
axes[0, 1].set_title('Humidity Data')
axes[0, 1].set_ylabel('Humidity g/m3')


# Acceleration X Data Visalisation

c.execute('SELECT id, accX FROM Acc')
data = c.fetchall()

id = []
accX = []

for row in data:
    id.append(row[0])
    accX.append(row[1])

axes[1, 0].plot(id, accX, 'tab:green')
axes[1, 0].set_title('Acceleration X Data')
axes[1, 0].set_ylabel('m/s2')

# Acceleration Y Data Visalisation

c.execute('SELECT id, accY FROM Acc')
data = c.fetchall()

id = []
accY = []

for row in data:
    id.append(row[0])
    accY.append(row[1])

axes[1, 1].plot(id, accX, 'tab:green')
axes[1, 1].set_title('Acceleration Y Data')
axes[1, 1].set_ylabel('m/s2')

# GPS lat Data Visalisation

c.execute('SELECT id, lat FROM GPS_Data')
data = c.fetchall()

id = []
tight_layout = []

for row in data:
    id.append(row[0])
    tight_layout.append(row[1])

axes[2, 0].plot(id, tight_layout, 'tab:orange')
axes[2, 0].set_title('GPS lat Data')
axes[2, 0].set_ylabel('deg')

# GPS lon Data Visalisation

c.execute('SELECT id, lon FROM GPS_Data')
data = c.fetchall()

id = []
lon = []

for row in data:
    id.append(row[0])
    lon.append(row[1])

axes[2, 1].plot(id, lon, 'tab:green')
axes[2, 1].set_title('GPS lon Data')
axes[2, 1].set_ylabel('deg')


fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()