# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
import random

# Find these values at https://twilio.com/user/account
account_sid = "ACbd6379708d49701c81296828775341bf"
auth_token = "2a3050bfce087b70b4adeb60f1509a54"

client = Client(account_sid, auth_token)
# Intro Message
client.api.account.messages.create(
    to="+16106806680",
    from_="+19516671794 ",
    body="Hello there! Welcome to Real Friends: a real friend for when your real friends aren't there. Save this number in your contacts for future use. Text 'Options' for options.")

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the messafe the user sent our Twilio number
    body = str(request.values.get('Body', None))
    body = body.lower()
    # Start our response
    resp = MessagingResponse()
    step1 = "Hey! It's been so long! How have you been? What is going on in your life?"
    run_res = ['CALL ME ASAP', 'We need to talk!','EMERGENCY', 'Call me as soon as you get this message.']
    step2 = "HAHAH That's awesome! I've been doing great actually! I just got a new job and a new dog! He's so cute omg you gotta see him. We should meet up sometime! When are you free??"
    ok_res = ["Hey! What are you going to do this weekend? I feel like I haven't seen you in forever!", 
    'How was your day? You do anything fun without me?', 'How have you been? I just bombed my math test :(', "What's up! You tryna hang out later? I know a REALLY good thai place nearby.", 'How is everything? Is everything good? Hopefully pretty good :)']
    step3 = "Okay thats good with me! I'll see you then!"
    other_res = ["That is nice! This week I went to the beach with my freinds. Would you want to go soon?", 
    "I have been really busy this week, but we should really hangout soon.", "I really miss you. You are my best friend. We need to see each other soon!", "Damn that is really cool.",
              "I wanna go to the mall soon, can you come with me?", "Lmao! I have been having the craziest week!"]

    mom_res = ['Come home immediately', "Bitch, I'm the adult here. Call me right now!", 'You are my least favorite child. Come home now!', 'OH HELL NO! GET YOUR ASS HERE!']

    love_res = ['I love you too babe', 'Aww you are too cute! <3', "Come over, my parents aren't home ;)", 'Damn, you are hot!', "I really want you right now"]
    
    # Determine the right reply
    if 'hey' in body:
        resp.message(random.choice(ok_res))
    #What's up! I'm so bored right now
    elif 'bored' in body:
    	resp.message(step1)
    #Oh nothing much, just hanging out with friends but everyone is on their phones :\ smh How have you been doing?
    elif 'phones' in body:
    	resp.message(step2)
    #is saturday good
    elif 'saturday' in body:
    	resp.message(step3)
    elif body == 'emergency':
        resp.message(random.choice(run_res))
    elif 'mom' in body:
        resp.message(random.choice(mom_res))
    elif 'babe' in body:
        resp.message(random.choice(love_res))
    elif body == 'options':
    	resp.message("'hey' to start a friendly conversation. 'emergency' to get an urgent message that requires you to step away. Include the keyword 'mom' for a very disapproving mother. Include keyword 'babe' to get a cute message from your significant other. ")
    else:
        resp.message(random.choice(other_res))
        
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
