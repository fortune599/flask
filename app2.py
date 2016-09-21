from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route("/memes")
@app.route("/thanks")

def hello_world():
    return "hello"

if __name__ == "__main__":
    app.run()
