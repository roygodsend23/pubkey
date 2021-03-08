#!/usr/bin/env python

import socket
import threading
from typing import Tuple

SERVER_NAME = ""
SERVER_PORT = 5230
BUFFER_SIZE = 1024

def socket_handler(connection: socket.socket, address: Tuple[str, int]):
    print(f"Receive connection from {address}")

    input_value_bytes = connection.recv(BUFFER_SIZE)
    input_value = input_value_bytes.decode("UTF-8")
    print(f"Receive input from {address}: {input_value}")

    output_value = logic(input_value)
    output_value_bytes = output_value.encode("UTF-8")

    connection.send(output_value_bytes)
    connection.close()

def logic(input_value: str):
    output_value = {}
    for char in input_value:
        if char in output_value.keys():
            output_value[char] += 1
        else:
            output_value[char] = 1
    return str(output_value)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((SERVER_NAME, SERVER_PORT))
        sc.listen(0)

        print("Example Socket Server Program")
        print("Hit Ctrl+C to terminate the program")

        while True:
            connection, address = sc.accept()

            thread = threading.Thread(target=socket_handler,args=(connection,address))
            thread.start()

if __name__ == "__main__":
    main()