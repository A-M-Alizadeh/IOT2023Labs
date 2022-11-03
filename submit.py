import random
import string
import cherrypy
import json
import os.path


class Generator(object):

# returning a form with a button
# in the action part of the form you can call the function you need

    @cherrypy.expose 
    def index(self):
        return """
        <html>
        <head></head>
        <body>
            <form method="get" action="generate">
                <input type="text" value="10" name="length" />
                <button type="submit">Let it Rain</button>
            </form>
        </body>
        </html>
        """

    # when push the button this method is called and you are redirected to the path /generate
    @cherrypy.expose
    def generate(self, length = 10):
        return ''.join(random.sample(string.hexdigits, int(length)))

    # this is how we can return a json response
    @cherrypy.expose
    def json(self):
        res = "Pong"
        return json.dumps({"Ping":res})


if __name__ == "__main__":
    configFile = os.path.join(os.path.dirname(__file__),'server.conf')
    cherrypy.quickstart(Generator(), config =  configFile)