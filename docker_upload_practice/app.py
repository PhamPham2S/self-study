from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Make it work, make it right, make it fast.",
    "Simplicity is the soul of efficiency."
]

@app.route('/')
def get_quote():
    return {'quote': random.choice(quotes)}

if __name__ == '__main__':
    # 도커 컨테이너 외부에서 접근 가능하도록 host='0.0.0.0' 설정 필수
    app.run(host='0.0.0.0', port=5000)