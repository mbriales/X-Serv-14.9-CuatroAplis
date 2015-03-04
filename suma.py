#!/usr/bin/python

import sys
import socket
import webapp
import suma
import hola
import aleat


class Suma(webapp.app):

    def process(self, parsedRequest):
        # total = self.lista

        self.operar = parsedRequest
        sumando = int(self.operar[1]) + int(self.operar[2])

        return ("200 OK", "<html><body><h1>" +
                str(sumando))

try:
    if __name__ == "__main__":
        SumaApp = suma.Suma()
        HolaApp = hola.Hola()
        AdiosApp = hola.Adios()
        AleatApp = aleat.Aleat()
        testWebApp = webapp.webApp("localhost", 1234, {'/suma': SumaApp,
                                                       '/hola': HolaApp,
                                                       '/adios': AdiosApp,
                                                       '/aleat': AleatApp})

except TypeError:
    sys.exit()
