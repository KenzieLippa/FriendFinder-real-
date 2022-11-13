import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
account_authtoken = os.getenv('TWILIO_ACCOUNT_AUTHTOKEN')
client = Client(account_sid,account_authtoken)

message = client.messages \
    .create(
        body="hello! thanks for using our app!  \n \n On a scale of 1-10, how are you feeling today? your sponsor will be notified if you are below a 5.",
        from_='+18438966460',
        to='+16179815553'
    )
print(message.sid)