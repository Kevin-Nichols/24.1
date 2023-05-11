# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def sum():
    """Returns sum of 'a' and 'b'"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return str(add(a, b))

@app.route('/sub')
def difference():
    """Returns the difference of 'a' and 'b'"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return str(sub(a, b))

@app.route('/mult')
def product():
    """Returns the product of 'a' and 'b'"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return str(mult(a, b))

@app.route('/div')
def quotient():
    """Returns the quotient of 'a' and 'b'"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return str(div(a, b))

### Further Study
math_rules = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<rule>')
def calculate(rule):
    """Retures 'a' and 'b' using which ever rule from math_rules"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return str(math_rules[rule](a, b))
    