# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client


# Find these values at https://twilio.com/user/account
account_sid = "ACbd6379708d49701c81296828775341bf"
auth_token = "2a3050bfce087b70b4adeb60f1509a54"

client = Client(account_sid, auth_token)
# Intro Message
client.api.account.messages.create(
    to="+16106806680",
    from_="+19516671794 ",
    body="Hello there! Welcome to Real Friends. Save this number in your contacts for future use. If you wnat a friendly conversation text back 'Ok'. If you want an emergency conversation text 'Help'.")




app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the messafe the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our response
    resp = MessagingResponse()

    # Determine the right reply
    if body =='Ok' or 'Help':
        #beginning
        if body == 'Ok':
            resp.message("How are you?")
        else:
            resp.message("What do you need help with?")
            
    # next replies
    else:
        resp.message("You suck")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
