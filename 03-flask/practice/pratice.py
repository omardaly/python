from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return"Hello world"

@app.route('/dojo')
def dojo():
    return"Dojo"

@app.route('/dojo/<say>')
def hi_say(say):
    return(f"Hi {say}")

@app.route('/repeat/<string:world>/<int:num>')
def repeat_word(word,num):
    repeat_word = word*num
    return(repeat_word)


if __name__ =='__main__':
    app.run(debug=True, port=5000)
    