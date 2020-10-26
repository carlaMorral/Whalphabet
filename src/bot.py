from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import re

from consts import TAGS
from detect import detect_language
from translate_text import translate, detect_translate

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
 
    tl = re.compile('-translate -lan [a-z]{2,3} -text [a-zA-Z0-9]+')
    dt = re.compile('-detect [a-zA-Z0-9]+')
    dt_tl = re.compile('-all -lan [a-z]{2,3} -text [a-zA-Z0-9]+')

    if incoming_msg == '-show':
        response = TAGS
    elif tl.search(incoming_msg):
        split = incoming_msg.split(' ', 4)
        response = translate(split[4], split[2])
    elif dt.search(incoming_msg):
        split = incoming_msg.split(' ', 1)
        detection = detect_language(split[1])
        response = "Language detected: " + detection[0] + "\nScore: " + str(detection[1])
    elif dt_tl.search(incoming_msg):
        split = incoming_msg.split(' ', 4)
        result = detect_translate(split[4], split[2])
        if isinstance(result, str): response = result
        else: response = "Language detected: {}\nScore: {}\nText: {}".format(result[0], result[1], result[2])
    else:
        response = showHelp()

    msg.body(response)
    return str(resp)

def showHelp():
    return "Welcome to the cognitive bot! I can do the following things: \
            \n 1. Translate text: -translate -lan <TAG> -text <TEXT> \
            \n 2. Detect the language of a text: -detect <TEXT> \
            \n 3. Detect + translate: -all -lan <TAG> -text <TEXT> \
            \n 4. Show supported languages and their tags: -show"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)