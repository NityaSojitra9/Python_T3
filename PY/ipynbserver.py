import socket
HOST = '0.0.0.0'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on port {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        with open("received_notebook.ipynb", "wb") as f:
             while True:
                data = conn.recv(4096)
                if not data:
                         break
                f.write(data)
    print("Notebook file received and saved as 'received_notebook.ipynb'.")
