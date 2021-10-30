# Bibliotecas
import redis
import serial
import simplejson
from datetime import datetime


def gravar_dados(json):
    r = redis.Redis(host='localhost', port='6379')
    with r.pipeline() as pipe:
        chave = json["data"]
        pipe.hset(chave, "ldr", json["lums"])
        pipe.hset(chave, "tempC", json["grauC"])
        pipe.hset(chave, "tempF", json["grauF"])
        pipe.execute()
    r.bgsave()
    r.close()


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
