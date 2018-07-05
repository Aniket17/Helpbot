from rasa_core.actions import Action
from rasa_core.events import SlotSet

class SearchAPI(object):
    def search(self, product, version, keyword):
        print(product)
        print(version)
        print(keyword)
        return "Searched completed for - "

class ActionSearch(Action):
    def name(self):
        return 'action_search'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for information...")
        search_api = SearchAPI()
        results = search_api.search(tracker.get_slot("product"),tracker.get_slot("version"),tracker.get_slot("keyword"))
        return [SlotSet("matches", results)]


class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 )
        return []
