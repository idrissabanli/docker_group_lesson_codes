from blog import app

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'key'
    app.run(debug=True, port=5000,)