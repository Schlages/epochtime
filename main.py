import os
import time
from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()
epoch_time = time.time()

@app.route('/epochtime/')
def get_time():
    epoch_time = time.time()

    return f"Current epoch time: {epoch_time}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)