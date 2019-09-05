from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Assertible!"

@app.route("/hagemaru")
def hagemaru():
    return "Hello!"


if __name__ == "__main__":
    app.run()
