from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('how.html')

#Do not touch this part
@app.route('/voicerecog')

@app.route('/user/<int:username>')
def show_user_profile(username=None):
    return render_template('user.html', name=username)

@app.route('/loop/<int:number>')
def loop(number=None):
    boo = (number == None)
    return render_template('loop.html',num=number,boo=boo)


if __name__ == '__main__':
    app.run(debug=True)
