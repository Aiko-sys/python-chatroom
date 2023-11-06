import socket, threading, random

class ClientCommands:
    disconnectCommand = "/disconnect"


class keys:
    serverSeeChatKey = True


class colors:
    default = "\033[m"
    red = "\033[31m"
    green = "\033[32m"
    yellow ="\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    grey = "\033[37m"
    colorslist = [
    red, 
    green,
    yellow,
    blue,
    magenta,
    cyan,
    ]


class TextDetails:
    systemMessage = {
    "plus":f"{colors.red}[{colors.yellow}+{colors.red}]{colors.default}",
    "System":f"{colors.red}[{colors.yellow}SYSTEM{colors.red}]{colors.default}"}


def start_server():
    sock.listen()
    print(f"[LISTENING] Server is listening on {ServerHost}")

    while True:
        ClientSocket, clientAdress  = sock.accept()
        thread = threading.Thread(target=handle_client, args=(ClientSocket, clientAdress))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1} ')


def broadcast(message, senderClient):
    try:
        for client in clients:
            if (client!=senderClient):
                client.send(message.encode(formatMessage))
    except:
        print("[ERROR] broadcast fail")


def handle_client(ClientSocket, clientAdress):
    print(f"[NEW CONNECTION] {clientAdress[0]} connected.")
    clientConnected = True
    clients.append(ClientSocket)

    # recive client name
    try:
        ClientNickName = ClientSocket.recv(header).decode(formatMessage)
        if ClientNickName:
                try:
                    ClientNickName = int(ClientNickName)
                except:
                    print("[ERRO] can't recive username")
                else:   
                    ClientNickName = ClientSocket.recv(ClientNickName).decode(formatMessage)
                    
    except ConnectionError:
        print(f"[ERROR] {clientAdress[0]} left before set nickname")
        clients.remove(ClientSocket)
        clientConnected = False
        
    #recive client messages  
    try:
        while clientConnected:
            messageLength = ClientSocket.recv(header).decode(formatMessage)
            if messageLength:
                try:
                    messageLength = int(messageLength)
                except:
                    print('[ERRO] cant recive messages')
                else:   
                    message = ClientSocket.recv(messageLength).decode(formatMessage)
                    
                    if (message == ClientCommands.disconnectCommand):
                        print(f"[DISCONNECTED] -- {ClientNickName}")
                        clients.remove(ClientSocket)
                        broadcast(f"{TextDetails.systemMessage['plus']} <{ClientNickName}> disconnected", ClientSocket)
                        clientConnected = False
                        
                    else:
                        if keys.serverSeeChatKey:
                            print(f'<{ClientNickName}> {message}')
                        broadcast(f'<{random.choice(colors.colorslist)}{ClientNickName}{colors.default}> {message}', ClientSocket)

    except ConnectionError:
        print(f"[DISCONNECTED] -- {ClientNickName}")
        clients.remove(ClientSocket)
        broadcast(f"{TextDetails.systemMessage['plus']} <{ClientNickName}> disconnected", ClientSocket)
        

    except:
        print(f"[WTF] what happenned to {ClientNickName}?")    

    ClientSocket.close()


# main code
clients = []
header = 64 
formatMessage = "utf-8"

ServerHost = socket.gethostbyname(socket.gethostname())
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerAddress = (ServerHost, 5050)
sock.bind(ServerAddress)

print("[START] starting the server v1.0.0")
start_server()