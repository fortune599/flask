from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello_world():
    return "hello"

@app.route("/memes")

def goodbye_world():
    return "goodbye"

@app.route("/thanks")

def thanks_world():
    return "thanks"

if __name__ == "__main__":
    app.run()
