from flask import Flask, request, render_template
import pandas as pd
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog_list')
def blog_list():
    # posts = [
    #     {
    #         'title': '제목1',
    #         'content': '첫 번째 포스트의 내용입니다.'
    #     },
    #     {
    #         'title': '제목2',
    #         'content': '두 번째 포스트의 내용입니다.'
    #     },
    #     {
    #         'title': '제목3',
    #         'content': '세 번째 포스트의 내용입니다.'
    #     }
    # ]
    df = pd.read_csv('lec09/hw08/blog_data.csv', encoding='utf-8')
    print(df)
    posts = df.to_dict(orient='records')
    return render_template('blog_list_simple.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about_me.html')    
        
if __name__ == '__main__':
    app.run(debug=True)
