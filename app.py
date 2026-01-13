from flask import Flask, render_template, request
import pywhatkit
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    status = None

    if request.method == "POST":
        phone = request.form["phone"]
        message = request.form["message"]

        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1

        if minute >= 60:
            minute -= 60
            hour += 1

        if hour >= 24:
            hour = 0

        pywhatkit.sendwhatmsg(phone, message, wait_time=10)
        status = "Message scheduled! Check WhatsApp Web."

    return render_template("index.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)
