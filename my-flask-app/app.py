from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps! It was a successful deployment using render."

if __name__ == '__main__':
    app.run()