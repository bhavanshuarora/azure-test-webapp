  
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bhavanshu Arora webApp test!  <b>hello !!</b>  <img src='https://lwmystorage.blob.core.windows.net/myblob/IMG_20200803_201943001.jpg'  width='150' height='200' />"
