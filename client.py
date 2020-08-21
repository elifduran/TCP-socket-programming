import time
from socket import *

host = str(input("Enter server address: "))
port = 1234

ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect(host, port)

print('Waiting for the connection...')

name = input('İsminizi giriniz:')
ClientSocket.send(name.encode())
server_name = ClientSocket.recv(1024)
server_name = server_name.decode()
print(server_name, 'hazır!')

kelimeler = []

def check_time(x,y):
    e = x - y
    if e > 2000:
        print("time is up", server_name, "kazandı!")

while True:
    server_message = ClientSocket.recv(1024)
    server_message = server_message.decode()
    first_time = time.time()
    kelimeler.append(server_message)
    print((server_name, server_message))
    client_message = input("Kelime giriniz:")
    a = len(server_message)
    if client_message not in kelimeler:
        if server_message[a-2:a] == client_message[0:2]:
            finish_time = time.time()
            ClientSocket.send(client_message.encode())
            check_time(finish_time, first_time)
        elif client_message == 'exit':
            print(name, 'terk etti!')
        else:
            print('Gönderemezsiniz.')
    else:
        print("Daha önce kullanılmamış bir kelime seçiniz.")
