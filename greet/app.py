from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    html = """
    <html>
      <body>
      <h1>Hello!</h1>
      <a href='/welcome'>Go to welcome page</a>
      <br><a href='/welcome/home'>Go to welcome home page</a>
      <br><a href='/welcome/back'>Go to welcome back page</a>
      </body>
    </html>"""
    return html


@app.route("/welcome")
# this is a decorator (@). It needs to have a function followed in order to decorate it
def welcome():

    # return html
    return "welcome"
    # this string will be used to construct a full HTTP response


@app.route("/welcome/home")
def welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    return "welcome back"
