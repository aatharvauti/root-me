import socket

def connect_to_socket(host, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Send data to the server
        message = "Hello, server!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        # Receive data from the server
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    # Change these values to match your server's address
    server_host = "localhost"
    server_port = 12345

    connect_to_socket(server_host, server_port)
