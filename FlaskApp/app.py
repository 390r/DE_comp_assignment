import json
import re
from math import pow, exp

import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

funct = '-x + (y * (2*x + 1)) / (x)'
solved_funct = 'C * pow(exp(1), 2 * x) * x + x / 2'


# funct = 'pow(x, 2) - 2*y'
# solved_funct = '3 / 4 * pow(exp(1), -2 * x) + 1 / 2 * pow(x, 2) - 1 / 2 * x + C'


def get_function_value(funct, x, const=None, y=None):
    eq = funct
    eq = re.sub(r"\b{}\b".format('x'), str(x), eq)
    try:
        eq = re.sub(r"\b{}\b".format('C'), str(const), eq)
    except:
        print('No const found')
    try:
        eq = re.sub(r"\b{}\b".format('y'), str(y), eq)
    except:
        print('No Y parameter found')
    return eval(eq)


def euler_method(funct, x, y, _to, step):
    res = []
    while x < _to:
        res.append([x, y])
        f = get_function_value(funct, x, y=y)
        hf = step * f
        x += step
        y += hf
    return res


def improved_euler_method(funct, x, y, _to, step):
    res = []
    while x < _to:
        res.append([x, y])
        x_t = x + step / 2
        f_t = get_function_value(funct, x=x, y=y)
        y_t = y + step * f_t / 2
        f_res = get_function_value(funct, x=x_t, y=y_t)
        d_y = f_res * step
        y = y + d_y
        x = x + step
    return res


def runge_kutta(funct, x, y, _to, step):
    res = []
    while x < _to:
        res.append([x, y])
        k1 = get_function_value(funct, x=x, y=y)
        k2 = get_function_value(funct, x=x + step / 2, y=y + step * k1 / 2)
        k3 = get_function_value(funct, x=x + step / 2, y=y + step * k2 / 2)
        k4 = get_function_value(funct, x=x + step, y=y + step * k3)
        d_y = step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += step
        y += d_y
    return res


def find_const(x0, y0):
    return (y0 - (x0 / 2)) / (pow(exp(1), 2 * x0) * x0)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/getChart")
def get_chart():
    global solved_funct, funct

    _from = float(request.args.get('from'))
    _to = float(request.args.get('to'))
    _step = float(request.args.get('step'))
    print('Step', _step)
    x0 = float(request.args.get('x0'))
    y0 = float(request.args.get('y0'))
    funct = request.args.get('init_f')
    solved_funct = request.args.get('solved_f')

    print(funct, solved_funct)

    const = find_const(x0, y0)
    print(improved_euler_method(funct, x0, y0, _to, _step))

    exact_res = [[x, get_function_value(solved_funct, x, const)] for x in np.arange(_from, _to + _step, _step)]
    euler_res = euler_method(funct, x0, y0, _to, _step)
    impr_euler_res = improved_euler_method(funct, x0, y0, _to, _step)
    runge_res = runge_kutta(funct, x0, y0, _to, _step)

    euler_err = [[euler_res[x][0], exact_res[x][1] - euler_res[x][1]] for x in range(len(euler_res))]
    impr_euler_err = [[impr_euler_res[x][0], exact_res[x][1] - impr_euler_res[x][1]] for x in
                      range(len(impr_euler_res))]
    runge_err = [[runge_res[x][0], exact_res[x][1] - runge_res[x][1]] for x in range(len(runge_res))]

    return json.dumps({"Exact": exact_res,
                       "Euler": euler_res,
                       "Improved_Euler": impr_euler_res,
                       "Runge_Kutta": runge_res,
                       "error_Runge_Kutta": runge_err,
                       "error_Euler": euler_err,
                       "error_Impr_Euler": impr_euler_err
                       })


if __name__ == "__main__":
    app.run()
