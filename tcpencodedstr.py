# To start this test using the TCP protocol, you need to connect to a program on a network socket.

#  You must decode the encoded character string sent by the program.
#  You have 2 seconds to send the correct answer from the moment the program sends you the string.
#  The answer must be sent as a string.
 
import socket
import re
import base64


def connect_to_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.settimeout(10) # 5 seconds timeout

        # Connect
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

        pattern = r"'(.*?)'" # This pattern captures content within single quotes
        question = re.findall(pattern, data.decode('utf-8'))

        answer = base64.b64decode(question[0])
        answer = answer.decode('utf-8')

        # The string is encoded to bytes and a new line is added to make it behave as a string
        client_socket.sendall(str(answer).encode('utf-8') + b'\n')
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

    except socket.error as e:
        print(f"Socket error: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        print("Connection closed")


if __name__ == "__main__":
    server_host = "challenge01.root-me.org"
    server_port = 52023

    connect_to_socket(server_host, server_port)
