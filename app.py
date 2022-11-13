
from flask import Flask, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms/", methods=['GET', 'POST'])
def sms_reply():
    console.log("hey bestie")
    print("slayyyy")
    body = request.values.get('Body').lowe()
    resp = MessagingResponse()
    if body in range(5, 11):
        resp.message("We're glad you're doing okay today! :)")
    elif body in range(1, 5):
        resp.message("we're sorry to hear that, your sponsor will be notified")
    else: 
        resp.message("Please respond with a number from 1-10. ")
    return Response(str(resp),  mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)