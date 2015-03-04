#!/usr/bin/python

import sys
import webapp
import suma
import hola
import aleat


class Hola(webapp.app):

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        # total = self.lista

        return ("200 OK", "<html><body><h1>" +
                "Hola")


class Adios(webapp.app):

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        # total = self.lista

        return ("200 OK", "<html><body><h1>" +
                "Adios")

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
