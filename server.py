from flask import Flask, render_template
import requests
from settings import MY_CONTENT


app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(MY_CONTENT)
    all_posts = response.json()
    return render_template("index.html",posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)