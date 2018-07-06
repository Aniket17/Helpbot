import logging
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    dialog_training_data_file = './data/stories.md'
    path_to_model = './models/dialogue'
    # domain = Domain()
    agent = Agent('chat_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])

    agent.train(
        dialog_training_data_file,
        augmentation_factor=50,
        epochs=500,
        batch_size=20,
        validation_split=0.2)
    agent.persist(path_to_model)