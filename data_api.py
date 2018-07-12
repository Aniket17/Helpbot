import pyodbc
import nltk
from difflib import SequenceMatcher
import copy

class DataAPI(object):
    data = []
    PDFs = []
    def __init__(self):
        self.initData()
    def getContext(self):
        ctx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ANIKETD-M93\SQLEXPRESS;"
                      "Database=Scrapper.Importer.Context.ScrapperContext;"
                      "Trusted_Connection=yes;")
        return ctx
    
    def getCursor(self,ctx):
        cursor = ctx.cursor()
        return cursor

    def initData(self):
        if(len(self.data) != 0):
            print('data already init-ed')
            return
        ctx = self.getContext()
        cursor = self.getCursor(ctx)
        query = "SELECT * from data"
        cursor.execute(query)
        for row in cursor:
            obj = {}
            obj['id'] = row[0]
            obj['text'] = row[1]
            obj['link'] = row[2]
            obj['parent'] = row[3]
            self.data.append(obj)
    
    def search(self, product, version, keyword):    
        matches = self.getMatches(product, version,keyword)
        # search in text
        return matches

    def getMatches(self,product,version,sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        n_tags = [t[0] for t in tagged if t[1].startswith("N")]
        if(len(n_tags)<=0):
            return
        input_str = " ".join(n_tags)
        print("tags"+input_str)
        filtered_data = []
        for record in self.data:
            db_str = record["text"]
            rank = round(SequenceMatcher(lambda x: x == " ",input_str,db_str).ratio()*10)
            if(rank >= 4):
                rec = copy.deepcopy(record)
                rec["rank"] = rank
                filtered_data.append(rec)
        if(len(filtered_data) == 0 ):
            return []
        matches = sorted(filtered_data, key=lambda record: record['rank'], reverse=True)
        take = 3
        if( len(matches) < 3):
            take = len(matches)
        return matches[:take]
if __name__ == '__main__':
    #train('./data/training_data/', './config/config.yml', './models/nlu')
    api = DataAPI()
    matches = api.getMatches('','','Real-Time Solutions Installation Files"')
    print(matches)