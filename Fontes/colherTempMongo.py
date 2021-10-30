from pymongo import MongoClient
import serial
import simplejson
from datetime import datetime


def gravar_dados(json):
    cliente = MongoClient("localhost", 27017)
    db = cliente['coleta']
    col = db['dados']
    chv = col.insert_one(json)
    print("Registro Inserido: ", chv.inserted_id)
    cliente.close()


def ler_dados_serial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    i = 0
    while i < 10:
        try:
            ler = ser.readline()
            json = simplejson.loads(ler)
        except (Exception) as error:
            print("Falhou para ler o registro", error)
            continue
        dt_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        json["data"] = dt_str
        print(json)
        gravar_dados(json)
        i = i + 1


if __name__ == '__main__':
    ler_dados_serial()
