import socket, threading, os


class ClientCommands:
    disconnectCommand = "/disconnect"

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


class textDetails:

    systemMessage = {
    "plus":f"{colors.red}[{colors.yellow}+{colors.red}]{colors.default}",
    "System":f"{colors.red}[{colors.yellow}SYSTEM{colors.red}]{colors.default}"}


    asciiArt = f"""
                     {colors.red} 
   (       )           ) )\ )                   
   )\   ( /(     )  ( /((()/(              )    
 (((_)  )\()) ( /(  )\())/(_)) (    (     (     
 )\___ ((_)\  )(_))(_)){colors.yellow}/(_))   )\   )\    )\  ' 
((/ __|| |(_)((_)_ | |_ | _ \ ((_) ((_) _((_))  
 | (__ | ' \ / _` ||  _||   // _ \/ _ \| '  \() 
  \___||_||_|\__,_| \__||_|_\\___/\___/|_|_|_|  
                                               {colors.default}
    {colors.yellow}chat: {colors.default}v1.0.1      | {colors.yellow}Server:{colors.default} v1.0.1
    {colors.yellow}Coded by: {colors.default}<ricky> | {colors.yellow}My Github:{colors.default} @rickyy-sys
    {colors.default}
"""


def send_client_message():

    # send nickname
    while True:
        clientName = nickname.encode(formatMessage)
        clientNameLength = len(clientName)
        SendClientNameLength = str(clientNameLength).encode(formatMessage)
        SendClientNameLength += b' ' * (header - len(SendClientNameLength))
        ClientSock.send(SendClientNameLength)
        ClientSock.send(clientName)

        while True:
            message = input()
            while message in ["", " "] or message.isspace():
                message = input()

            # send messages
            clientMessage = message.encode(formatMessage)
            clientMessageLength = len(clientMessage)
            SendClientMessageLength = str(clientMessageLength).encode(formatMessage)
            SendClientMessageLength += b' ' * (header - len(SendClientMessageLength))
            ClientSock.send(SendClientMessageLength)
            ClientSock.send(clientMessage)

            if (message == ClientCommands.disconnectCommand):
                os.system('taskkill /F /T /PID %i' % os.getpid())
            


def recive_server_message():
    while True:                                                
        try:
            message = ClientSock.recv(header).decode(formatMessage)
            print(message)
        except:                                                 
            print("[ERROR] can't recive messages")
            ClientSock.close()
            break

header = 64 
formatMessage = "utf-8"
os.system("cls")
ServerAdressToConnect = ('127.0.0.1', 5050)
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print(f"{colors.red}==========={colors.yellow} Checking {colors.red}==========={colors.default}")

nickname = str(input(textDetails.systemMessage["System"]+" define your nickname: ")).strip().replace(" ", "-")
while (nickname in [" ", ''] or nickname.isspace() or len(nickname) > 15):
    nickname = input(textDetails.systemMessage["System"]+" invalid Nickname (only 1 to 15 characters)! try again: ")


input(textDetails.systemMessage["System"]+" press enter to network connect...")

try: 
    ClientSock.connect(ServerAdressToConnect)
except:
    print("[ERROR] can't connect")
else:

    os.system("cls")
    print(textDetails.asciiArt)
    print(f"{colors.red}=-=-=-=-=-=-= {colors.yellow}Welcome! {colors.red}=-=-=-=-=-=-={colors.default}\n"+textDetails.systemMessage["plus"]+" Connection sussefully! send a message:\n")


    receive_thread = threading.Thread(target=recive_server_message)               
    receive_thread.start()
    write_thread = threading.Thread(target=send_client_message)                    
    write_thread.start()