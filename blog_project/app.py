from blog import app
import os

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'key' # os.urandom(16)
    app.run(debug=True, port=5000,)