import cherrypy
import random
import string

# basic application - just a static page
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello MotherFucker!'
    
    # if you add /generate at the end of the url each time you get a new random 8char string
    @cherrypy.expose
    def generate(self, length = 10):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == "__main__":
    cherrypy.quickstart(HelloWorld())