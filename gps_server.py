#!/usr/bin/python2

from flask import Flask
import json
from gps import *
import threading

gpsd = None

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        global gpsd #bring it in scope
        gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.current_value = None
        self.running = True #setting the thread running to true
 
    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

app = Flask(__name__)

@app.route("/")
def hello():
    global gpsd
    data = {}
    data['latitude'] = gpsd.fix.latitude
    data['longitude'] = gpsd.fix.longitude
    return json.dumps(data)
    
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    gpsp = GpsPoller() # create the thread
    gpsp.start()
    app.run()
