from flask import Flask
from html import escape
app = Flask(__name__)


# routing
@app.route('/<name>')      # decorator
def hello(name):
    return "Hello  %s" % escape(name)
  @app.route('/')            # decorator
def hi():
    return "Hi  "


@app.route('/user/<int:id>')            # decorator
def Num(id):
    return "Number is %d " % id


@app.route('/path/<path:subpath>')      # decorator
def show_path(subpath):
    return "<h1>Hello<h1>  %s" % escape(subpath)


if __name__ == '__main__':
    app.run(debug=True)
