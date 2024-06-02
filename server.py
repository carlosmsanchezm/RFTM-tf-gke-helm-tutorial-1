from flask import Flask, request, render_template
import redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis-master')
redis_port = os.getenv('REDIS_PORT', 6379)
print(f"Connecting to Redis at {redis_host}:{redis_port}")

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        r.lpush('names', name)
    names = r.lrange('names', 0, -1)
    return render_template('index.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
