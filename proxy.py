from socket import *
import sys
import string

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server]')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((sys.argv[1],8888))
tcpSerSock.listen(1)

while 1:

    # Start receiving data from the client
    print('Ready to serve...')
    
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    
    message = tcpCliSock.recv(1024).decode()
    print("message: " + message)
    
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print("filename: " + filename)
    
    fileExist = "false"
    filetouse = "/" + filename
    print("filetouse: " + filetouse)
    
    try:
        # Check whether the file exist in the cache
        cacheFile = open(filetouse[1:], "rb")
        byte = cacheFile.read()
        
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send(byte)
        tcpCliSock.close()
        cacheFile.close()
        
        print('Read from cache')
    
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = message.split()[1].partition("/")[2].partition("/")[0]
            dest =  message.split()[1].partition("/")[2].partition("/")[2]
            print("hostn" + hostn)
            try:
                # Connect to the socket to port 80
                c.connect((hostn, 80))
                print('Socket connected to port 80 of the host')

                messagenew = message.split()[0] + ' /' + dest + ' ' + message.split()[2]+'\r\n'
                print("messagenew: "+ messagenew)

                messagenew += message.split('\n')[1].split()[0] + ' ' + hostn + '\r\n'
                print("messagenew: "+ messagenew)

                othermessage = message.split('\r\n')[2:]

                for i in othermessage:
                    messagenew += i + '\r\n'
                print("messagenew: "+ messagenew)

                c.send(messagenew.encode())
                rq = c.recv(300000000)

                tmpFile = open("./" + filename,"wb")
                tmpFile.write(rq)
                tmpFile.close()

                tcpCliSock.send(rq)
                tcpCliSock.close()
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            print("File not Found")
    
    # Close the client and the server sockets
    tcpCliSock.close()