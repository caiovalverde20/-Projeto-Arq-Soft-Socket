import socket
import os
import json
import re

def clean_text(text):
    # Remove a sintaxe wiki, HTML e caracteres especiais
    text = re.sub(r'==.*?==', '', text)
    text = re.sub(r'\{\|.*?\|\}', '', text, flags=re.DOTALL)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[\.,;:\'"!@#$%^&*\(\)_\+\-=\[\]\{\};<>/?\\|`~]', '', text)
    return text

def send_text(text, conn):
    text_bytes = text.encode('utf-8')
    conn.sendall(text_bytes)

def data_sender():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # ip e porta, talvez tenha que mudar
    server_socket.listen()

    print('Esperando conexão...')
    conn, addr = server_socket.accept()
    print(f'Conexão estabelecida com {addr}')

    directory = 'enwiki20201020'
    
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                print(f'Processando {file_path}...')
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    for item in data:
                        text = item.get('text', 'Campo "text" não encontrado')
                        cleaned_text = clean_text(text)
                        send_text(cleaned_text, conn)
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    data_sender()
