from flask import Flask, render_template, request
import requests
import datetime
import smtplib

posts = requests.get("https://api.npoint.io/7d132abb9210de68d989").json()
current_year = datetime.datetime.now().year

MY_EMAIL = "inda4894@gmail.com"
MY_PASSWORD = "***"

app = Flask (__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts, year=current_year)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="v.saburov@yahoo.com", msg=email_message)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)