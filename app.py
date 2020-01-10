from flask import Flask

app = Flask(__name__)

@app.route("/") # Define the path to get to this function "/" means default domain
def home():
    return "<h1>Running Flask on Heroku!</h1>" # HTML code

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
