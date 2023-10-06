import socket

def python_processor():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))  # ip e porta, talvez tenha que mudar. Tem que ser igual ao do socket
    try:
        while True:
            text = client_socket.recv(1024) # numero maximo de bytes a serem recebidos de uma vez só
            if not text:
                break
            print(text)
    finally:
        client_socket.close()

if __name__ == "__main__":
    python_processor()
