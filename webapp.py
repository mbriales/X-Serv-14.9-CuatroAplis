#!/usr/bin/python

import socket
import sys


class app:

    def parse(self, request, rest):
        print request

        try:
            paquete = request.split()[1][1:]
            lista = paquete.split('/')
            if len(lista) != 3 or lista[0] not in ["suma", "resta"]:
                return None
            return lista

        except ValueError:
            return None
        return paquete

    def keys(self):
        return None

        # try:
        #     if len(self.lista) == 3:
        #         suma_total = parse.lista[2] + parse.lista[3]
        #         return suma_total
        # except ValueError:
        #     print 'entro aqui2'
        #     return None

    def process(self, parsedRequest):
        # total = self.lista
        operar = parsedRequest

        print 'Test 6'
        return ("200 OK", "<html><body><h1>" +
                "Dumb application just saying 'It works!'" +
                "</h1><p>App id: " + 'NO HAY NADA' + "<p></body></html")


class webApp:
    def select(self, request):
        """Selects the application (in the app hierarchy) to run.

        Having into account the prefix of the resource obtained
        in the request, return the class in the app hierarchy to be
        invoked. If prefix is not found, return app class
        """

        resource = request.split(' ', 2)[1]
        for prefix in self.apps.keys():
            if resource.startswith(prefix):
                print "Running app for prefix: " + prefix + \
                    ", rest of resource: " + resource[len(prefix):] + "."
                return (self.apps[prefix], resource[len(prefix):])
        print "Running default app"
        return (self.myApp, resource)

    def __init__(self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps
        self.myApp = app()

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and processod meths (in a loop)
        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to parse and process):'
            request = recvSocket.recv(2048)
            print request
            (theApp, rest) = self.select(request)
            parsedRequest = theApp.parse(request, rest)
            # For operate in other classes
            (returnCode, htmlAnswer) = theApp.process(parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1 " +
                            returnCode +
                            " \r\n\r\n" +
                            htmlAnswer +
                            "\r\n")
            recvSocket.close()
