import socket, threading, random

# APPLICATION MODULES AND HELPERS
from modules.classes import *
from modules.helpers import *
from modules.exceptions import *

# ARRAYS
clients = []
clientNicknames = []

# CONSTS
HEADER = 64 
FORMATMESSAGE = "utf-8"


def start_server():

    sock.listen()
    print(f"[LISTENING] Server is listening on {host}")

    while True:
        ClientSocket, clientAdress  = sock.accept()
        thread = threading.Thread(target=handle_client, args=(ClientSocket, clientAdress))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] : {threading.active_count() - 1} ')


def broadcast(message, senderClient):
    try:
        for client in clients:
            if (client!=senderClient):
                client.send(message.encode(FORMATMESSAGE))
    except:
        print("[ERROR] broadcast fail")


def handle_client(ClientSocket, clientAdress):
    clientConnected = True
    clients.append(ClientSocket)

    # RECIVE CLIENT NAME
    ClientNickName = ClientSocket.recv(HEADER).decode(FORMATMESSAGE)
    if ClientNickName:
        try:
            ClientNickName = int(ClientNickName)
        except:
            print("[ERROR] can't recive username")
        else:   
            ClientNickName = ClientSocket.recv(ClientNickName).decode(FORMATMESSAGE)

            # Verifing if Client nickname repeating int client nicknames list
            count = 2
            NewClientNickName = ClientNickName
            while True:
                
                if NewClientNickName in clientNicknames:
                    NewClientNickName = ClientNickName + f"({count})"
                    count += 1
                else:
                    ClientNickName = NewClientNickName
                    break
                    
            clientNicknames.append(ClientNickName)

    print(f"[NEW CONNECTION] -- <{ClientNickName}> from ip: {clientAdress[0]} connected.")
    broadcast(f"{TextDetails.systemMessage['plus']} <{ClientNickName}> connected", ClientSocket)
    
    # RECIVE CLIENT MESSAGES
    try:
        while clientConnected:
            messageLength = ClientSocket.recv(HEADER).decode(FORMATMESSAGE)
            if messageLength:
                try:
                    messageLength = int(messageLength)
                except:
                    print('[ERROR] cant recive messages')
                else:   
                    message = ClientSocket.recv(messageLength).decode(FORMATMESSAGE)
                    

                    if (message == ClientCommands.disconnectCommand):
                        print(f"[DISCONNECTED] -- <{ClientNickName}> from ip: {clientAdress[0]}")
                        clients.remove(ClientSocket)
                        clientNicknames.remove(ClientNickName)
                        broadcast(f"{TextDetails.systemMessage['plus']} <{ClientNickName}> disconnected", ClientSocket)
                        clientConnected = False

                    elif(ClientCommands.renameCommand in message.strip()):
                        try:
                            oldClientNickName = ClientNickName
                            ClientNickName = message[message.index(' '):].strip().replace(" ", "-")

                            if ClientNickName in clientNicknames:
                                raise AlreadyExistingNickName()
                            else:
                                clientNicknames[clientNicknames.index(oldClientNickName)] = ClientNickName
                        except AlreadyExistingNickName:
                            ClientSocket.send(f"{TextDetails.systemMessage['System']}: Nickname already exists in the chat, choose another one.".encode(FORMATMESSAGE))

                        except:
                            ClientSocket.send(f"{TextDetails.systemMessage['System']}: Your nickname cannot be changed".encode(FORMATMESSAGE))

                        else:
                            print(f'[USER] -- {oldClientNickName} changed their name to {ClientNickName}')
                            ClientSocket.send(f"{TextDetails.systemMessage['System']}: Your nickname has been changed".encode(FORMATMESSAGE))

                            broadcast(f'{TextDetails.systemMessage["plus"]} <{random.choice(colors.colorslist)}{oldClientNickName}{colors.default}> changed their name to <{random.choice(colors.colorslist)}{ClientNickName}{colors.default}> ', ClientSocket)
                    else:
                        if keys.serverSeeChatKey:
                            print(f'<{ClientNickName}> {message}')
                        broadcast(f'<{random.choice(colors.colorslist)}{ClientNickName}{colors.default}> {message}', ClientSocket)

    except ConnectionError:
        print(f"[DISCONNECTED] -- <{ClientNickName}> from ip: {clientAdress[0]}")
        clients.remove(ClientSocket)
        clientNicknames.remove(ClientNickName)
        broadcast(f"{TextDetails.systemMessage['plus']} <{ClientNickName}> disconnected", ClientSocket)
        

    except:
        print(f"[DISCONNECTED] -- <{ClientNickName}> from ip: {clientAdress[0]}")
        clients.remove(ClientSocket)
        clientNicknames.remove(ClientNickName)
        print(f"[WTF] what happenned to {ClientNickName}?")   
        broadcast(f"{TextDetails.systemMessage['plus']} <{ClientNickName}> disconnected", ClientSocket) 

    ClientSocket.close()


# MAIN CODE

# CREATING SOCKET
host = socket.gethostbyname(socket.gethostname())
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerAddress = (host, 5050)
sock.bind(ServerAddress)

# STARTING THE SERVER
print("[START] starting the server v1.0.2")
start_server()
