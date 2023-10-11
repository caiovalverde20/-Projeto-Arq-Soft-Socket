from sklearn.feature_extraction.text import TfidfVectorizer
import socket
import numpy as np

def receive_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))  

    received_data = b""  
    while True:
        data = client_socket.recv(1024)  
        if not data:
            break
        received_data += data

    text = received_data.decode('utf-8')

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    
    vocab = tfidf_vectorizer.get_feature_names_out()
    tfidf_values = tfidf_matrix.toarray()[0]

    term_tfidf = dict(zip(vocab, tfidf_values))

    sorted_terms = sorted(term_tfidf.items(), key=lambda x: x[1], reverse=True)

    top_10_terms = sorted_terms[:10]

    print("Os 10 termos mais frequentes:")
    for term, tfidf in top_10_terms:
        print(f"{term}: {tfidf}")

    client_socket.close()

if __name__ == "__main__":
    receive_data()
