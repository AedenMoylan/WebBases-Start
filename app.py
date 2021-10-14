from flask import Flask

import datetime



app = Flask(__name__)


@app.route("/")       #register the / url with the web server
def index():  
    return datetime.datetime.now().ctime()    # the http response

@app.route("/hello")
def hello():
    return "was poppin my g"
    
if __name__== "__main__":
    app.run()