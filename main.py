# if you are not familiar with Twilio, first check the readme file
from flask import Flask, render_template, request
from twilio.rest import Client
account_sid = "xxxxx" # use your Twilio Account SID 
auth_token = "xxxxx" # use your Twilio Auth Token 
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/submit_message", methods=["POST", "GET"])
def send_sms():
    if request.method == "POST":
        pass
        message = request.form["message"]
        client.messages.create(
            body={message}, to="+421908944619", from_="+12564747323") # Replace my numbers with your own phone number and your Twilio phone number
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)