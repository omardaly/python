from flask import Flask, render_template, session, request,redirect
app = Flask(__name__)
app.secret_key="21354354534"

@app.route('/')
def index():
      return render_template("form.html")

@app.route('/process', methods=['POST'])
def result():
     session['full_name']=request.form['full_name']
     session['location']=request.form['location']
     session['language']=request.form['language']
     session['comment']=request.form['comment']
      
     return render_template("result.html")

# @app.route('/result')
# def result():
#      return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)