from flask import Flask

app  = Flask(__name__)
app.secret_key = "fvjbdfkvbfd"

DATABASE = "users_lol"