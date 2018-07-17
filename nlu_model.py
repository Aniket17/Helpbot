from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data

from rasa_nlu.config import RasaNLUModelConfig
#from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.agent import Agent

def train (data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

def run():
    interpreter = Interpreter.load('./models/nlu/default/chat')

# def run(serve_forever=True):
#     interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
#     agent = Agent.load("models/dialogue", interpreter=interpreter)

#     if serve_forever:
#         agent.handle_channel(ConsoleInputChannel())
#     return agent

if __name__ == '__main__':
    #train('./data/training_data/', './config/config.yml', './models/nlu')
    run()