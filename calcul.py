
import confBDD
import math
from datetime import datetime



def calculDPV(temperature, humidité_air):
    SVP = math.exp((13.7 - 5120 / ( temperature + 273.15 ))) * 1000
    print (SVP)
    DPV =  (( 100 - humidité_air ) / 100) * SVP
    print (DPV)
    return (DPV)

def calcul_arrosage(arduino_id, temperature, humidité_air, humidité_sol):
    DPV = calculDPV(temperature, humidité_air)
    connection = confBDD.getConnection()
    if (DPV > 4.5 and DPV < 12.5 and humidité_sol > 15 and humidité_sol < 30):
        arrosage = 0
    else :
        arrosage = 1
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO info (info_type, info_arduino, info_value, info_date) VALUES('%s','%s','%s','" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "')"
            cursor.execute(sql,(1, arduino_id, temperature))
            cursor.execute(sql,(2, arduino_id, humidité_air))
            cursor.execute(sql,(3, arduino_id, humidité_sol))
            cursor.execute(sql,(4, arduino_id, arrosage))
    finally:     
        connection.close()
    return (arrosage*arduino_id)


