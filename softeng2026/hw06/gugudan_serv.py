from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gugudan')
def gugudan():
    dan = request.args.get('dan', '2')
    try:
        dan = int(dan)
    except ValueError:
        return render_template('error.html')

    gugudan_list = []
    for i in range(1, 10):
        gugudan_list.append({
            'multiplier': i,
            'result': dan * i
        })
    
    return render_template('gugudan.html', dan=dan, gugudan_list=gugudan_list)


if __name__ == '__main__':
    app.run(debug=True)
