import socket, threading, os, sys


class ClientCommands:
    commandList = ["/disconnect", '/rename']
    disconnectCommand = "/disconnect"
    renameCommand = '/rename'

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

class Cursors:
    
    def move_cursor_up(lines=5):
        sys.stdout.write(f"\033[{lines}A")

    def move_cursor_down(lines=5):
        sys.stdout.write(f"\033[{lines}B")

    def clear_previous_line():
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K") 
        print('', end='', flush=True)

class TextDetails:

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
    {colors.yellow}chat: {colors.default}v1.0.2      | {colors.yellow}Server:{colors.default} v1.0.2
    {colors.yellow}Coded by: {colors.default}<Aiko> | {colors.yellow}My Github:{colors.default} @Aiko-sys
    {colors.default}
"""
class keys:
    serverSeeChatKey = True
