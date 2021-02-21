from flask import render_template
from flask import Flask, request

app = Flask(__name__)


@app.route('/')           # first view website
def my_echart():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def main():                         
    #const = Constans()
    req = request.form.to_dict()
    print('Result Req', req)
    #res = main_function(p, now)
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
    






