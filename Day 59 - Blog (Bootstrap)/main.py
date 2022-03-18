from flask import Flask, render_template
import requests
import datetime

posts = requests.get("https://api.npoint.io/7d132abb9210de68d989").json()
current_year = datetime.datetime.now().year

app = Flask (__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts, year=current_year)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")