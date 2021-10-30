from cassandra.cluster import Cluster
import serial
import simplejson
from datetime import datetime


def unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()


def unix_time_millis(dt):
    return int(unix_time(dt) * 1000.0)


def gravar_dados(session, JSON):
    try:
        session.execute("""
            INSERT INTO dados (datahora, ldr, tempC, tempF)
            VALUES (%(data)s, %(lums)s, %(grauC)s, %(grauF)s);
            """, JSON)
        print("Registro inserido com sucesso!")
    except (Exception) as error:
        print("Falhou para inserir registro!", error)


def ler_dados_serial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    cluster = Cluster()
    session = cluster.connect()
    session.execute("USE coleta;")

    i = 0
    while i < 10:
        try:
            ler = ser.readline()
            json = simplejson.loads(ler)
        except (Exception) as error:
            print("Falhou para ler o registro: ", ler)
            continue
        dt_long = unix_time_millis(datetime.now())
        json["data"] = dt_long
        gravar_dados(session, json)
        i = i + 1


if __name__ == '__main__':
    ler_dados_serial()
