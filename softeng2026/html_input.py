from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>자유 주제 웹앱</title>
</head>
<body>
<h1>프리토픽 웹 애플리케이션</h1>
<section>
  <h2>1) 구구단 출력하기</h2>
  <form method="GET" action="/gugu">
    <label>단: <input type="number" name="dan" min="1" max="20" required></label>
    <button type="submit">출력</button>
  </form>
</section>
<section>
  <h2>2) 노래 장르 추천곡 생성기</h2>
  <form method="GET" action="/recommend">
    <label>장르:
      <select name="genre" required>
        <option value="클래식">클래식</option>
        <option value="인디">인디</option>
        <option value="테크노">테크노</option>
        <option value="사이키델릭">사이키델릭</option>
        <option value="나레이션">나레이션</option>
        <option value="시티팝">시티팝</option>
      </select>
    </label>
    <button type="submit">추천받기</button>
  </form>
</section>
</body>
</html>
'''

@app.route('/gugu')
def gugudan():
    dan = request.args.get('dan', '2')
    try:
        dan = int(dan)
    except ValueError:
        return '<html><body><h2>정수를 입력해주세요.</h2></body></html>'

    resp = '<html><head><title>구구단 결과</title></head><body>'
    resp += f'<h2>{dan}단 결과</h2>'
    for i in range(1, 10):
        resp += f"<p>{dan} x {i} = <strong style='color:blue;'>{dan * i}</strong></p>"
    resp += '</body></html>'
    return resp

@app.route('/recommend')
def recommend():
    genre = request.args.get('genre', '로맨스')
    suggest = {
        '클래식': [
            'Heidenröslein, D.257 (Schubert, Franz)',
            'Für Elise, Op. 93 (Beethoven, Ludwig van)',
            'Verdi: Il trovatore, Act4 Scene 1: Damor sullali rosee (Leonora)'
        ],
        '인디': [
            'Uso no Tabi - HonjitsuKyuen',
            '내게 남은 것 - 강찬구',
            'Farther than before - Way dynamic'
        ],
        '테크노': [
            'Pump - He said',
            'The Quotdian - Wiston Tong',
            'YMO - Taiso'
        ],
        '사이키델릭': [
            'Fazon - Sopwith Camel',
            'LIght My Fire - The Doors',
            'California Satin - Man'
        ],
        '시티팝': [
            'Silly Crush - Masaki Matsubara',
            'Moonlight Serenade - Tuxedo Junction',
            'E.S.P - Masayoshi Takanaka'
        ],
        '나레이션': [
            'Full Moon - Eden Ahbez',
            'While Drifting - The Sebastain String Quartet',
            'Come Love Me - Authur Prysock.'
        ]
    }
    message = random.choice(suggest.get(genre, ['노래 장르 추천입니다.']))
    return f'<html><head><title>추천 결과</title></head><body><h2>{genre} 노래 추천</h2><p>{message}</p></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
