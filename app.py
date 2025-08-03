# Contoh sebelumnya
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Halo! Aplikasi ini berjalan di Docker!'

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)

import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
# Ambil alamat host Redis dari environment variable, defaultnya 'redis'
redis_host = os.environ.get('REDIS_HOST', 'redis')
# Hubungkan ke database Redis
db = Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello_world():
    # Tambah nilai 'hits' sebanyak 1 setiap kali halaman diakses
    count = db.incr('hits')
    return f'Halo! Halaman ini telah dikunjungi sebanyak {count} kali.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)