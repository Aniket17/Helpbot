from rasa_core.actions import Action
from rasa_core.events import SlotSet
from data_api import DataAPI
import json

class SearchAPI(object):
    def search(self, product, version, keyword):
        api = DataAPI()
        results = api.search(product,version,keyword)
        return results

class ActionSearch(Action):
    def name(self):
        return 'action_search'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for information...")
        search_api = SearchAPI()
        product = tracker.get_slot("product")
        version = tracker.get_slot("version")
        keywords = tracker.get_slot("keywords")
        print(product)
        print(version)
        print(keywords)
        results = search_api.search(product, version, keywords)
        print(matches)
        return [SlotSet("matches", results)]

class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        product = tracker.get_slot("product")
        version = tracker.get_slot("version")
        keywords = tracker.get_slot("keywords")
        print(product)
        print(version)
        print(keywords)
        result = self.convertToLink(tracker.get_slot("matches"))
        response = json.dumps(result)
        print("******************************************************************")
        print("******************************************************************")
        print(response)
        print("******************************************************************")
        print("******************************************************************")
        dispatcher.utter_message(response)
        return []
    def convertToLink(self,matches):
        result = []
        for m in matches:
            link = "<li><a href='{1}'>{0}</a></li>".format(m["text"],m["link"])
            result.append(link)
        return result

