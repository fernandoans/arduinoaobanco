# Bibliotecas
import psycopg2
import serial
import simplejson
from datetime import datetime


def gravar_dados(conn, JSON):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO projetoint.dados (datahora, ldr, tempC, tempF)
            VALUES (%(data)s, %(lums)s, %(grauC)s, %(grauF)s);
            """, JSON)
        conn.commit()
        count = cursor.rowcount
        print(count, "Registro inserido com sucesso!")
    except (Exception) as error:
        print("Falhou para inserir registro!", error)


def ler_dados_serial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    con = psycopg2.connect(
        "host=localhost port=5432 dbname=postgres user=postgres password=postgres")
    i = 0
    while i < 10:
        try:
            ler = ser.readline()
            json = simplejson.loads(ler.decode('utf8').replace("'", '"'))
        except (Exception) as error:
            print("Falhou para ler o registro", error)
            continue
        dt_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        json["data"] = dt_str
        gravar_dados(con, json)
        i = i + 1


if __name__ == '__main__':
    ler_dados_serial()
