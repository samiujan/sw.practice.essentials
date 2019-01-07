from flask import Flask, request
app = Flask(__name__)


def add_numbers(num1, num2):
    return num1 + num2

@app.route('/add')
def hello_world():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    return add_numbers(num1, num2)
