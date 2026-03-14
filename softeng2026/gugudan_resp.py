from flask import Flask

app = Flask(__name__)

@app.route("/gugu/<dan>")
def gugudan(dan):
    dan = int(dan)
    resp = "<html><head><title>gugudan</title></head>"
    resp += "<body>"
  
    for i in range(1, 10):
        resp += f"<p>{dan} * {i} =  <font color='blue'>{dan * i}</font></p>"
    resp += "</body></html>"
    print(resp)
    return resp
 
if __name__ == "__main__":
    app.run(debug=True)
