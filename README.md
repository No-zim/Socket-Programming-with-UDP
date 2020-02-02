# Socket_Programming_with_UDP

UDP is unreliable data transfer. Used for loss tolerant data transfer(audio, video, games and so on)
Tried it on text messages(I know TCP is the best for such things, but...)

run serverUDP.py then clientUDP.py

This program runs on your local server (aka: local or 127.0.0.1)

The serverUDP.py requires a port number, and you can enter any integer for port number (or just press enter for default value of 9999), You'll need this # in your clientUDP.py program
        
        Server program runs until you stop it and:
        receives two strings:
        ->First commands: upper, lower, reverse
        ->Second message: string
        Modifies the message according to your command and returns it
        
  
  
ClientUDP.py
         Needs a host address(you can enter localhost or 127.0.0.1 which mean your own computer) or just press enter for default
         Needs a port #(same port # you entered for serverUDP.py[if you entered nothing, enter 9999])
         
         This program runs until you enter 'quit'
         
         First Enter your message: a sentense
         Second your command: upper, lower, reverse
         prints the received back message from the serverUDP.py
         
         
There are comments explaining what the code does in the serverUDP.py and clientUDP.py 
         
         
     
      
