#!/usr/bin/python

import sys
import webapp
import suma
import hola
import aleat
import random


class Aleat(webapp.app):

    def parse(self, request, rest):
        print request
        try:
            self.paquete = request.split()[1]
        except IndexError:
            return 'IndexError'

    # Defines new process answer
    def process(self, request):
        # Creates a random number between 1 and 10000
        URLaleatoria = str(random.randint(1, 10000))
        return ("200 OK", "<html><body><h1>" +
                "<a href=' " + URLaleatoria + " ''>" + URLaleatoria + "</a>")

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
