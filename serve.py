from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.channels import HttpInputChannel
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.channels.rest import HttpInputComponent
from flask import Blueprint, request, jsonify
from textblob import TextBlob

logger = logging.getLogger(__name__)
class SimpleWebBot(HttpInputComponent):
    """A simple web bot that listens on a url and responds."""

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/status", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @custom_webhook.route("/", methods=['POST'])
        def receive():
            payload = request.json
            sender_id = payload.get("sender", None)
            text = payload.get("message", None)
            if(len(text)>=3 and 'apa' not in text and 'rts' not in text):
                b = TextBlob(text)
                print(b.detect_language())
                if(b.detect_language() == 'mt'):
                    return jsonify(["Please try to form an understandable sentence"])
                if(b.detect_language() != 'en'):
                    return jsonify(["I am sorry but I only understand English! I am a quick lerner and learning other languages!"])
            out = CollectingOutputChannel()
            on_new_message(UserMessage(text, out, sender_id))
            responses = [m["text"] for m in out.messages]
            return jsonify(responses)
        return custom_webhook

def run(serve_forever=True):
    #path to your NLU model
    interpreter = RasaNLUInterpreter("models/nlu/default/chat")
    # path to your dialogues models
    agent = Agent.load("models/dialogue", interpreter=interpreter)
    #http api endpoint for responses
    input_channel = SimpleWebBot()
    if serve_forever:
        agent.handle_channel(HttpInputChannel(5004, "/chat", input_channel))
    return agent
if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    run()