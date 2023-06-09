import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9023))
while True:
    data = sock.recv(1024).decode()
    if data == "off":
        break
    else:
        try:
            with open(f"{data}.txt", "r+") as f:
                text = f.readline()
            sock.send(bytes(text, encoding="UTF-8"))
            data = sock.recv(1024).decode()
            print(f"Ответ: {data}")
        except:
            sock.send(bytes("error", encoding="UTF-8"))
sock.close()