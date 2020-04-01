from pynput.keyboard import Key, Listener

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 44044
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP

def on_press(key):
    MESSAGE = f'{key}:press'.replace("'","")
    sock.sendto(bytes(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
    print(MESSAGE)

def on_release(key):
    MESSAGE = f'{key}:release'.replace("'","")
    sock.sendto(bytes(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
    print(MESSAGE)

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()