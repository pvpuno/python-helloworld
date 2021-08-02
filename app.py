from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def hello2():
    return{
        "user":"admin",
        "result":"OK - Healthty"
    }

@app.route("/metrics")
def hello3():
    return {
        "user":"admin",
        "data":"{UserCount: 140, UserCountActive: 23}"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
