from blog import app

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'key'
    app.config['WTF_CSRF_SECRET_KEY'] = 'a random string'
    # app.config['RECAPTCHA_PARAMETERS'] = {'hl': 'zh', 'render': 'explicit'}
    # app.config['RECAPTCHA_DATA_ATTRS'] = {'theme': 'dark'}
    # app.config['RECAPTCHA_PUBLIC_KEY'] = "6Ld8WqgZAAAAACn_sXsa-hv2QiUD7jCgcH47HNq-"
    # app.config['RECAPTCHA_PRIVATE_KEY'] = "6Ld8WqgZAAAAAMCjoPEHwOdfCveZBTNnxFf3QKN2"
    app.run(debug=True, port=5000,)