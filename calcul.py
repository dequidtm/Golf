
import confBDD
import math
import CSV_golf
from datetime import datetime



def calculDPV(temperature, humidité_air):
    SVP = math.exp((13.7 - 5120 / ( temperature + 273.15 ))) * 1000
    print (SVP)
    DPV =  (( 100 - humidité_air ) / 100) * SVP
    print (DPV)
    return (DPV)

def calcul_arrosage(arduino_id, temperature, humidité_air, humidité_sol):
    DPV = calculDPV(temperature, humidité_air)
    String_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    CSV_name = datetime.now().strftime("%Y-%m-%d") + '.csv'
    connection = confBDD.getConnection()
    if (DPV > 4.5 and DPV < 12.5 and humidité_sol > 15 and humidité_sol < 30):
        arrosage = 0
    else :
        sql = "SELECT * FROM water WHERE water_day = " + str(datetime.now().weekday()) + ";"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        for row in cursor :
            print(row)
            if (row["water_start"] < datetime.now().hour and row["water_end"] > datetime.now().hour ) :
                arrosage = 1
            else :
                arrosage = 0
        
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO info (info_type, info_arduino, info_value, info_date) VALUES('%s','%s','%s','" + String_now + "')"
            cursor.execute(sql,(1, arduino_id, temperature))
            cursor.execute(sql,(2, arduino_id, humidité_air))
            cursor.execute(sql,(3, arduino_id, humidité_sol))
            cursor.execute(sql,(4, arduino_id, arrosage))
    finally:     
        connection.close()
        chaine_CSV = [String_now, str(arduino_id), str(temperature), str(humidité_air), str(humidité_sol),str(arrosage)]
        print(chaine_CSV)
        if not CSV_golf.csv_exist(CSV_name) :
            CSV_golf.inserer(CSV_name, ["Heure","Arduino_id","Temperature","Humidite_air","Humidite_sol","Arrosage"])
        CSV_golf.inserer(CSV_name, chaine_CSV)
    return (arrosage*arduino_id)


