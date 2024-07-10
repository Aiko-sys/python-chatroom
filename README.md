# Python Chatroom
<p>This is a chatroom created in python with libraries "Socket and "Threading". There are two main files: ClientSide.py and ServerSide.py, there are Also modules with a logger class.</p>

### ServerSide.py
<img width="700" src="https://github.com/Aiko-sys/python-chatroom/blob/main/preview/ServerSide.png" alt="...">

<p>This file opens a terminal that shows all the interactions in the chatroom</p>

#### Functions ->
<ul>
  <li>start_server()
    <p>Void function that init the server, The server keeps listening for all clients who want to join in the chat.</p>
  </li>
  <li>
    handle_client()
    <p>Void function that controls all clients, the funcion recives the client name and client socket, after, recive and broadcasts the messages sent by clients</p>
  </li>
  <li>
    broadcast(ClientSocket, clientAdress)
    <p>Void function that broadcasts all messages sent by clients except its owns</p>
  </li>
</ul>

#### Keys(class) ->
<p>these keys are used for Control the server. (modules/classes.py)</p>
<code>serverSeeChatKey(bool) : control Chat in the ServerSide. If it's active, the terminal will shows messages from chat<br>
logKey(bool) : control if the application will log the interactions in the chat room</code>

### ClientSide.py

<img width="700" src="https://github.com/Aiko-sys/python-chatroom/blob/main/preview/ClientSideWelcome.png" alt="...">
<img width="700" src="https://github.com/Aiko-sys/python-chatroom/blob/main/preview/ClientSideChat.png" alt="...">

<p>This file opens the application that clients will interact with chat</p>

#### Functions ->
<ul>
  <li>send_client_message()
  </li>
  <li>
    recive_server_message()
  
  </li>
</ul>
