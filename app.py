# From the flask module, you want to import the Flask class.

from flask import Flask  # (importing the Flask class)

# We need to create an app simply as an instance of the Flask class
app = Flask(__name__)

@app.route("/")
def home():
  return "<p>This is Home Page</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
