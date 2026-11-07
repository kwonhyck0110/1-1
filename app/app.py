# app/app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # 환경변수로 메시지를 받을 수 있게 (보너스 '환경변수'로 확장 가능)
    msg = os.environ.get("APP_MSG", "Hello Docker Workstation!")
    return f"<h1>{msg}</h1>"

if __name__ == "__main__":
    # 0.0.0.0 으로 열어야 컨테이너 외부(호스트)에서 접속 가능
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)