# From the flask module, import the Flask class.

from flask import Flask, render_template

# We need to create an app simply as an instance of the Flask class
app = Flask(__name__)


@app.route("/home")
def home():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
