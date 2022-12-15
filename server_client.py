import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

print('Соединение с сервером...')
try:
    sock.connect(('localhost', 9090))
    print('Вы успешно подключены к серверу!')
except:
    print('Error')
    exit()

while True:
    msg = input()

    print('Отправка данных серверу...')
    sock.send(msg.encode())

    data = sock.recv(1024)

    print('Прием данных от сервера: ')
    print(data.decode())

    if msg == 'stop':
        print('Разрыв соединения с сервером...')
        sock.close()
        break
