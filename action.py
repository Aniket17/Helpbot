from rasa_core.actions import Action
from rasa_core.events import SlotSet
import pyodbc

class DataAPI(object)
    def getContext():
        ctx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ANIKETD-M93\SQLEXPRESS;"
                      "Database=Scrapper.Importer.Context.ScrapperContext;"
                      "Trusted_Connection=yes;")
        return ctx
    def getCursor(ctx):
        cursor = ctx.cursor()
        return cursor
    
    def search(self, product, version, keyword):
        ctx = getContext()
        cursor = getCursor(ctx)
        cursor.execute('SELECT top 1 [link] from FROM [data] where text like "Real-Time Solutions"')
        # for row in cursor:
        #     print('row = %r' % (row,))
        return cursor[0]



class SearchAPI(object):
    def search(self, product, version, keyword):
        data_api = DataAPI()
        results = data_api.search(product, version, keyword)
        return results

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
        dispatcher.utter_message("is it ok for you? ")
        return []
