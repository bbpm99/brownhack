# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACbd6379708d49701c81296828775341bf"
auth_token = "2a3050bfce087b70b4adeb60f1509a54"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+16106806680",
    from_="+19516671794 ",
    body="Hello there!")