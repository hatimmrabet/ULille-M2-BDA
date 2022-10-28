import json
from API import API

def launchSimple(filename, db):
    monAPI = API()
    content = json.load(open(filename))
    monAPI.create_db(db)
    for doc in content:
        monAPI.create_doc(db, json.dumps(doc), doc["code"])

def launchMult(filename, db):
    monAPI = API()
    content = json.load(open(filename))
    monAPI.create_db(db)
    # diviser en paquet de 1000
    for i in range(0, len(content), 1000):
        monAPI.create_doc_mult(db, {"docs": content[i:i+1000]})

def myPostman():
    monAPI = API()
    print(monAPI.getLeastPopulatedCIty("france", 84).text) 

if __name__ == "__main__":
    # launchSimple("nord.json", "nord")
    # launchMult("france.json", "france")
    myPostman()
