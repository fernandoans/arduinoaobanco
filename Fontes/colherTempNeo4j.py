from neo4j import GraphDatabase
import serial
import simplejson
from datetime import datetime

cqlCriar = "CREATE (:coleta { data: $data, ldr: $ldr, tempC: $tempC, tempF: $tempF})"


def gravar_dados(json):
    graphDB_Driver = GraphDatabase.driver(
        "bolt://localhost:7687", auth=("neo4j", "test"))
    with graphDB_Driver.session() as secao:
        secao.run(cqlCriar,
                  data=json["data"],
                  ldr=json["lums"],
                  tempC=json["grauC"],
                  tempF=json["grauF"])
        secao.close()


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
