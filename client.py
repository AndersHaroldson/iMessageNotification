import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
server_address = ("INSERT_HOST_IP_HERE", 5050)
client.connect(server_address)

try:
    # Send data to the server
    message = "iMessage"
    client.sendall(message.encode())

finally:
    client.close()
