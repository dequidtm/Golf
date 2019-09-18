
import confBDD
import math


def calculDPV(temperature, humidité_air):
    SVP = math.exp((13.7 - 5120 / ( temperature + 273.15 ))) * 1000
    print (SVP)
    DPV =  (( 100 - humidité_air ) / 100) * SVP
    print (DPV)
    return (DPV)

def calcul_arrosage(ID_capteur, temperature, humidité_air, humidité_sol):
    DPV = calculDPV(temperature, humidité_air)
    connection = confBDD.getConnection()
    if (DPV < 4.5 && DPV > 12.5 && humidité_sol < 15 && humidité_sol > 30):
        
    elif

    try:
    with connection.cursor() as cursor:
        sql = ""
        cursor.execute(sql)
    finally:     
    connection.close()
    return 0


