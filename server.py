import socket
from notify import notification

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to specific address and port
SERVER_ADDR = (socket.gethostbyname(socket.gethostname()), 5050)
server.bind(SERVER_ADDR)

server.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client, client_address = server.accept()
    print(f"Connected to {client_address}")

    try:
        # Receive data from client
        data = client.recv(1024)
        print(f"Received: {data.decode()}")
        # Make the notification pop up on the server
        if data.decode() == "iMessage":
            notification('From: _____', message='iMessage Received', app_name='iMessage Notification')

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        print("Server closed")
        break

    finally:
        client.close()
