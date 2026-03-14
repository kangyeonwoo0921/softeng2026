from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/gugudan")
def gugudan():
    return"""
구구단

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
"""

if __name__ == "__main__":
    app.run(debug=True)

