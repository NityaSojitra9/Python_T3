import socket 
host=socket.gethostname()
port=7000
client=socket.socket()
client.connect((host,port))
msg=input("HIIII")
while msg.lower()!='bye':
    client.send(msg.encode())
    data=client.recv(1024).decode()
    print(data)
    msg=input("405")
client.close()
