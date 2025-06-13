import socket
HOST = 'localhost'
PORT = 7002
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open("Transfer.ipynb", "rb") as f:
        s.sendfile(f)
    print("Notebook file sent successfully.")
