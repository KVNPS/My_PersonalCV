from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = os.environ['My_Content']
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html",posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)