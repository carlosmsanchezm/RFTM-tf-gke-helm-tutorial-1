from flask import Flask, request, render_template
import redis

app = Flask(__name__)
r = redis.Redis(host='redis-master', port=6379, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        r.lpush('names', name)
    names = r.lrange('names', 0, -1)
    return render_template('index.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
