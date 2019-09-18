
import confBDD
import math
from datetime import datetime


def calculDPV(temperature, humidité_air):
    SVP = math.exp((13.7 - 5120 / ( temperature + 273.15 ))) * 1000
    print (SVP)
    DPV =  (( 100 - humidité_air ) / 100) * SVP
    print (DPV)
    return (DPV)

def calcul_arrosage(ID_capteur, temperature, humidité_air, humidité_sol):
    DPV = calculDPV(temperature, humidité_air)
    connection = confBDD.getConnection()
    if (DPV > 4.5 and DPV < 12.5 and humidité_sol > 15 and humidité_sol < 30):
        arrosage = "non"
    else :
        arrosage = "oui"
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO MESURE (DATE_MESURE, ID_CAPTEUR, TEMPERATURE, HUMIDITE_AIR, HUMIDITE_SOL, ARROSAGE) VALUES('" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")  + "','" + ID_capteur + "','" + str(temperature) + "','" + str(humidité_air) + "','" + str(humidité_sol) + "','" + arrosage + "')"
            print (sql)
            cursor.execute(sql)
    finally:     
        connection.close()
    return 0


