from flask import Flask

app = Flask(__name__)

@app.route('/haha')
def homepage():
    return "Hi there, how ya doin?"


if __name__ == "__main__":
    app.run()