import cherrypy
import os
class MyApp:
    pass

if __name__ == '__main__':
    conf = {
         '/': {
             
             'tools.staticdir.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd()),
             'tools.staticdir.dir': 'D:/New Learnings/GEC_VR_tour/GEC_virtual_tour',
             
         }
             }
cherrypy.config.update({'server.socket_port': 8085})
cherrypy.quickstart(MyApp(),"/",conf)
