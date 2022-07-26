from ast import While, arg
from asyncio import constants
from random import random
import socket
import threading
import json
from time import sleep

SERVER = "127.0.0.1"
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)

s.listen(1)
print("Waiting For a connection, Server Started")


def client_thread(conn, addr):
    num = 0

    while True:
        num += 1
        try:
            data = conn.recv(2048)
            recv = data.decode("utf-8")
            values = ""
            try:
                print(data.decode("utf-8"))
                values = json.loads(recv)
                print(values["ints"][1])

                values["ints"][1] = 0
                print(values)
                conn.send(str.encode(json.dumps(values)))
            except:
                pass

        except:
            break

    conn.close()

    print(f"Connection Lost From: {addr}")


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    # Recv data test
    data = conn.recv(2048)
    print(data.decode("utf-8"))

    conn.send(str.encode("connection accepted"))

    thread = threading.Thread(target=client_thread, args=(conn, addr,))
    thread.start()
