import random
import socket
import pickle
import threading
import time
import pandas as pd
from tkinter import *
from os import path
from random import randint
window = Tk()
window.title("Server")
window.geometry('350x200')
multicast_addr = '224.0.0.3'
bind_addr = '0.0.0.0'          
port = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((bind_addr, port))
name = "Server"
def thread_function():
    while True:
        message, address = sock.recvfrom(255)
        values = pickle.loads(message)
        if(values[0] != name and values[1] == "puntajes"):
            df = pd.read_csv('datos.csv', delimiter = ',')
            for index, row in df.iterrows():
                print(row[1])
                values=["puntajes", row[0], row[1]]
                data=pickle.dumps(values)
                sock.sendto(data, (multicast_addr, port))
        elif(values[0] != name and values[1] == "Add"):
            df = pd.read_csv('datos.csv', delimiter = ',')
            df = df.append({'usuario': values[0], "score":0}, ignore_index=True)
            df.to_csv('datos.csv', index=False)
        elif (values[0] != name and values[1] == "Update"):
            df = pd.read_csv('datosata.json', delimiter = ',')
            df.loc[df['usuario'] == values[0], 'puntajes'] = int(values[2])
            df.to_csv('datos.csv', index=False)

x = threading.Thread(target=thread_function)
x.start()

window.mainloop()


