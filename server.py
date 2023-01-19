import socket
import threading

ip_addr , port = '192.168.1.68' , 9999
server = socket.socket()
server.bind((ip_addr , port))
server.listen(2)

client_names = []


def recv_message(client_info , client_address):
    while True:
        if len(client_names) == 2:
            recv_data  = client_info.recv(1024).decode("utf-8")
            print(f"{client_address} send message {recv_data}")
            if client_info == client_names[0]:
                client_names[1].send(recv_data.encode('utf-8'))
                # client_names[1].send(str(client_address[1]).encode('utf-8'))
            elif client_info == client_names[1]:
                client_names[0].send(recv_data.encode('utf-8'))
                # client_names[0].send(str(client_address[1]).encode('utf-8'))
        else:
            pass





def conn():
    global client_names
    while True:
        client_info , client_address = server.accept()
        print(f"client address {client_address}")
        client_names.append(client_info)
        
        recv_msg_thread = threading.Thread(target=recv_message , args=(client_info , client_address))
        # # recv_msg_thread.daemon = True
        recv_msg_thread.start()

conn()
