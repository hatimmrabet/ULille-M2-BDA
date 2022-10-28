import json
import requests as req

class API:

    def __init__(self):
        self.url = "http://172.28.100.246:5984"
        self.username = "admin"
        self.password = "admin"

    def create_db(self, name):
        response = req.put(self.url+"/"+name, auth=(self.username, self.password))
        return response

    def delete_db(self, name):
        response = req.delete(self.url+"/"+name, auth=(self.username, self.password))
        return response

    def create_doc(self, db, doc, docID):
        response = req.put(self.url+"/"+db+"/"+docID, data=doc, auth=(self.username, self.password))
        return response
    
    def create_doc_mult(self, db, docs):
        response = req.post(self.url+"/"+db+"/_bulk_docs", data=json.dumps(docs), 
                    auth=(self.username, self.password), 
                    headers={"Content-Type": "application/json"})
        return response

    def update_doc(self, db, doc, data):
        response = req.put(self.url+"/"+db+"/"+doc, data=data, auth=(self.username, self.password))
        return response

    def delete_doc(self, db, doc, rev):
        response = req.delete(self.url+"/"+db+"/"+doc+"?rev="+rev, auth=(self.username, self.password))
        return response

    # methods pour la recherche
    def getLeastPopulatedCIty(self, db, codeRegion):
        response = req.post(self.url+"/"+db+"/_find", data=json.dumps({
            "selector": {
                "codeRegion": {"$eq": str(codeRegion)}
            },
            "execution_stats": True,
            "sort": [{"population": "desc"}],
            "limit": 1
        }), auth=(self.username, self.password), headers={"Content-Type": "application/json"})
        return response
