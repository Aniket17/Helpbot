from rasa_core.actions import Action
from rasa_core.events import SlotSet
from data_api import DataAPI

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
        results = search_api.search(tracker.get_slot("product"),tracker.get_slot("version"),tracker.get_slot("keywords"))
        print(results)
        return [SlotSet("matches", results)]

class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        result = self.convertToLink(tracker.get_slot("matches"))
        print(result)
        return []
    def convertToLink(self,matches):
        result = []
        print(matches)
        for m in matches:
            try:
                link = "<a href='{0}'>{1}</a>".format(m.text,m.link)
                result.append(link)
                pass
            except Exception as identifier:
                print(identifier)
                print(m)
                pass
        return result

