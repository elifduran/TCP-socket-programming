import socket
import time

print('Welcome to chat!')

port = 1234
host = ''
server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_Socket.bind((host, port))
server_Socket.listen(2)
connection, add = server_Socket.accept()
name = input('İsminizi giriniz:')

Client_name = connection.recv(1024)
Client_name = Client_name.decode()
print(Client_name, "hazır!")
connection.send(name.encode())
kelimeler = []

def check_time(x,y):
    e = x-y
    if e > 200:
        print("time is up", Client_name, "kazandı.")

while True:
    server_message = input('Kelime giriniz:')
    if server_message not in kelimeler:
        start_time = time.time()
        connection.send(server_message)
        kelimeler.append(server_message)
    elif server_message == 'exit':
        print(Client_name, 'terk etti!')
    else:
        print("Kullanılmamış bir kelime seçiniz.")

    client_message = connection.recv(1024)
    client_message = client_message.decode()
    finish_time = time.time()
    print(Client_name, client_message)
    check_time(finish_time, finish_time)








