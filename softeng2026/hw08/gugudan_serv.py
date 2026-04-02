from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog_list')
def blog_list():
    return render_template('blog_list.html')

@app.route('/about')
def about():
    return render_template('about_me.html')    
        
if __name__ == '__main__':
    app.run(debug=True)
