import socket

sock = socket.socket()
print('Запуск сервера...')
sock.bind(('', 9090))
print('Начало прослушивания порта...')
sock.listen(1)
conn, addr = sock.accept()
print('Подключение клиента...')
print(addr)

msg = ''

flag = True
while flag == True:
    print('Прием данных от клиента...')
    data = conn.recv(1024)

    if not data:
        break

    msg = data.decode()

    print(msg)

    if msg == 'stop':
        print('Отключение клиента...')
        stop_msg = 'Отключаю клиента. Сервер закончил свою работу'
        conn.send(stop_msg.encode())
        break

    print('Отправка данных клиенту...')
    conn.send(data)

print('Остановка сервера...')
conn.close()
