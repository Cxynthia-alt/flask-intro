# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/math/<method_name>')
def calculate(method_name):
    method_by_method_name = {
        'add': (add, 'Sum'), 'sub': (sub, 'Subtract'), 'mult': (mult, 'Multiply'), 'div': (div, 'Divide')}
    num1 = request.args.get('a', type=int)
    num2 = request.args.get('b', type=int)
    method, msg = method_by_method_name[method_name]
    return f"{msg} :{num1} and {num2} equals {method(num1, num2)}"
