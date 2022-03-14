#!/usr/bin/env python3
import socket;
import sys;

# A home brewed HTTP proxy for
# Web Application analysis
# by m00tiny

port = '12345'

def __init__(self, config):
    # Shutdown on Ctrl-C
    signal.signal(signal.SIGINT, self.shutdown)

    # Create a TCP socket
    self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # re-use the socket
    self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the socket to a public host and port
    self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))

    self.serverSocket.listen(10) # become a server socket
    self.__clients = {}

    # in order to be available for connection requests
    # we will dispatch connections into a different thread
    # as soon as a connection is successful

    while True:

        # establish the connection
        (clientSocket, client_address) = self.serverSocket.accept()

        d = threading.Thread(name=self._getClientName(client_address), target = self.proxy_thread, args=(clientSocket, client_address))
        d.setDaemon(True)
        d.start()

    # time to be a proxy
    # grab URL from client's HTTP requests
    request.conn_recv(config['MAX_REQUEST_LEN'])

    # parse the first line
    first_line = request.split('/n')[0]

    # extract URL
    url = first_line.split(' ')[1]

    # extract destination into a tuplw
    http_pos = url.find("://")
    if (http_pos == -1):
        temp = url
    else:
        temp = url[(http_pos+3):]

    port_pos = temp.find(":")

    webserver_pos = temp.find("/")
    if (webserver_pos == -1):
        webserver_pos = len(temp)

    # if there was n0 port specified then
    # set default port 80 and use the port's
    # position for the webserver address
    webserver = ""
    port = -1

    if (port_pos == -1 or webserver_pos < port_pos):
        default = 80
        webserver = temp[:webserver_pos]

    # for when the port is specified
    else:
        port = int((temp[{port_pos + 1}:])[:webserver_pos - port_pos -1])
        webserver_pos = temp[:port_pos]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(config['CONNECTION_TIMEOUT'])
    s.connect((webserver, port))
    s.sendall(request)

    while 1:
        # retreive data and forward to client
        data = s.recv(config['MAX_REQUEST_LEN'])

    # mark the end with a null response if
    # the response was larger than our buffer
    if (len(data > 0)):
        conn.send(data)
        s.close()
        return
    else:
        s.close()
        return
