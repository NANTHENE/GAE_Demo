from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><head><title>Greeting</title></head><body><h1 style="color:blue;font-style:calibri">Google App Engine Demo</h1><p>Hello, World!</p></body></html>'

if __name__ == "__main__":
   app.run()
