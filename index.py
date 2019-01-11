from flask import Flask, request
import os
import sys


app = Flask(__name__)

def addNumbers(num1, num2):
    return int(num1) + int(num2)

@app.route('/add')
def hello_world():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    return str(addNumbers(num1, num2))

if __name__ == '__main__':
    app.run(debug=True)
