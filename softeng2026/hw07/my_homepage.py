from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_me')
def about():
    return render_template('about_me.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

if __name__ == '__main__':
    app.run(debug=True)
