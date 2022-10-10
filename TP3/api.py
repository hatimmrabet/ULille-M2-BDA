import requests as req

class api:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def create_db(self, name):
        response = req.put(self.url+"/"+name, auth=(self.username, self.password))
        return response

    def delete_db(self, name):
        response = req.delete(self.url+"/"+name, auth=(self.username, self.password))
        return response

    def create_doc(self, db, docId, doc):
        response = req.put(self.url+"/"+db+"/_bulk_docs/"+docId, data=doc, auth=(self.username, self.password))
        return response

    def update_doc(self, db, doc, data):
        response = req.put(self.url+"/"+db+"/"+doc, data=data, auth=(self.username, self.password))
        return response

    def delete_doc(self, db, doc, rev):
        response = req.delete(self.url+"/"+db+"/"+doc+"?rev="+rev, auth=(self.username, self.password))
        return response

    
