from flask import Flask, render_template, request


app = Flask(__name__)


#Do not touch this part
@app.route('/voicerecog')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)