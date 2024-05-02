import socket, threading, os, sys


class ClientCommands:
    commandList = ["/disconnect", '/rename', '/clear', '/help']
    disconnectCommand = "/disconnect"
    renameCommand = '/rename'
    clearCommand = '/clear'
    helpCommand = '/help'

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
    "plus":f"{colors.magenta}[{colors.yellow}+{colors.magenta}]{colors.default}",
    "System":f"{colors.magenta}[{colors.yellow}SYSTEM{colors.magenta}]{colors.default}"}


    OldasciiArt = f"""
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
    asciiArt = f"""
    {colors.magenta}
 ██████╗██╗  ██╗ █████╗ ████████╗    ██████╗  ██████╗  ██████╗ ███╗   ███╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
██║     ███████║███████║   ██║       ██████╔╝██║   ██║██║   ██║██╔████╔██║
██║     ██╔══██║██╔══██║   ██║       ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
╚██████╗██║  ██║██║  ██║   ██║       ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
                                                                     
    {colors.yellow}chat: {colors.default}v1.1.0     | {colors.yellow}Server:{colors.default} v1.1.0
    {colors.yellow}Coded by: {colors.default}<Aiko> | {colors.yellow}My Github:{colors.default} @Aiko-sys
    """

    welcome_message = f"""
    {colors.magenta}
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
{colors.default}                                                              
    """

    help_command_string = f"""
                {colors.yellow}All commands:
{colors.magenta}=================================================
                
{colors.yellow}- /disconnect : {colors.default}disconnect from the chat and leave 
the terminal

{colors.yellow}- /rename <name> : {colors.default}change your username

{colors.yellow}- /clear : {colors.default}clean the terminal

{colors.magenta}=================================================
{colors.default}
    """

class keys:
    serverSeeChatKey = True
    logKey = False
