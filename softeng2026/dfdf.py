from flask import Flask, request

app = Flask(__name__)

@app.route("/") 
def index():
    return """
<!DOCTYPE html>
<html lang="kr">
<head>
<meta charset="UTF-8">
<title>Flask Home Page</title>
</head>
<body>
<form method="GET" action="/gugu">
<h2>구구단 출력하기</h2>
<label>단 :
<input type="text" name="dan">
</label>
<button type="submit">출력</button>
</form>
</body>
</html>
"""

@app.route("/gugu")
def gugudan():
    dan_str = request.args.get("dan", "1")
    dan = int(dan_str)
    
    resp = "<html><head><title>gugudan</title></head>"
    resp += "<body>"
    resp += f"<h1>{dan}단 출력 결과</h1>"
  
    for i in range(1, 10):
        resp += f"<p>{dan} * {i} = <font color='blue'>{dan * i}</font></p>"
    
    resp += "<br><a href='/'>돌아가기</a>"
    resp += "</body></html>"
    return resp
 
if __name__ == "__main__":
    app.run(debug=True)