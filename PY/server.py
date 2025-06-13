import socket 
host=socket.gethostname()
port=7000
server=socket.socket()
server.bind((host,port))
server.listen()
conn,add=server.accept()
print("client add",add)
while True:
    data=conn.recv(1024).decode()
    print(data)
    if not data:
        break
    data=input("stop")
    conn.send(data.encode())
conn.close()
