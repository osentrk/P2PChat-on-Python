# P2PChat-on-Python
BAU CMP2204 Term Project

This project created for CMP2204 - Introduction to Computer Network

Project related to the Peer-to-peer chat application with UDP and TCP ports.
This application was developed in MacOS.<br>

Online list will be storage in json file, the path of the file is your /home/USER/onlineList.json<br>
Chat log will be storage in text file, the path of the file is your /home/USER/chatUsername_chatIP.txt

Please run the applications in the order given below.

1-) **Service_Listener.py** Always listen broadcast IP and shows who is online Just run, it won't ask any question.<br>
2-) **Service_Announcer.py** You must enter own username and every 60 seconds program sends user data to local broadcast 
IP address.<br>
3-) **Chat_Listener.py** Program displays and logging messages from any online user. Just run, it won't ask any question.<br> 
4-) **Chat_Client.py** You must enter username which in the list in order to start conversation. After this, you can 
chat with user. If you want to leave the conversation, type 'exit'. Online list reloading automatically but if you want 
to refresh, type reload.<br>


Now, you can focus on Chat_Client.py and you can chat any online user.
