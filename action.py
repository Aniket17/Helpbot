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
        search_api = SearchAPI()
        product = tracker.get_slot("product")
        version = tracker.get_slot("version")
        keywords = tracker.get_slot("keywords")
        print(product)
        print(version)
        print(keywords)
        if(product == None and keywords == None):
            return
        if(product != None and keywords == None):
            return
        results = search_api.search(product, version, keywords)
        return [SlotSet("matches", results)]

class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot("product")
        version = tracker.get_slot("version")
        keywords = tracker.get_slot("keywords")
        matches = tracker.get_slot("matches")
        if(product == None and keywords == None):
            dispatcher.utter_template("utter_no_keywords")
            dispatcher.utter_template("utter_structured_garbage")
            return
        if(product != None and keywords == None):
            dispatcher.utter_template("utter_product_page")
            dispatcher.utter_template("utter_structured_garbage")
            return
        if(matches == None or len(matches) == 0):
            dispatcher.utter_template("utter_no_keywords")
            return
        result = []
        print(product)
        print(version)
        print(keywords)
        filtered =[]
        wrong_version = None
        if(version != None):
            filtered = [x for x in matches if  x["version"] == version]
            if(len(filtered) == 0):
                wrong_version = True
                dispatcher.utter_message("I could not find '{keywords}' for '{product}' in '{version}'".format(**locals()))
            else:
                result = self.convertToLink(filtered)
        if(len(result) == 0):
            if(wrong_version != None and wrong_version == True):
                dispatcher.utter_message("This is what I could find for other versions.. :")
            result = self.convertToLink(tracker.get_slot("matches"))
        response = json.dumps(result)
        dispatcher.utter_message(response)
        return []
    def convertToLink(self,matches):
        result = []
        for m in matches:
            link = "<li><a href='{1}'>{0} - Version {2}</a></li>".format(m["text"],m["link"],m["version"])
            result.append(link)
        return result