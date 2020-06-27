from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/env")
def env():
    res="<table>"
    for var in os.environ:
        res+="<tr><td>"+var+"</td>"+"<td>"+os.environ[var]+"</td></tr>"
    res+="</table>"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0")