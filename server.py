from flask import Flask, request, render_template
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis-master')
redis_port = int(os.getenv('REDIS_PORT', 6379))

app.logger.info(f"Connecting to Redis at {redis_host}:{redis_port}")
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            name = request.form['name']
            r.lpush('names', name)
        names = r.lrange('names', 0, -1)
    except redis.ConnectionError as e:
        app.logger.error(f"Redis connection error: {e}")
        names = []
    return render_template('index.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
