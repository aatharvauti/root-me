# To start this test using the TCP protocol, you need to connect to a program on a network socket.

# Calculate the square root of number 1 and multiply by number 2.
# Then round the result to two decimal places.
# You have 2 seconds to send the correct answer from the moment the program sends you the calculation.
# The answer must be sent in the form of int
 
import socket
import re
import struct


def connect_to_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:
        client_socket.settimeout(10)  # 5 seconds timeout

        # Connect
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

        num1, num2 = extract_numbers(data.decode('utf-8'))
        if num1 is not None and num2 is not None:
            answer = calculate_solution(num1, num2)
            
            # .encode('utf-8') converts string to bytes, so the integer has been converted to string to bytes
            # + b'\r\n' concatenates the bytes from the previous step and adds a new line

            # the entire line of code converts the floating-point answer to a string, 
            # encodes it into bytes using UTF-8, appends a newline in bytes, 
            # and then sends this byte sequence to the server

            client_socket.sendall(str(answer).encode('utf-8') + b'\r\n')
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


def extract_numbers(message):

    # Define a regular expression pattern to match numbers
    number_pattern = r'\d+'
    matches = re.findall(number_pattern, message)

    # Extract the first two numbers found
    if len(matches) >= 3:
        first_number = int(matches[1])
        second_number = int(matches[2])
        return first_number, second_number
    else:
        print("Not enough numbers for calculation.")
        return None, None


def calculate_solution(num1, num2):
    return round((num1**0.5)*num2, 2)


if __name__ == "__main__":
    server_host = "challenge01.root-me.org"
    server_port = 52002

    connect_to_socket(server_host, server_port)
