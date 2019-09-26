import calcul
import CSV_golf 
from threading import Thread
print(CSV_golf.csv_exist('test1.csv'))
CSV_golf.inserer('test.csv',["1;2;3"])
Thread.start(calcul.calcul_arrosage(1,15,50,25))

