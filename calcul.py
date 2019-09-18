
import confBDD
import math
 
connection = confBDD.getConnection()
 
print ("Connect successful!")

def calcul_arrosage(ID_capteur, temperature, humidité_air, humidité_sol):
    SVP = math.exp((13.7 - 5120 / ( temperature + 273.15 ))) * 1000
    print (SVP)
    DPV =  (( 100 - humidité_air ) / 100) * SVP
    print (DPV)
    connection = confBDD.getConnection()


    return 0;
