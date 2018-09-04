from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    age = request.args.get("age")
    return "Your age is " + age


if __name__ == '__main__':
    app.run(debug=True)
