import socket, threading, os, sys

# APPLICATION MODULES AND HELPERS
from modules.classes import *
from modules.helpers import *

# CONSTS

HEADER = 64 
FORMATMESSAGE = "utf-8"


def send_client_message():

    # SEND NICKNAME
    while True:
        clientName = nickname.encode(FORMATMESSAGE)
        clientNameLength = len(clientName)
        SendClientNameLength = str(clientNameLength).encode(FORMATMESSAGE)
        SendClientNameLength += b' ' * (HEADER - len(SendClientNameLength))
        ClientSock.send(SendClientNameLength)
        ClientSock.send(clientName)

        while True:

            # GET AND VERIFY MESSAGE
            while True:
                try:
                    message = input("")
                except KeyboardInterrupt:
                    kill()

                if message in ["", " "] or message.isspace():
                    continue
                elif len(message) > 160:
                    print(f'{TextDetails.systemMessage["System"]}: Your message can only be 160 characters or less')
                    continue
                elif message.startswith('/'):
                    command = message.split(' ')[0]
                    if command not in ClientCommands.commandList:
                        print(f'{TextDetails.systemMessage["System"]}: Command syntax is wrong')
                        continue
                    else:
                        break
                else:
                    break
                    

            # SEND MESSAGES
            clientMessage = message.encode(FORMATMESSAGE)
            clientMessageLength = len(clientMessage)
            SendClientMessageLength = str(clientMessageLength).encode(FORMATMESSAGE)
            SendClientMessageLength += b' ' * (HEADER - len(SendClientMessageLength))
            ClientSock.send(SendClientMessageLength)
            ClientSock.send(clientMessage)

            if (clientMessage == ClientCommands.disconnectCommand):
                kill()
            


def recive_server_message():

    while True:                                                
        try:
            message = ClientSock.recv(HEADER).decode(FORMATMESSAGE)
            print(message)
            
        except:                                                 
            print(f"{TextDetails.systemMessage['System']}: can't recive messages. Probably the server was turned off :< press enter to quit")
            ClientSock.close()
            input()
            os.system('taskkill /F /T /PID %i' % os.getpid())
            break
        

# MAIN CODE >>>

print(f"{colors.red}==========={colors.yellow} Checking {colors.red}==========={colors.default}")
os.system("cls")

# GETTING USER AND SERVER INFO
nickname = str(input(TextDetails.systemMessage["System"]+" define your nickname: ")).strip().replace(" ", "-")
while (nickname in [" ", ''] or nickname.isspace() or len(nickname) > 15):
    nickname = input(TextDetails.systemMessage["System"]+" invalid Nickname (only 1 to 15 characters)! try again: ").strip().replace(" ", "-")

serverIP = str(input(TextDetails.systemMessage["System"]+" server IP: ")).strip().replace(" ", "-")

# CREATING SOCKET
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# CONNECTING 

ServerAdressToConnect = (serverIP, 5050)

while True:
    try: 
        ClientSock.connect(ServerAdressToConnect)
        input(TextDetails.systemMessage["System"]+" press enter to network connect...")
    except KeyboardInterrupt:
        ClientSock.close()
        kill()
    except:
        serverIP = str(input(TextDetails.systemMessage["System"]+" The Server isn't listening on that IP, try again: ")).strip().replace(" ", "-")
        ServerAdressToConnect = (serverIP, 5050)
    else:
        break



# STARTING CHAT
os.system("cls")
print(TextDetails.asciiArt)
print(f"{colors.red}=-=-=-=-=-=-={colors.yellow} Welcome! {colors.red}=-=-=-=-=-=-={colors.default}\n"+TextDetails.systemMessage["plus"]+" Connection sussefully! send a message:\n")


receive_thread = threading.Thread(target=recive_server_message)               
receive_thread.start()
write_thread = threading.Thread(target=send_client_message)                    
write_thread.start()